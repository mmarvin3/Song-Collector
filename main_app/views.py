
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Home</h1>')

def about(request):
  return render(request, 'about.html')

def songs_index(request):
  return HttpResponse('<h1>Songs from the SongCollector</h1>')
