from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = message,
        max_tokens = 150,
        n = 1,
        stop = None,
        temperature = 0.7,
    )
    
    answer = response.choices[0].text.strip() # type: ignore
    return answer


# Create your views here.
#def render_index(request):
    return render(request, "Main.HTML")

def chatbot(request):
    
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, "response": response})
    return render(request,"classgpt.html")
#def render_menu(request):
    return render(request,"classgpt.html")

def login(request):      
    if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = auth.authenticate(request,email=email, password=password)
            if user is not None:
                auth.login(request, user)
                print("user logged in")
                return render(request,'classgpt.html')
            else:
                error_message = 'Invalid username or password'
                print("error")
                return render(request, 'Main.HTML', {'error_message': error_message})
    else:
        return render(request, 'Main.HTML')
def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            try:
                user = User.objects.create_user(email, password,first_name=fullname)
                user.first_name = fullname
                user.save()
                auth.login(request, user)
                return redirect('Main.HTML')
            except:
                error_message = 'Error creating account'
                return render(request, 'Main.HTML', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'Main.HTML', {'error_message': error_message})
    return render(request,'Main.HTML')
    
            
            
def logout(request):
    auth.logout(request)
    return redirect('Main.HTML')