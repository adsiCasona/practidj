from django.shortcuts import render

def productos(request):
    prod=['compu','mouse','impresora','server']
    context={'listado':prod}
    return render(request, 'productos.html', context)
