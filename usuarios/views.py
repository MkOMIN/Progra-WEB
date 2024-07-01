from django.shortcuts import render, redirect
from . models import Usuarios,Genero
from django.http import HttpResponseRedirect
from . forms import GeneroForm, UsuariosForm
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

def carrito(request):
    context={}
    return render(request, 'usuarios/carrito.html', context)

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

    print("Estoy en controlador usuariosAdd...")
    generos=Genero.objects.all()
    usuariosForm=UsuariosForm()
    context={'generos':generos, 'usuariosForm':usuariosForm, 'boton':"Agregar"}

    if request.method == "POST":
        print(1)
        usuariosForm=UsuariosForm(request.POST)
        for field in usuariosForm:
            print(field.errors)
        if usuariosForm.is_valid():
            print(2)
            usuariosForm.save()
            print("exito")
        

    return render(request, 'usuarios/usuarios_add.html', context)

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
        usuariosForm=UsuariosForm(instance=usuarios)

        print(type(usuarios.id_genero.genero))

        context={'usuarios':usuarios,'generos':generos, 'usuariosForm':usuariosForm, 'boton':"Actualizar"}


        if request.method == "POST":
            print(1)
            usuariosForm=UsuariosForm(request.POST, instance=usuarios)
            for field in usuariosForm:
                print(field.errors)
            if usuariosForm.is_valid():
                print(2)
                usuariosForm.save()
                print("exito")    

    return render(request, 'usuarios/usuarios_add.html',context)

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
    
def crud_generos(request):
    generos=Genero.objects.all()
    context={'generos':generos}
    print("enviando datos generos_list")
    return render(request, 'usuarios/generos_list.html',context)

def generosAdd(request):
    print("Estoy en controlador generosAdd...")
    context={}

    if request.method == "POST":
        print("Controlador es un post...")
        form=GeneroForm(request.POST)
        if form.is_valid:
            print("Estoy en agregar, is_valid")
            form.save()

            #limpiar formulario
            form=GeneroForm()

            context={'mensaje': "Ok, datos grabados...", "form":form}
            return render(request, 'usuarios/generos_add.html', context)
        
    else:
        form=GeneroForm()
        context={'form':form}
        return render(request, 'usuarios/generos_add.html', context)

def generos_del(request,pk):
    mensajes=[]
    errores=[]
    generos = Genero.objects.all()
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            genero.delete()
            mensajes.append("Bien, datos eliminados...")
            context={'generos':generos, 'mensajes':mensajes, 'errores':errores}
            return render(request, 'usuarios/generos_list.html', context)
    except:
        print("Error, id no existe...")
        generos = Genero.objects.all()
        mensaje="Error, id no existe..."
        context={'mensaje':mensaje, 'generos':generos}
        return render(request, 'usuarios/generos_list.html', context)

def generos_edit(request, pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("Edit encontró el género...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = GeneroForm(request.POST, instance=genero)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'genero':genero, 'form':form , 'mensaje':mensaje}
                return render(request, 'usuarios/generos_edit.html', context)
            else:
                #no es POST
                print("Edit, NO es POST")
                form = GeneroForm(instance=genero)
                mensaje=""
                context = {'genero':genero, 'form':form , 'mensaje':mensaje}
                return render(request, 'usuarios/generos_edit.html', context)
    except:
        print("Error, id no existe...")
        generos = Genero.objects.all()
        mensaje="Error, id no existe..."
        context={'mensaje':mensaje, 'generos':generos}
        return render(request, 'usuarios/generos_list.html', context)