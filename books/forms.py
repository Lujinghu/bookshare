from django.forms import ModelForm
from .models import Book


class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'iamge', 'intro', 'is_available')

