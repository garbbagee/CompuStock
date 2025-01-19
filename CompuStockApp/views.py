from django.shortcuts import render,get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegistroForm, LoginForm, ProductoForm

# Vista para la página principal
def index(request):
    return render(request, 'html/index.html')

# Vista para la página "Quiénes somos"
def nosotros(request):
    return render(request, 'html/nosotros.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión exitosamente.")
            return redirect("index")  # Redirige al inicio o donde prefieras
        else:
            messages.error(request, "Credenciales incorrectas. Intenta de nuevo.")
    
    return render(request, "html/login.html")


# Vista para el registro de usuarios
def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Crear el usuario con los datos del formulario
            user = form.save()
            
            # Autenticar e iniciar sesión automáticamente
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                messages.success(request, "Usuario registrado e iniciado sesión exitosamente.")
                return redirect('index')  # Redirige a la página principal después del registro
            else:
                messages.error(request, "Hubo un error al autenticar el usuario.")
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = RegistroForm()
    return render(request, 'html/registro.html', {'form': form})


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
    # Obtener todos los productos
    productos = Producto.objects.all()

    # Formularios
    agregar_form = ProductoForm()
    editar_form = None
    producto_a_editar = None

    # Manejar solicitud POST
    if request.method == 'POST':
        if 'create' in request.POST:
            # Agregar un nuevo producto
            agregar_form = ProductoForm(request.POST, request.FILES)
            if agregar_form.is_valid():
                agregar_form.save()
                messages.success(request, "Producto creado exitosamente.")
                return redirect('inventario')
            else:
                messages.error(request, "Error al crear el producto. Revisa los datos.")

        elif 'edit' in request.POST:
            # Editar producto
            producto_id = request.POST.get('producto_id')  # Tomamos el ID del producto
            if producto_id:
                producto_a_editar = get_object_or_404(Producto, pk=producto_id)

                # Actualizamos solo los campos que hayan sido enviados
                if 'nombre' in request.POST:
                    producto_a_editar.nombre = request.POST['nombre']
                if 'descripcion' in request.POST:
                    producto_a_editar.descripcion = request.POST['descripcion']
                if 'especificaciones' in request.POST:
                    producto_a_editar.especificaciones = request.POST['especificaciones']
                if 'precio' in request.POST:
                    producto_a_editar.precio = request.POST['precio']
                if 'imagen' in request.FILES:
                    producto_a_editar.imagen = request.FILES['imagen']

                producto_a_editar.save()  # Guardar cambios
                messages.success(request, "Producto actualizado exitosamente.")
                return redirect('inventario')

        elif 'delete' in request.POST:
            # Eliminar producto
            producto_id = request.POST.get('producto_eliminar')
            if producto_id:
                producto_a_eliminar = get_object_or_404(Producto, pk=producto_id)
                producto_a_eliminar.delete()
                messages.success(request, "Producto eliminado exitosamente.")
                return redirect('inventario')

    # Manejar búsqueda
    query = request.GET.get('search', '')
    if query:
        productos = productos.filter(nombre__icontains=query)

    # Manejar la selección de un producto para editar
    producto_id = request.GET.get('producto_id', None)
    if producto_id:
        producto_a_editar = get_object_or_404(Producto, pk=producto_id)
        editar_form = ProductoForm(instance=producto_a_editar)

    context = {
        'productos': productos,
        'agregar_form': agregar_form,
        'editar_form': editar_form,
        'producto_a_editar': producto_a_editar,
    }
    return render(request, 'html/inventario.html', context)