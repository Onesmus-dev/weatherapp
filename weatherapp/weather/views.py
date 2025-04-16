from django.shortcuts import render
import requests

def weather(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']
        source = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=9a6bb4dbe1d571d242fdaece62f15d1f"
        list_of_data = requests.get(source.format(city)).json()

        data = {
            'city': city.title(),
            'country_code': list_of_data['sys']['country'],
            'coordinate': f"{list_of_data['coord']['lon']}, {list_of_data['coord']['lat']}",
            'temp': round((list_of_data['main']['temp'] - 32) * 5.0 / 9.0),
            'humidity': list_of_data['main']['humidity'],
            'description': list_of_data['weather'][0]['description'].title(),
            'icon': list_of_data['weather'][0]['icon'],
            'main_weather': list_of_data['weather'][0]['main']  # NEW
        }

    return render(request, 'weather.html', data)
