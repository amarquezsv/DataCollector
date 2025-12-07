# tracker/views.py
import requests
from django.shortcuts import render, redirect
from .models import CovidData

def extract_data(request):
    url = "https://disease.sh/v3/covid-19/countries/usa?strict=true"
    response = requests.get(url).json()

    CovidData.objects.create(
        country=response["country"],
        cases=response["cases"],
        deaths=response["deaths"],
        recovered=response["recovered"]
    )
    return redirect("show_data")

def show_data(request):
    data = CovidData.objects.all().order_by("-updated_at")
    return render(request, "tracker/show_data.html", {"data": data})