from django.shortcuts import render
import json 
import urllib.request  # urllib.request to make a request to api 

from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        try:
            error=0
            city = request.POST.get('city')
            
            # Ensure the query string is correctly formatted without spaces
            source = urllib.request.urlopen(
                f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=xxxxxxxxxxxxxxxxxxx'
            ).read()

            #USE UR OWN API KEY......

            list_of_data = json.loads(source)

            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ' '
                            + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + 'k',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
            print(data)
        except:
            error={}
            return render(request, 'index.html', error)
    else:
        data = {}

    return render(request, 'index.html', data)