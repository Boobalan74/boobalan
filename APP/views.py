from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserRegisterationForm, UserPersonalForm
from .models import UserPersonalModel


def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterationForm()
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect("Login_3")
        
    context = {'form':form}
    return render(request, "2_Register.html", context)

def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)
    
def Logout(request):
    logout(request)
    return redirect('Login_3')


@login_required(login_url='Login_3')
def Home_4(request):
    return render(request, '4_Home.html')

@login_required(login_url='Login_3')
def Per_Info_5(request):
    
    if request.method == 'POST':
        print('Data is valid')
        form = UserPersonalForm(request.POST, request.FILES)
        if form.is_valid():
            print('Personal form is valid')
            form.save()
            return redirect('Home_4')
        else:
            return render(request, '5_Per_Info.html', {'form':form})
    else:
        form = UserPersonalForm()      
        return render(request, '5_Per_Info.html', {'form':form})

@login_required(login_url='Login_3')     
def Per_Database_6(request):
    models = UserPersonalModel.objects.all()
    return render(request, '6_Per_Database.html', {'models':models})


@login_required(login_url='Login_3')
def update(request, id):  
    models = UserPersonalModel.objects.get(id=id)  
    form = UserPersonalForm(request.POST, instance = models)  
    if form.is_valid():  
        form.save()  
        return redirect("Per_Database_6")  
    return render(request, '5_Per_Info.html', {'models': models})  


@login_required(login_url='Login_3')
def delete(request, id):  
    models = UserPersonalModel.objects.get(id=id)  
    models.delete()  
    return redirect("Per_Database_6")

from django.core.mail import EmailMessage
from django.http import HttpResponse  
from .forms import ContactForm
from django.shortcuts import render  
import os 

@login_required(login_url='Login_3')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            image = form.cleaned_data['image']

            email_subject = 'This is surya from outer space'
            email_body = f"name: {name} \n Email: {email} \n\n Message:\n {message}"

            recipient_email = [email, 'mailjavasend@gmail.com']

            email = EmailMessage(email_subject, email_body, to=recipient_email)  
            
            pdf_file = form.cleaned_data['pdf_file']

            email.attach(pdf_file.name, pdf_file.read(), pdf_file.content_type)
            
            email.attach(image.name, image.read(), image.content_type)
            
            email.send()

            return HttpResponse("Success!")
    else:
        form = ContactForm()

    return render(request, 'email.html', {'form': form})
