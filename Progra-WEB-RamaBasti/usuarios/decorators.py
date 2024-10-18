from django.shortcuts import redirect

def login_request(view_func):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            print("HOLA MUNDO")
            return redirect('index')
    return wrap

def solo_jefe(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.groups.exists():
            grupo_usuario = request.user.groups.all()[0]
        else:
            return redirect('index')

        
        print(grupo_usuario)
    
        if grupo_usuario.__str__() == "adminsitio":
            
            return view_func (request, *args, **kwargs)

        else:
            return redirect('error')
        
    return wrap