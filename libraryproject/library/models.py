from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

def get_due_date():
    return  timezone.now().date() + timedelta(days=14)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField()
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title
    


### member

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    membership_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    



#foreign keysssss ka concept dawg




class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)
    due_date = models.DateField(default=get_due_date)


    def __str__(self):
        return f"{self.member.name} borrowed {self.book.title}"
    
