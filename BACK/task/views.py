from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def form_registro(request):
    return render(request, '.html', {
        'form': UserCreationForm
    })