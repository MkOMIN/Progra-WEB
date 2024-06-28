from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'usuarios/index.html')

def contacto(request):
    context={}
    return render(request, 'usuarios/contacto.html', context)

def contra_olvido(request):
    context={}
    return render(request, 'usuarios/contra_olvido.html', context)

def inicio_sesion(request):
    context={}
    return render(request, 'usuarios/inicio_sesion.html', context)

def registro(request):
    context={}
    return render(request, 'usuarios/registro.html', context)

def trabajo1(request):
    context={}
    return render(request, 'usuarios/trabajo1.html', context)

def trabajo2(request):
    context={}
    return render(request, 'usuarios/trabajo2.html', context)

def trabajo3(request):
    context={}
    return render(request, 'usuarios/trabajo3.html', context)

def trabajos(request):
    context={}
    return render(request, 'usuarios/trabajos.html', context)

def carrito(request):
    context={}
    return render(request, 'usuarios/carrito.html', context)