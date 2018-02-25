from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import UserForm
from .models import User
# Create your views here.
def home(request):
    return render(request, 'switching/home.html',{});

def info(request,serverName, characterName):
    try:
        user = User.objects.get(serverName=serverName, characterName=characterName)
    except:
        user = ''

    return render(request, 'switching/info.html', {'user':user})

def test(request):
    return render(request, 'switching/test.html', {});
