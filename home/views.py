from django.shortcuts import render

def inicio(request):
    client=['Cliente_uno','Cliente_dos','Cliente_tres','Cliente_cuatro']
    context={'listado':client}
    return render(request, 'home.html', context)