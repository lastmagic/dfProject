from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import UserForm
from .models import User
from .connect import get_characterId, get_response
import urllib.parse
from .parsing import extract_item, extract_creature, extract_skillName
HOST = 'https://api.neople.co.kr/df/servers/<serverId>/characters/<characterId>/skill/buff/equip/'
# Create your views here.
def home(request):
    return render(request, 'switching/home.html',{});

def info(request,serverName, characterName):
    # get해서 데이터 가져올 것
    cid = get_characterId(serverName, characterName)
    if cid == {'rows':[]}:
        return HttpResponse("캐릭터정보가 존재하지않습니다.")
    equipment = extract_item(get_response('equipment', serverName, cid), 'equipment')
    avatar = extract_item(get_response('avatar', serverName, cid),'avatar')
    creature = extract_creature(get_response('creature', serverName, cid), 'creature')
    skillInfo = extract_skillName(get_response('equipment', serverName, cid))
    switching_info = {'equipment':equipment, 'avatar':avatar, 'creature':creature, 'skillInfo':skillInfo}
    return render(request, 'switching/info.html', switching_info)

def test(request):
    return render(request, 'switching/test.html', {});
