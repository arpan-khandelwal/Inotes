from django import forms
from .models import Note
from django.contrib.auth.models import User

class NoteCreationForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['notes_title','note_text']

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['notes_title','note_text']   

class AccountSettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']