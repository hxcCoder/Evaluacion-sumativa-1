from django.shortcuts import render

def catalogo(request):
    # Creamos una lista simulando una base de datos
    autos_disponibles = [
        {'marca': 'Toyota', 'modelo': 'Corolla', 'año': 2022},
        {'marca': 'Ford', 'modelo': 'Mustang', 'año': 2023},
        {'marca': 'Chevrolet', 'modelo': 'Spark', 'año': 2021},
    ]
    
    # Preparamos el contexto para enviarlo al template HTML
    contexto = {
        'titulo': 'Catálogo de Vehículos',
        'lista_autos': autos_disponibles
    }
    
    # Retornamos el render hacia un archivo HTML (que crearemos en el Paso 4)
    return render(request, 'Autos/catalogo.html', contexto)
