import logging
from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note

# Create your views here.


logger = logging.getLogger(__name__)

TEMPLATES_PATH = 'note/'

LIST_URI = '/notes/note_list/'


def note_create_form(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(LIST_URI)
            except Exception as e:
                logger.error(e)
                pass
    else:
        form = NoteForm()
    return render(request, f'{TEMPLATES_PATH}note_create_form.pug', {'form': form})


def note_edit_form(request, id):
    note = Note.objects.get(id=id)
    form = NoteForm(request.POST, instance=note)
    if form.is_valid():
        try:
            form.save()
            return redirect(LIST_URI)
        except Exception as e:
            logger.error(e)
            pass
    return render(request, f'{TEMPLATES_PATH}note_edit_form.pug', {'note': note})


def note_list(request):
    notes = Note.objects.all()
    return render(request, f'{TEMPLATES_PATH}note_list.pug', {'notes': notes})


def note_edit(request, id):
    note = Note.objects.get(id=id)
    return render(request, f'{TEMPLATES_PATH}note_edit_form.pug', {'note': note})


def note_delete(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return redirect(LIST_URI)
