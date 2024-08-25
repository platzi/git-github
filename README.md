# Contenido de este repositorio

Este repo cuenta con tres proyectos que usarás para tu curso de Git y Github.

Los proyectos son los siguientes:

## Plantilla web para presentación

Una muy colorida plantilla HTML básica para lograr una muy buena presentación y llevar a tu audiencia a todos tus canalaes sociales.

Puedes verla [aquí](/miSitio/).

## API de Python básica

Una API básica con solo tres métodos de prueba. ¡Lo que importa es aprender de Github ahora!

Si quieres probarla en modo local solo necesitas escribir los comandos:

```bash
pip install -r requirements.txt
```

Y luego podrás ejecutar la aplicación usando [uvicorn](https://www.uvicorn.org/).

```bash
uvicorn app:app --reload
```

Puedes verla [aquí](/API_Python/).

## Paquete de PIP

Un paquete muy simple de PIP que servirá para crear un artefacto. ¿Te imaginas publicando tu primer paquete PIP?

Todos los archivos preconstruidos están ya cargados en este repo, sin embargo los únicos dos que necesitas son **setup.py** y el contenido de la carpeta **mi_paquete**, todo lo demás lo puedes borrar.

Modifica **setup.py** con tu propia información.

```python
from setuptools import setup, find_packages

setup(
    name="paquetePlatzi",                           # Nombre del paquete
    version="0.1.0",                                # Versión inicial
    packages=find_packages(),                       # Paquetes a incluir
    description="Un paquete pip simple de saludo",  # Breve descripción
    author="Amin Espinoza",                         # Tu nombre
    author_email="amin@platzi.com",                 # Tu correo electrónico
    url="https://github.com/platzi/git-github",     # URL del proyecto
)
```

Después de eso si es necesario, instala las herramientas adecuadas para empaquetar el proyecto.

```bash
pip install setuptools wheel
```

Empaqueta tu proyecto.

```bash
python setup.py sdist bdist_wheel
```

Aquí es donde están todos los archivos de esta carpeta y donde la clase comenzará.

Puedes verla [aquí](/Paquete/).
