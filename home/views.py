from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hola, me encuentro en la aplicación Home</h1>")

def home(request):
    return HttpResponse("<h2>Hola, esta es un segunda función de Home</h2>")