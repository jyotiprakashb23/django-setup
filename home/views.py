from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35},
]
def home(request):
    return render(request, 'home/index.html', context={'people': people})

def success_page(request):
    return HttpResponse("<h1>This is a success page!</h1>")