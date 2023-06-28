from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai


openai_api_key = 'ADD_KEY_HERE'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer


# Create your views here.
def render_index(request):
    return render(request, "Main.html")

def render_menu(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, "response": response})
    return render(request,"classgpt.html")