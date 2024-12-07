from django.shortcuts import render, get_object_or_404, redirect
from .models import GuestbookEntry
from .forms import GuestbookEntryForm

def entry_list(request):
    entries = GuestbookEntry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'guestbook/entry_list.html', {'entries': entries})

def entry_add(request):
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    else:
        form = GuestbookEntryForm()
    return render(request, 'guestbook/entry_form.html', {'form': form})

def entry_edit(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    else:
        form = GuestbookEntryForm(instance=entry)
    return render(request, 'guestbook/entry_form.html', {'form': form})

def entry_delete(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'guestbook/entry_confirm_delete.html', {'entry': entry})
