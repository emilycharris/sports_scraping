from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.

def get_url_view(request): #change name
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



#def stats_scraping_view(request):
    #name = request.GET.get('name')
    #curr_hist = request.GET.get('curr_hist')
    #print(name, curr_hist)
    #player_url = get_url_view(name)
    #return render(request, 'index.html', {} )



# def get_temps(city):
#     content = requests.get("https://www.wunderground.com/cgi-bin/findweather/getForecast?query=" + city).text
#     souper = BeautifulSoup(content, 'html.parser')
#     current_temp = str(souper.find(id='curTemp'))
#     current_feels = str(souper.find(id='curFeel'))
#     return current_temp, current_feels
#
#
# def weather_scraping_view(request):
#     city = request.GET.get("city") or 'greenville south carolina'
#     print(city)
#     current_temp, current_feels = get_temps(city)
#     return render(request, 'index.html', {'current_temp': current_temp, "current_feels": current_feels, "city": city})
