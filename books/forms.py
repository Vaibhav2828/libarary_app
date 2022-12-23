from django import forms
from books.models import BookModel

class BookModelForms(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'