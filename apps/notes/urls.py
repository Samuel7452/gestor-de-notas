from django.urls import path
from .functions import create_note, list_notes, edit_note
from .views import NotesAPIView,NoteDeleteView,NotesUpdateView

urlpatterns = [
    path('notes/', NotesAPIView.as_view(), name='notes'),
    path('notes/new/', create_note, name='create_note'),
    path('notes/list/', list_notes, name='list-notes'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('notes/edit/<int:note_id>/', edit_note, name='edit-note'),
    path('notes/<int:pk>/update/', NotesUpdateView.as_view(), name='note-update'),
]



