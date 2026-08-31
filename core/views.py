from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return HttpResponse("Hola mundo desde Django")

def contacto(request):
    return HttpResponse('Pagina de contacto')

def servicios(request):
    return HttpResponse('Servicios')

def perfiles(request, nombre_usuario):
    return HttpResponse(f'Perfil de {nombre_usuario}')