from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Usuarios



# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join("BASE_DIR", "templates")'
)


# views.py


def index(request):
    return render(request, "index.html")

def listar(request):
    users = Usuarios.objects.all()
    datos = {'usuarios': users}
    return render(request, "usuarios_crud/listar.html", datos)

def agregar(request):
    if request.method=='POST':
        if request.POST.get('nombre') and request.POST.get('numero_id')  and request.POST.get('perfil')  and request.POST.get('telefono') and request.POST.get('email')  and request.POST.get('facultad')  and request.POST.get('fecha_prestamo')  and request.POST.get('nro_portatil'):
            user = Usuarios()
            user.nombres_apellidos =request.POST.get('nombre')
            user.id = request.POST.get('numero_id')
            user.Perfil = request.POST.get('perfil')
            user.Telefono = request.POST.get('telefono')
            user.Correo = request.POST.get('telefono')
            user.Facultad = request.POST.get('facultad')
            user.Fecha = request.POST.get('fecha_prestamo')
            user.Nro_portatil = request.POST.get('nro_portatil')
            user.save()
            return redirect('listar')
            
            
            
     
    else:
         return render(request, "usuarios_crud/agregar.html")

        
   
def actualizar(request):
    users = Usuarios.objects.all()
    datos = {'usuarios': users}
    return render(request, "usuarios_crud/actualizar.html", datos)
def eliminar(request):
    return render(request, "usuarios_crud/eliminar.html")