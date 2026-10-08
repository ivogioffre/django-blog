# Sitio web personal con blog en base a la estructura de Django
Este proyecto es mi portfolio personal, desarrollado para presentar mis conocimientos, proyectos y trabajos realizados durante mi formacion como Tecnico en Computación.
El sitio reune informacion sobre mi, mis habilidades y diferentes proyectos en los que trabajé utilizando tecnologías como Python, HTML, CSS y Django. Además, cuenta con un blog integrado en Django donde puedo publicar proyectos, experiencias y contenidos relacionados con mi aprendizaje, futbol, cine y mucho más.


# Funcionalidades del blog
- Listado de entradas en orden cronológico (las más recientes primero).
- Cada entrada tiene título, resumen opcional(si no se completa se utilizan las primeras 30 palabras del texto), texto, imagen y una o más categorias.
- Filtro por categoria.
- Cualquier visitante puede dejar un comentario sin registrarse.
- Solo el administrador crea entradas y elimina comentarios desde el /admin.

# Instalación y ejecución

* Instalar las dependencias:
pip install -r requirements.txt

* Iniciar el servidor:
python manage.py runserver

* Abrir en el navegador:
- Portfolio: http://127.0.0.1:8000/
- Blog: http://127.0.0.1:8000/blog/
- Panel de administración: http://127.0.0.1:8000/admin/

Para publicar contenido, entrar a /admin, crear las categorias y después las entradas (Posts). Los comentarios aparecen en Comments, donde se pueden eliminar.

# Estructura del proyecto

```
django-blog/
├── manage.py
├── requirements.txt
├── personal_blog/              # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── portfolio/                  # App del portfolio
│   ├── static/portfolio/css/
│   │   └── portfolio.css
│   ├── templates/portfolio/
│   │   └── portfolio.html
│   ├── views.py
│   └── urls.py
├── blog/                       # App del blog
│   ├── static/blog/css/
│   │   └── blog.css
│   ├── templates/blog/
│   │   ├── index.html
│   │   ├── detail.html
│   │   └── category.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── templates/
│   └── base.html               # Plantilla base compartida
├── static/
│   ├── css/base.css            # Estilos compartidos
│   ├── js/script.js
│   └── assets/                 # CV, imágenes, favicon
└── media/                      # Imágenes subidas desde el admin 
```

## Que hace cada archivo importante

# personal_blog

- settings.py: Configuración del proyecto, incluyendo apps instaladas, base de datos, rutas de archivos estáticos y media, entre otros.
- urls.py: Define las rutas principales del proyecto, incluyendo las rutas para el portfolio y el blog.

# blog

- models.py: Define los modelos de datos para las entradas del blog, categorías, descripciones y comentarios.
- views.py: Contiene las funciones que manejan las solicitudes HTTP y devuelven respuestas, como la lista de entradas, detalle de una entrada y filtrado por categoria.
- urls.py: Define las rutas específicas para la app del blog, incluyendo la lista de entradas, detalle de una entrada y filtrado por categoria.
- forms.py: Define los formularios para la creacion de comentarios en las entradas del blog.
- admin.py:	Registra los modelos en el panel de administración, con listados, filtros y buscadores. Desde acá el administrador crea entradas y elimina comentarios.

* HTML
- index: Página principal del blog: grilla de tarjetas con las entradas.
- detail: Vista de una entrada completa, lista de comentarios y formulario para comentar.
- category: Entradas filtradas por categoría.

* CSS
- blog.css: Estilos específicos para la app del blog (tarjetas, entrada individual, comentarios) etc.

# portfolio
- views.py: Contiene la función que maneja la solicitud HTTP para la página del portfolio y devuelve la respuesta con el template correspondiente.
- urls.py: Define la ruta específica para la app del portfolio, que apunta a la vista

* HTML
- portfolio.html: Página principal del portfolio, con información personal, habilidades, proyectos realizados e info de contacto.

* CSS
- portfolio.css: Estilos específicos para la app del portfolio (portada, habilidades, proyectos, contacto).

# archivos compartidos
- templates/base.html: Plantilla base compartida por todas las páginas del proyecto, que incluye la estructura HTML común, como encabezado, pie de página y enlaces a archivos CSS y JS.
- static/js/script.js:JavaScript general del sitio.
- static/assets: Recursos del portfolio: CV, imágenes y favicon.
## Autor

