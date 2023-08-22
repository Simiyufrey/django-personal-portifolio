from django import forms
from .models import Message


class Message_Form(forms.ModelForm):
    
    class Meta():
        model=Message
        fields=['email','message']

        labels={
            'email':'',
            'message':'',
            
        }

        widgets={
            'email':forms.EmailInput(attrs={'class':"form-control my-2","placeholder":"Email"}),
            'message':forms.TextInput(attrs={'class':'form-control my-2',"placeholder":"Message"})
        }