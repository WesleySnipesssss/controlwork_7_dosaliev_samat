from django import forms
from .models import GuestbookEntry

class GuestbookEntryForm(forms.ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ['author_name', 'author_email', 'text', 'status']
