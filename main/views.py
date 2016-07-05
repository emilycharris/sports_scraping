from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.

def player_stats_view():
    hostname = 'http://www.nfl.com'
    content = requests.get('http://www.nfl.com/players/search?category=name&filter=travelle+wharton&playerType=historical')

    souper = BeautifulSoup(content.text, 'html.parser')
    player_name = souper.find(class_='tbdy').a.text
    player_url = hostname + souper.find(class_='tbdy').a.attrs['href']
    return player_name, player_url

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
