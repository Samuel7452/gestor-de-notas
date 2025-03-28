from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm
from .models import Notes
from apps.categories.models import Categories
from django.contrib import messages

def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/api/v1/notes/list/')
    else:
        form = NoteForm()
    
    return render(request, 'notes/note_form.html', {'form': form})


def list_notes(request):
    notes = Notes.objects.all().order_by('-created_at')
    categories = Categories.objects.all().order_by('-created_at')
    return render(request, 'notes/note_list.html', {'notes': notes, 'categories':categories}) 


def edit_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Nota actualizada con éxito")
            return redirect('/api/v1/notes/list/')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/edit_note.html', {'form': form, 'note': note})