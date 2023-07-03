from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import User, Chat
from django.utils import timezone


openai_api_key = 'ADD_KEY_HERE'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are an helpful assistant.'},
            {'role': 'user', 'content': message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer


# Create your views here.
#def render_index(request):
#    return render(request, 'Main.html')

#THIS IS THE CHATBOT IN THE GITHUB REPO
@login_required(login_url='login')
def render_menu(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request,'classgpt.html', {'chats': chats})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('render_menu')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'Main.html', {'error_message': error_message})
    else:
        return render(request, 'Main.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                print('Success creating account')
                return redirect('render_menu')
            except:
                error_message = 'Username and/or Email Already Exists'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Passwords do not match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')