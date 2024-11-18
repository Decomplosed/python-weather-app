import json
import os
import requests
from django.shortcuts import render


def home(request):
    url = f"https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2024-11-18&distance=5&API_KEY={os.getenv('API_KEY')}"
    api_request = requests.get("")
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})
