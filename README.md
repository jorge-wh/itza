# Django Base


## Estructura del directorio del proyecto

```text
.
├── django_base
|   |
|   |    # Directorio de las aplicaciones del proyecto de Django.
│   ├── apps/
|   |   
│   ├── core
│   │   ├── asgi.py
│   │   ├── wsgi.py
│   │   |    # Archivo de urls principal del proyecto
│   │   └── urls.py
|   |
│   ├── media/
|   | 
|   |   # Archivos staticos del proyecto
│   ├── static/
|   |
|   |   # Archivo settings del proyecto
│   └── settings.py
|
|   # Directorio para documentación del proyecto
├── docs/
|
|   # Este directorio contiene los archivos estaticos autogenerados al ejecutar el comando `collectstatic`.
├── static/
|
|   # Directorio para las traducciones
├── locale/
|
├── media/
|   
├── manage.py
|
├── Pipfile
└── Pipfile.lock
```
