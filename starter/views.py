from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Service,Skill,Message
from .forms import Message_Form
from django.urls import reverse
# Create your views here.


def landing(request):
    service=Service.objects.all()
    skill=Skill.objects.all().order_by('-s_perce')
    form=Message_Form()
    return render(request,"starter/landing.html",{'services':service,'skills':skill,'form':form})

def Services(request):
    
    if request.method =="POST":
        pass
    else:
        service=Service.objects.all()
        
        return service
def send_message(request):
    if request.method== "POST":
        form=Message_Form(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            if message :
                message=Message(email=email,message=message,entry_type="mess")
                message.save()
        else:
             email=request.POST['email']
             message=Message(email=email,message="",entry_type="subs")
             message.save()
        return  HttpResponseRedirect(reverse("index"))

                
            
    else:
        return HttpResponseRedirect(reverse("index"))

        