# Mi Proyecto Automotriz - Evaluación Sumativa 1

## Propósito y Proyección
Este proyecto es un catálogo interactivo desarrollado en Django para un taller automotriz. Su propósito principal es organizar y mostrar los vehículos disponibles, además de los precios de los distintos servicios. Para futuras evaluaciones, planeo implementar un sistema de reservas de horas, autenticación de usuarios (mecánicos/clientes) y un panel administrativo.

## Integrante
* Benjamin Millalonco

## Requisitos e Instalación
1. Clonar el repositorio: `git clone https://github.com/hxcCoder/Evaluacion-sumativa-1.git`
2. Entrar a la carpeta: `cd evaluacion-sumativa-1`
3. Crear entorno virtual: `python -m venv .venv`
4. Activar entorno virtual: 
   * Windows: `.venv\Scripts\activate`
   * Mac/Linux: `source .venv/bin/activate`
5. Instalar dependencias: `pip install -r requirements.txt`
6. Ejecutar servidor: `python manage.py runserver`

## Estructura y Rutas del Proyecto
El proyecto está dividido en 3 aplicaciones principales:
* **core**: Contiene las rutas generales (`/inicio/`, `/contacto/`, `/servicios/`, `/perfil/<nombre_usuario>/`).
* **Autos**: Contiene la ruta del inventario (`/autos/catalogo/`).
* **Precios**: Contiene la ruta de valores (`/precios/lista/`).

## Desarrollo del Trabajo
Al ser un proyecto individual, me encargué de realizar todas las etapas: configuración inicial del entorno, creación de las vistas y templates base en `core`, y la lógica de programación (uso de diccionarios, condicionales y bucles) para las aplicaciones `Autos` y `Precios`.

## Dificultades y Soluciones
* **Dificultad**: Al principio tuve problemas para organizar las rutas, ya que las vistas de la aplicación `Precios` y `Autos` se mezclaban o chocaban con las rutas principales de `core`.
* **Solución**: Aprendí a utilizar la función `include()` en el archivo principal `config/urls.py`. Esto me permitió delegar y separar las URLs, dándole a cada aplicación su propio archivo `urls.py` de forma más ordenada.

## Registro de uso de IA
* **Problema inicial**: No tenía del todo claro cómo pasar una lista de diccionarios (los datos de los autos) desde el archivo `views.py` hacia el archivo HTML para mostrarlos en pantalla.
* **Consulta**: Le pedí a la IA que me explicara cómo enviar esta lista de autos al template y cómo recorrerla usando un bucle en Django.
* **Solución aplicada**: La IA me explicó que debía agrupar los datos en un diccionario llamado `contexto` al momento de hacer el `render`, y luego me mostró cómo usar la etiqueta `{% for auto in lista_autos %}` en el HTML. Lo apliqué en `Autos/views.py` y el catálogo renderizó correctamente.

## Conclusiones y Reflexión
Con esta primera evaluación logré comprender en la práctica el flujo de trabajo de Django (URL -> Vista -> Template). El uso de IA fue una buena herramienta de apoyo para destrabar errores de sintaxis y recordar etiquetas específicas, pero de todas formas tuve que entender la lógica por mi cuenta para poder estructurar bien los archivos base (como el uso de `{% extends %}` y `{% block contenido %}`). Considero que el proyecto cumple con los requisitos base y queda con una buena estructura para seguir escalándolo en las próximas entregas.