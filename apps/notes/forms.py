from django import forms
from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'category']


class NoteEditForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ['title', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un título'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe el contenido...'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'category': 'Categoría',
        }
