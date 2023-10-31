from inertia import render
from django.http import HttpResponse
    
# Ruta Index
def index(request):
    lista = []
    lista.append(12)
    return render(request,'Index',props={
        'array': lista
    })

#region View Solicitudes NC
### Punto de Venta
def notaPDV(request):
    lista = []
    lista.append(12)
    return render(request,'NotaPDV',props={
        'array': lista
    })
### Financieros
def notaFinanciero(request):
    lista = []
    lista.append(12)
    return render(request,'NotaFinancieros',props={
        'array': lista
    })
### Servicios
def notaServicios(request):
    lista = []
    lista.append(12)
    return render(request,'NotaServicios',props={
        'array': lista
    })
#endregion

#region View Consolidacion NC
### Punto de Venta
def cnotaPDV(request):
    lista = []
    lista.append(12)
    return render(request,'CNotaPDV',props={
        'array': lista
    })
### Financieros
def cnotaFinanciero(request):
    lista = []
    lista.append(12)
    return render(request,'CNotaFinancieros',props={
        'array': lista
    })
### Servicios
def cnotaServicios(request):
    lista = []
    lista.append(12)
    return render(request,'CNotaServicios',props={
        'array': lista
    })
#endregion

#region View Bandeja NC
### Punto de Venta
def bnotaPDV(request):
    lista = []
    lista.append(12)
    return render(request,'BNotaPDV',props={
        'array': lista
    })
### Financieros
def bnotaFinanciero(request):
    lista = []
    lista.append(12)
    return render(request,'BNotaFinancieros',props={
        'array': lista
    })
### Servicios
def bnotaServicios(request):
    lista = []
    lista.append(12)
    return render(request,'BNotaServicios',props={
        'array': lista
    })
#endregion

# Ruta para login sesion
def login_successful(request):
    return HttpResponse("Hey, login successful.")