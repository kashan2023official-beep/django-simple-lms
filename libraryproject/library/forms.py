from django import forms
from .models import BorrowRecord


class BorrowRecordForms(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['book','member']

