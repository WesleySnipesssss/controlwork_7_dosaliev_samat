from django import forms
from .models import GuestbookEntry

class GuestbookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['author_name', 'author_email', 'text', 'status']

class SearchForm(forms.Form):
    q = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Введите имя автора'})
    )