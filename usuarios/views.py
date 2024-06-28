from django.shortcuts import render
from . models import Usuarios,Genero
from django.http import HttpResponseRedirect
from .forms import GeneroForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context={}
    return render(request, 'usuarios/index.html', context)

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

#ADMIN
def admin(request):
    usuarios= Usuarios.objects.all()
    context={"usuarios":usuarios}
    return render(request, 'usuarios/visionadmin.html', context)

def alumnosAdd(request):
    if request.method != "POST":
        generos=Genero.objects.all()
        context={"generos":generos}
        return render(request, 'myApp/alumnos_add.html', context)
    
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
        
        
        objGenero=Genero.objects.get(id_genero = genero)
        obj=Usuarios.objects.create(  rut=rut,
                                    nombre=nombre,
                                    apellido_paterno=aPaterno,
                                    apellido_materno=aMaterno,
                                    fecha_nacimiento=fechaNac,
                                    id_genero=objGenero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    )
        obj.save()
        context={'mensaje':"Ok, datos grabados..."}
        return render(request, 'usuarios/usuarios_add.html', context)
        
        


def crud(request):
    usuarios=Usuarios.objects.all()
    context={"usuarios":usuarios}
    return render(request, 'usuarios/usuarios_list.html', context)


def usuarios_del(request,pk):
    context={}
    try:
        usuarios=Usuarios.objects.get(rut=pk)
        
        usuarios.delete()
        mensaje="Bien, datos aliminados..."
        usuarios = Usuarios.objects.all()
        context = {'usuarios':usuarios, 'mensaje':mensaje }
        return render(request, 'usuarios/usuarios_list.html', context)
    except:
        mensaje="Error, rut no existe..."
        usuarios = Usuarios.objects.all()
        context = {'usuarios': usuarios, 'mensaje': mensaje}
        return render(request, 'usuarios/usuarios_list.html', context)
    
    
def usuarios_findEdit(request,pk):
    
    if pk != "":
        usuarios=Usuarios.objects.get(rut=pk)
        generos=Genero.objects.all()
        
        print(type(usuarios.id_genero.genero))
        
        context={'usuarios':usuarios, 'generos':generos}
        if usuarios:
            return render(request, 'usuarios/usuarios_edit.html', context)
        else:
            context={'mensaje':'Error, rut no existe...'}
            return render(request, 'usuarios/usuarios_list.html', context)
        
        
def usuariosUpdate(request):
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
        
        
        objGenero=Genero.objects.get(id_genero = genero)
        
        usuarios = Usuarios()
        usuarios.rut=rut
        usuarios.nombre=nombre
        usuarios.apellido_paterno=aPaterno
        usuarios.apellido_materno=aMaterno
        usuarios.fecha_nacimiento=fechaNac
        usuarios.id_genero=objGenero
        usuarios.telefono=telefono
        usuarios.email=email
        usuarios.direccion=direccion
        usuarios.save()       
        generos= Genero.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'generos':generos, 'usuarios':usuarios}
        return render(request, 'usuarios/usuarios.html', context)
    
    else:
        usuarios = Usuarios.objects.all()
        context= {'usuarios':usuarios}
        return render(request, 'usuarios/usuarios_edit.html', context)
    
    
def crud_generos(request):
    
    generos=Genero.objects.all()
    context ={'generos':generos}
    print("enviado datos generos_list")
    return render(request,"usuarios/generos_list.html",context)


def generosAdd(request):
    print("controlador generosAdd...")
    context={}
    
    if request.method == "POST":
        print("es un POST...")
        form = GeneroForm(request.POST)
        if form.is_valid:
            print("estoy en agregar...")
            form.save()
            
            form=GeneroForm()
            
            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request,"usuarios/generos_add.html",context)
    else:
        form = GeneroForm()
        context={'form':form}
        return render(request, 'usuarios/generos_add.html',context)
    
    
def generos_del(request, pk):
    mensajes=[]
    errores=[]
    generos = Genero.objects.all()
    try:
        genero = Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            genero.delete()
            mensajes.append("bien, datos eliminados...")
            context = {'generos':generos, 'mensajes': mensajes, 'errores':errores}
            return render(request, 'usuarios/generos_list.html', context)
    except:
        print("error, id no existe...")
        generos = Genero.objects.all()
        mensaje="error, id no existe"
        context={'mensaje':mensaje, 'generos':generos}
        return render(request, 'usuarios/generos_list.html', context)


def generos_edit(request, pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("edit encontró el genero...")
            if request.method == "POST":
                print("edit, es un POST")
                form = GeneroForm(request.POST, instance=genero)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'genero':genero, 'form':form, 'mensaje':mensaje}
                return render(request, 'usuarios/generos_edit.html', context)
            else:
                #no es un POST
                print("edit, NO es un POST")
                form = GeneroForm(instance=genero)
                mensaje=""
                context = {'genero':genero, 'form':form, 'mensaje':mensaje}
                return render(request, 'usuarios/generos_edit.html', context)
    except:
        print("error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'generos':generos}
        return render(request, 'usuarios/generos_edit.html', context)

@login_required   
def menu(request):
    request.session["usuario"]="basti"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, 'usuarios/index.html', context)
