from django.shortcuts import render, redirect
from .models import Book 
from .models import Member
from .models import BorrowRecord
from .forms import BorrowRecordForms
from django.utils import timezone
from django.core.mail import send_mail

# Create your views here.


##For all books

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books':books})
  
  
  
##addding one
def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title = request.POST['title'],
            author = request.POST['author'],
            isbn = request.POST['isbn'],
            total_copies = request.POST['total_copies'],
            available_copies = request.POST['total_copies'],

        )
        return redirect('book_list')
    return render(request, 'library/add_book.html')


### editing


def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.total_copies = request.POST['total_copies']
        book.save()
        return redirect('book_list')
    return render(request, 'library/edit_book.html', {'book':book})

## delete


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_list')



##member list
def member_list(request):
    members = Member.objects.all()
    return render(request, 'library/member_list.html', {'members':members})



##add member



def add_member(request):
    if request.method == 'POST':
        Member.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            is_active = request.POST.get('is_active') == 'on'
        )
        return redirect('member_list')
    return render(request, 'library/add_member.html')


def edit_member(request, member_id):
    member = Member.objects.get(id=member_id)
    if request.method == 'POST':
        member.name = request.POST['name']
        member.email = request.POST['email']
        member.is_active = request.POST.get('is_active') == 'on'
        member.save()
        return redirect('member_list')
    return render(request, 'library/edit_member.html', {'member':member})

#### delete



def delete_member(request, member_id):
    member = Member.objects.get(id= member_id)
    member.delete()
    return redirect('member_list')




##### formssssss
def borrow_book(request):
    if request.method == 'POST':
        form = BorrowRecordForms(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            if record.book.available_copies > 0:
                record.book.available_copies -= 1
                record.book.save()
                record.save()

                send_mail(
                    'Book Borrowed Confirmation',
                    f"Hi {record.member.name},\n\nYou borrowed '{record.book.title}' by {record.book.author} on {record.borrow_date}.\n\nPlease return it on time.",
                    'library@example.com',
                    [record.member.email],
                    fail_silently=False,

                )
                return redirect('book_list')
    else:
        form = BorrowRecordForms()
    return render(request, 'library/borrow_book.html', {'form':form})
    


###returning book
def return_book(request, record_id):
    record = BorrowRecord.objects.get(id=record_id)
    record.returned = True
    record.return_date = timezone.now().date()
    record.save()

    record.book.available_copies += 1
    record.book.save()

    return redirect('borrow_list')




## borrow list


def borrow_list(request):
    records = BorrowRecord.objects.all().order_by('-borrow_date')
    return render(request, 'library/borrow_list.html', {'records': records})




def home(request):
    return render(request, 'library/index.html')



