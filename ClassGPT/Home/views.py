from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai


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
    
    answer = response.choices[0].text.strip()
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