from django.shortcuts import render

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
