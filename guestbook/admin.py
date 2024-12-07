from django.contrib import admin
from .models import GuestbookEntry

@admin.register(GuestbookEntry)
class GuestbookEntryAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_email', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('author_name', 'author_email', 'text')
