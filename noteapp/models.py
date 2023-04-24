from django.db import models
from django.contrib.auth.models import User
import datetime 
from django.utils import timezone
# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes_title = models.CharField(max_length=200,null = False)
    note_text = models.TextField(null = False)
    Created_on = models.DateTimeField(auto_now_add=True )
    Last_Update_date = models.DateTimeField(auto_now= True,blank=True)
    def __str__(self):
        return self.notes_title
    def was_published_recently(self):
        return self.Created_on >= timezone.now() - datetime.timedelta(days=1)