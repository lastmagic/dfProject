from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import UserForm
from .models import User
from .connect import get_characterId, get_response
import urllib.parse
HOST = 'https://api.neople.co.kr/df/servers/<serverId>/characters/<characterId>/skill/buff/equip/'
# Create your views here.
def home(request):
    return render(request, 'switching/home.html',{});

def info(request,serverName, characterName):
    # get해서 데이터 가져올 것
    cid = get_characterId('prey','리막이')
    user = get_response('equipment', 'prey', cid)
    return render(request, 'switching/info.html', {'user':user})

def test(request):
    return render(request, 'switching/test.html', {});
