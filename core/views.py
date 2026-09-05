from django.shortcuts import render

def inicio(request):
    return render(request, 'core/inicio.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def perfiles(request, nombre_usuario):
    contexto = {'nombre': nombre_usuario}
    return render(request, 'core/perfil.html', contexto)