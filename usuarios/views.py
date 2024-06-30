from django.shortcuts import render
from . models import Usuarios,Genero
from django.http import HttpResponseRedirect
from .forms import GeneroForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context={}
    return render(request, 'usuarios/index.html', context)

def base(request):
    usuarios=Usuarios.objects.all()
    context={"usuarios":usuarios}
    return render(request, 'usuarios/base.html', context)

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

def listadoSQL(request):
    usuarios=Usuarios.objects.raw('SELECT * FROM usuarios_usuarios')
    print(usuarios)
    context={"usuarios":usuarios}
    return render(request, 'usuarios/listadoSQL.html', context)

def crud(request):
    usuarios=Usuarios.objects.all()
    context={'usuarios':usuarios}
    return render(request, 'usuarios/usuarios_list.html',context)

def usuariosAdd(request):
    if request.method is not "POST":
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'usuarios/usuarios_add.html',context)
    else:
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo=request.POST["activo"]

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Usuarios.objects.create(    rut=rut,
                                        nombre=nombre,
                                        apellido_paterno=aPaterno,
                                        apellido_materno=aMaterno,
                                        fecha_nacimiento=fechaNac,
                                        id_genero=objGenero,
                                        telefono=telefono,
                                        email=email,
                                        direccion=direccion,
                                        activo=activo)
        obj.save()
        context={"mensaje":"Ok, datos grabados..."}
        return render(request, 'usuarios/usuarios_add', context)
 
def usuarios_del(request,pk):
    context=()
    try:
        usuarios=Usuarios.objects.get(rut=pk)

        usuarios.delete()
        mensaje="Bien, datos eliminados..."
        usuarios=Usuarios.objects.all()
        context={'usuarios':usuarios, 'mensaje': mensaje}
        return render(request, 'usuarios/usuarios_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        usuarios=Usuarios.objects.all()
        context={'usuarios':usuarios, 'mensaje':mensaje}
        return render(request, 'usuarios/usuarios_list.html')
    
def usuarios_findEdit(request,pk):
    if pk !="":
        usuarios=Usuarios.objects.get(rut=pk)
        generos=Genero.objects.all()

        print(type(usuarios.id_genero.genero))

        context={'usuarios':usuarios,'generos':generos}
        if usuarios:
            return render(request, 'usuarios/usuarios_edit.html',context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render(request, 'usuarios/usuarios_list.html',context)
        
def alumnosUpdate(request):
    if request.method == "POST":
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo=request.POST["activo"]

        objGenero=Genero.objects.get(id_genero = genero)
        usuarios=Usuarios
        usuarios.rut=rut,
        usuarios.nombre=nombre,
        usuarios.apellido_paterno=aPaterno,
        usuarios.apellido_materno=aMaterno,
        usuarios.fecha_nacimiento=fechaNac,
        usuarios.id_genero=objGenero,
        usuarios.telefono=telefono,
        usuarios.email=email,
        usuarios.direccion=direccion,
        usuarios.activo=activo
        usuarios.save()
        generos=Genero.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'generos':generos,'alumno':usuarios}
        return render(request, 'usuarios/usuarios_edit.html', context)
    else:
        usuarios=Usuarios.objects.all()
        context={'usuarios':usuarios}
        return render(request, 'usuarios/usuarios_list.html')