from django.shortcuts import render

# Create your views here.
def render_index(request):
    return render(request, "Main.html")

def render_menu(request):
    return render(request,"classgpt.html")