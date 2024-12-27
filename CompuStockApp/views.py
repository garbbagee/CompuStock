from django.shortcuts import render,get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages
# Vista para la página principal
def index(request):
    return render(request, 'html/index.html')

# Vista para la página "Quiénes somos"
def nosotros(request):
    return render(request, 'html/nosotros.html')

# Vista para el login
def login_view(request):
    return render(request, 'html/login.html')

# Vista para el registro de un nuevo usuario
def register_view(request):
    return render(request, 'html/registro.html')

# Vista para la categoría de Hardware
def hardware(request):
    return render(request, 'html/hardware.html')

# Vista para la categoría de Periféricos
def perifericos(request):
    return render(request, 'html/perifericos.html')

# Vista para la categoría de Accesorios
def accesorios(request):
    return render(request, 'html/accesorios.html')

# Vista para las ofertas
def ofertas(request):
    return render(request, 'html/ofertas.html')

# Vista para el soporte
def soporte(request):
    return render(request, 'html/soporte.html')


def inventario(request):
    # Mostrar todos los productos
    productos = Producto.objects.all()

    if request.method == 'POST':
        # Crear producto (C)
        if 'create' in request.POST:
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Producto creado exitosamente.")
                return redirect('inventario')
        
        # Editar producto (U)
        elif 'edit' in request.POST:
            producto_id = request.POST.get('producto_id')
            producto = get_object_or_404(Producto, pk=producto_id)
            form = ProductoForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                messages.success(request, "Producto actualizado exitosamente.")
                return redirect('inventario')

        # Eliminar producto (D)
        elif 'delete' in request.POST:
            producto_id = request.POST.get('producto_id')
            producto = get_object_or_404(Producto, pk=producto_id)
            producto.delete()
            messages.success(request, "Producto eliminado exitosamente.")
            return redirect('inventario')

    else:
        # Formulario vacío para agregar un nuevo producto
        create_form = ProductoForm()

    return render(request, 'html/inventario.html', {
        'productos': productos,
        'create_form': create_form,
    })