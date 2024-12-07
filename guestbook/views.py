from django.shortcuts import render, get_object_or_404, redirect
from .models import GuestbookEntry
from .forms import GuestbookEntryForm, SearchForm
from django.core.paginator import Paginator


def entry_list(request):
    query = request.GET.get('q', '').strip()
    entries = GuestbookEntry.objects.filter(status="active").order_by('-created_at')
    if query:
        entries = entries.filter(author_name__icontains=query)

    form = GuestbookEntryForm()

    context = {
        'entries': entries,
        'form': form,
    }

    paginator = Paginator(entries.order_by('-created_at'), 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request, 'guestbook/entry_list.html', context)

    form = SearchForm(request.GET or None)
    return render(request, 'guestbook/entry_list.html', {'entries': entries, 'form': form})

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

    context = {
        'form': form,
        'entry': entry,
    }
    return render(request, 'guestbook/entry_form.html', {'form': form})

def entry_delete(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)

    context = {'entry': entry}

    if request.method == 'POST':
        entered_email = request.POST.get('email', '')
        if entered_email == entry.author_email:
            entry.delete()
            return redirect('entry_list')
        else:
            context['error_message'] = 'Введена неверная почта.'
            return render(request, 'guestbook/delete_entry.html', context)

    return render(request, 'guestbook/delete_entry.html', context)