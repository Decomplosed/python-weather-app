import json
import os
import requests
from django.shortcuts import render

def home(request):
    url = f"https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=89129&date=2024-11-18&distance=5&API_KEY={os.getenv('API_KEY')}"
    api_request = requests.get(url)

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
