from django import forms
from .models import GuestbookEntry

class GuestbookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['author_name', 'author_email', 'text']
        widgets = {
            'author_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'author_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваш email'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст сообщения'}),
        }

class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя автора'})
    )