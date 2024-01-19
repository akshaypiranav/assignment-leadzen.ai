from django.shortcuts import render,redirect
from django.contrib import messages
import requests
from .models import City

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=91a2f279a911b959507f20df3520d84d&units=metric'

    if request.method == "POST":
        name = request.POST.get("name")
        print(name)

        if not City.objects.filter(Cname=name):
            response = requests.get(url.format(name))

            if response.status_code == 200:
                weather_data = response.json()
                print(weather_data)
                city = City(Cname=name)
                city.save()
                messages.success(request, f"{name} added successfully")
            else:
                print("Error:", response.status_code)

    cities = City.objects.all()
    city_values = []

    for city in cities:
        response = requests.get(url.format(city.Cname)).json()
        city_data = {
            'id':city.id,
            'city_name': city.Cname,
            'temp': response['main']['temp'],
        }
        city_values.append(city_data)

    return render(request, "index.htm", {"city_values": city_values})


def delete(request,id):
    if(City.objects.filter(id=id).exists()):
        data=City.objects.get(id=id)
        data.delete()
    return redirect("/")