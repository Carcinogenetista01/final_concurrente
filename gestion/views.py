from django.shortcuts import render
from .models import Supercomputadora
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


def listar_supercomputadoras(request):
    supercomputadoras = Supercomputadora.objects.all()  # Obtener todas las supercomputadoras
    return render(request, 'gestion/listar_supercomputadoras.html', {'supercomputadoras': supercomputadoras})
def crear_supercomputadora(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        pais = request.POST['pais']
        numero_cores = request.POST['numero_cores']
        ram_tb = request.POST['ram_tb']
        almacenamiento_tb = request.POST['almacenamiento_tb']
        teraflops = request.POST['teraflops']
        sistema_operativo = request.POST['sistema_operativo']

        Supercomputadora.objects.create(
            nombre=nombre,
            pais=pais,
            numero_cores=numero_cores,
            ram_tb=ram_tb,
            almacenamiento_tb=almacenamiento_tb,
            teraflops=teraflops,
            sistema_operativo=sistema_operativo
        )
        return redirect('listar_supercomputadoras')  # Redirige a la lista

    return render(request, 'gestion/crear_supercomputadoras.html')

def editar_supercomputadora(request, id):
    supercomputadora = get_object_or_404(Supercomputadora, id=id)  # Busca el registro o devuelve 404

    if request.method == 'POST':  # Si es un formulario enviado
        supercomputadora.nombre = request.POST.get('nombre')
        supercomputadora.pais = request.POST.get('pais')
        supercomputadora.numero_cores = request.POST.get('numero_cores')
        supercomputadora.ram_tb = request.POST.get('ram_tb')
        supercomputadora.almacenamiento_tb = request.POST.get('almacenamiento_tb')
        supercomputadora.teraflops = request.POST.get('teraflops')
        supercomputadora.sistema_operativo = request.POST.get('sistema_operativo')
        supercomputadora.save()  # Guarda los cambios en la base de datos
        return redirect('listar_supercomputadoras')  # Redirige a la lista

    return render(request, 'gestion/editar_supercomputadora.html', {'supercomputadora': supercomputadora})


def eliminar_supercomputadora(request, id):
    supercomputadora = get_object_or_404(Supercomputadora, id=id)

    if request.method == 'POST':  # Si se confirma la eliminación
        supercomputadora.delete()  # Elimina el registro
        return redirect('listar_supercomputadoras')  # Redirige a la lista

    return render(request, 'gestion/eliminar_supercomputadora.html', {'supercomputadora': supercomputadora})


def listar_supercomputadoras(request):
    supercomputadoras = Supercomputadora.objects.all()
    nombres = [sc.nombre for sc in supercomputadoras]
    velocidades = [sc.teraflops for sc in supercomputadoras]
    return render(request, 'gestion/listar_supercomputadoras.html', {
        'supercomputadoras': supercomputadoras,
        'nombres': nombres,
        'velocidades': velocidades
    })

