from django.contrib import admin

# Register your models here.
from . models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ["notes_title", "Last_Update_date", "Created_on"]


admin.site.register(Note,NoteAdmin)