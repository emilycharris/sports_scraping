from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.

def get_player_stats(request):
    hostname = 'http://www.nfl.com'
    player_name = request.GET.get('name') or 'brees'
    player_type = request.GET.get('historical') or 'current'
    content = requests.get(hostname + '/players/search?category=name&filter={}&playerType={}'.format(player_name, player_type)).text
    souper = BeautifulSoup(content, 'html.parser')
    player_url = hostname + (souper.find(id='result').a.attrs['href'])
    content = requests.get(player_url)
    souper = BeautifulSoup(content.text, 'html.parser')
    player_bio = str(souper.find(id='player-profile-wrapper'))
    player_stats = str(souper.find(id='player-stats-wrapper'))
    return render(request, 'index.html', {'player_bio': player_bio, 'player_stats':player_stats})
