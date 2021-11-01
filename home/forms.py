from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import addstudent,addbook

class AddStudentForm(ModelForm):
    class Meta:
        model=addstudent
        fields=['name','email','enrollment','branch','year','sem','mobile','address']
        
class AddBookForm(ModelForm):
    class Meta:
        model=addbook
        fields=['name','author','des','language','genres','year','student','img']