from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import NoteCreationForm,NoteUpdateForm,AccountSettingsForm
from .models import Note

# Create your views here.
@login_required
def home_page(request):
    #import ipdb;ipdb.set_trace()
    current_user = request.user
    user_id = current_user.id
    notes = Note.objects.filter(user__id = user_id)
    form = NoteCreationForm()
    if request.method == "POST":
        form = NoteCreationForm(request.POST)
        if form.is_valid():
            note_obj = form.save(commit=False)
            note_obj.user = request.user
            note_obj.save()

            return redirect('noteapp:home_page')

    context={
        'notes' : notes,
        'form' : form,
    }
    return render(request,'noteapp/home.html',context)

# def addnote(request):
#     form = NoteCreationForm()
#     if request.method == "POST":
#         form = NoteCreationForm(request.POST)
#         if form.is_valid():
#             note_obj = form.save(commit=False)
#             note_obj.user = request.user
#             note_obj.save()

#             return redirect('noteapp:home_page')
#     return render(request,'noteapp/addnote.html')   


def index(request):
    return render(request,'noteapp/index.html')

def loggedout(request):
    return render(request,'noteapp/loggedout.html')

# def login(request):
#     return render(request,'noteapp/login.html')

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('noteapp:login')


    context ={
        'form':form
    }
    return render(request,'noteapp/register.html',context)

@login_required
def settings(request):
    user = request.user
    form = AccountSettingsForm(instance=user)
    if request.method == "POST":
        user.username = request.post["username"]
        user.first_name = request.post["first_name"]
        user.last_name = request.post["last_name"]

        user.save()
        messages.success(request,"Account Updated Successfully")
        
        return redirect("noteapp:settings")

    context={
        'form' : form,
        'user' : user,
    }
    return render(request,'noteapp/settings.html',context)

@login_required
def update(request,id):
    note_to_update = Note.objects.get(id=id)
    form = NoteUpdateForm(instance = note_to_update)

    if request.method == "POST":
        form = NoteUpdateForm(request.POST)
        if form.is_valid():
            note_to_update.notes_title = form.cleaned_data["notes_title"]
            note_to_update.note_text = form.cleaned_data["note_text"]

            note_to_update.save()

            return redirect('noteapp:home_page')
                
    context ={
        'note' : note_to_update,
        'form' : form
    }
    return render(request,'noteapp/update.html',context)

@login_required
def delete(request,id):
    note_to_delete = Note.objects.get(id=id)
    if request.method == "POST":
        note_to_delete.delete()
        return redirect('noteapp:home_page')
    
    return render(request,'noteapp/delete.html')
