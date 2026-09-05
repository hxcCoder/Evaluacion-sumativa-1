from django.shortcuts import render

def catalogo(request):
    autos_disponibles = [
        {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2022},
        {'marca': 'Ford', 'modelo': 'Mustang', 'año': 2023},
        {'marca': 'Chevrolet', 'modelo': 'Spark', 'año': 2021},
    ]
    contexto = {
        'titulo': 'Catálogo de Vehículos',
        'lista_autos': autos_disponibles
    }
    # Se corrige la ruta para apuntar a core/catalogo.html
    return render(request, 'core/catalogo.html', contexto)