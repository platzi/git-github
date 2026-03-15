# CLAUDE.md — Memoria del Proyecto PrimerRepo

> Este archivo es la fuente de verdad para Claude Code en este proyecto.
> Contiene el contexto del proyecto, la arquitectura, y guías de desarrollo.

---

## Contexto del desarrollador

- Es el **primer proyecto** del usuario con Git/GitHub y desarrollo de software.
- El proyecto proviene del curso de **Git y GitHub de Platzi** (instructor: Amin Espinoza).
- El objetivo de aprendizaje es entender: control de versiones, APIs REST, paquetes Python, y HTML/CSS.
- Priorizar explicaciones claras y didácticas cuando se hagan cambios o se responda preguntas.

---

## ¿Qué es este repositorio?

Un **monorepo educativo** con 3 sub-proyectos independientes que demuestran conceptos distintos de desarrollo:

| Sub-proyecto | Carpeta | Concepto que enseña |
|---|---|---|
| API REST | `API_Python/` | Cómo construir un backend con Python |
| Paquete pip | `Paquete/` | Cómo empaquetar y distribuir código Python |
| Frontend estático | `plantilla_web/` | Cómo construir una página web con HTML/CSS |

Los 3 proyectos son **independientes entre sí** — no se llaman ni comparten código actualmente.

---

## Estructura del repositorio

```
git-github/                         ← Raíz del repositorio Git
└── PrimerRepo/                     ← Directorio de trabajo principal
    │
    ├── CLAUDE.md                   ← Este archivo (memoria del proyecto)
    │
    ├── API_Python/                 ← Sub-proyecto 1: Backend REST API
    │   ├── app.py                  ← Único archivo de la API (FastAPI)
    │   └── requirements.txt        ← Dependencias: fastapi, uvicorn, pydantic
    │
    ├── Paquete/                    ← Sub-proyecto 2: Paquete Python
    │   ├── setup.py                ← Configuración del paquete (nombre, versión, autor)
    │   ├── mi_paquete/
    │   │   └── __init__.py         ← Código del paquete: función saludar(nombre)
    │   ├── dist/                   ← Artefactos listos para distribuir (.whl, .tar.gz)
    │   └── build/                  ← Archivos de compilación (generados automáticamente)
    │
    ├── plantilla_web/              ← Sub-proyecto 3: Frontend estático
    │   ├── index.html              ← Página principal (landing page tipo "link tree")
    │   └── assets/
    │       └── style.css           ← Estilos: animación de gradiente, efecto shake
    │
    ├── .github/                    ← Configuración de GitHub
    │   ├── ISSUE_TEMPLATE/
    │   │   └── bug_report.md       ← Plantilla para reportar bugs
    │   └── pull_request_template.md ← Plantilla para Pull Requests
    │
    ├── README.md                   ← Descripción general del proyecto
    ├── CONTRIBUTING.md             ← Guía para contribuir (en español)
    ├── Contribuciones.md           ← Tabla de contribuidores
    └── LICENSE                     ← Licencia del proyecto
```

---

## Sub-proyecto 1: API_Python — REST API con FastAPI

### ¿Qué es?
Una **API REST** es un servidor que responde peticiones HTTP devolviendo datos (generalmente JSON).
FastAPI es el framework de Python moderno más popular para construirlas.

### Tecnologías
- **FastAPI** — Framework web asíncrono de Python. Genera documentación automática.
- **Uvicorn** — Servidor ASGI que ejecuta la aplicación FastAPI.
- **Pydantic** — Librería de validación de datos (FastAPI la usa internamente).

### Cómo funciona `app.py`
```python
from fastapi import FastAPI

app = FastAPI()          # Crea la aplicación

@app.get("/familia")     # Define una ruta GET en /familia
def get_familia():
    return ["Amin", "Marce", "Miranda"]   # Devuelve JSON automáticamente
```
Cada función decorada con `@app.get(...)` es un **endpoint** — una URL a la que se puede hacer una petición HTTP GET y que devuelve datos.

### Endpoints disponibles
| URL | Datos que devuelve |
|---|---|
| `GET /familia` | Lista de nombres de familia |
| `GET /superheroesDC` | Superhéroes DC (Superman, Batman, etc.) |
| `GET /superheroesMarvel` | Superhéroes Marvel (Spider-Man, Iron Man, etc.) |
| `GET /LOTRWarriors` | Personajes de El Señor de los Anillos |
| `GET /starwarsWarriors` | Personajes de Star Wars |
| `GET /warriorsGOT` | Personajes de Game of Thrones |

### Cómo correrlo
```bash
cd API_Python
pip install -r requirements.txt
uvicorn app:app --reload
```
- La API queda disponible en: `http://localhost:8000`
- Documentación interactiva (Swagger): `http://localhost:8000/docs`
- El flag `--reload` hace que el servidor se reinicie automáticamente al guardar cambios.

### Estado actual del código
- Sin base de datos — todos los datos están escritos directamente en el código (hardcoded).
- Sin autenticación — cualquiera puede acceder a todos los endpoints.
- Sin validación de entrada — todos los endpoints son solo GET sin parámetros.

---

## Sub-proyecto 2: Paquete — Paquete Python distribuible

### ¿Qué es?
Un **paquete pip** es código Python empaquetado para que otros puedan instalarlo con `pip install nombre`.
Es la misma forma en que se instalan FastAPI, NumPy, Pandas, etc.

### Tecnologías
- **setuptools** — Herramienta estándar de Python para crear paquetes.
- **wheel** — Formato de distribución binaria (`.whl`), más rápido de instalar que el código fuente.

### Cómo funciona
**`setup.py`** — Define los metadatos del paquete:
```python
setup(
    name="paquetePlatzi",      # Nombre con el que se instalaría: pip install paquetePlatzi
    version="0.1.0",           # Versión semántica: mayor.menor.parche
    packages=find_packages(),  # Detecta automáticamente las carpetas con código
    author="Amin Espinoza",
)
```

**`mi_paquete/__init__.py`** — El código real del paquete:
```python
def saludar(nombre):
    return "Hola " + nombre + ", este es mi primer paquete pip!"
```

### Cómo usarlo una vez instalado
```python
from mi_paquete import saludar

resultado = saludar("María")
print(resultado)  # → "Hola María, este es mi primer paquete pip!"
```

### Cómo construirlo (generar los archivos de distribución)
```bash
cd Paquete
pip install setuptools wheel
python setup.py sdist bdist_wheel
```
Esto genera en `dist/`:
- `paquetePlatzi-0.1.0.tar.gz` — Código fuente comprimido
- `paquetePlatzi-0.1.0-py3-none-any.whl` — Wheel listo para instalar

### Cómo instalarlo localmente (para probar)
```bash
pip install dist/paquetePlatzi-0.1.0-py3-none-any.whl
```

---

## Sub-proyecto 3: plantilla_web — Frontend estático

### ¿Qué es?
Una **página web estática** (HTML + CSS) que funciona como "link tree" — una página personal con botones que redirigen a distintas redes sociales y recursos.

### Tecnologías
- **HTML5** — Estructura y contenido de la página.
- **CSS3** — Estilos visuales, incluyendo animaciones.
- **Bootstrap 4.1.3** — Framework CSS para diseño responsivo (cargado desde CDN, no instalado localmente).
- **jQuery 3.3.1** — Librería JavaScript (requerida por Bootstrap).

### Cómo funciona `index.html`
La página tiene dos secciones principales:
1. **Header**: Avatar circular (foto cargada desde GitHub) + título del curso.
2. **Botones**: Cada botón usa `onclick="location.href='URL'"` para redirigir al hacer clic.

### Cómo funciona `style.css`
Dos efectos visuales principales:
1. **Gradiente animado** en el fondo (`@keyframes Gradient`):
   - Cicla entre 4 colores: naranja → rosa → azul → turquesa
   - Se repite infinitamente cada 15 segundos.
2. **Efecto shake** en el primer botón (`@keyframes shake-animation`):
   - El botón "Mi curso de Docker" vibra suavemente cada ~5 segundos.

### Cómo verlo en el navegador
```bash
cd plantilla_web
python -m http.server 8080
```
Luego abrir: `http://localhost:8080`

> No se puede abrir directamente haciendo doble clic en `index.html` porque algunos recursos
> pueden no cargar correctamente sin servidor HTTP.

---

## Relación entre los 3 sub-proyectos

```
┌──────────────────────────────────────────────────────────────┐
│                        PrimerRepo                            │
│                                                              │
│  ┌─────────────────┐  ┌──────────────────┐  ┌────────────┐  │
│  │  plantilla_web  │  │   API_Python      │  │  Paquete   │  │
│  │                 │  │                  │  │            │  │
│  │  HTML + CSS     │  │  FastAPI REST     │  │  pip pkg   │  │
│  │  Bootstrap      │  │  6 endpoints GET  │  │  saludar() │  │
│  │                 │  │                  │  │            │  │
│  │  Sin backend    │  │  Sin base datos   │  │  Sin deps  │  │
│  └─────────────────┘  └──────────────────┘  └────────────┘  │
│                                                              │
│  Los 3 son INDEPENDIENTES — no se comunican entre sí (aún)  │
└──────────────────────────────────────────────────────────────┘
```

**Integración potencial (no implementada):**
- `plantilla_web` podría hacer `fetch()` a los endpoints de `API_Python` para mostrar datos dinámicos.
- `API_Python` podría importar funciones de `Paquete` si el paquete creciera.

---

## Flujo de trabajo con Git/GitHub

Este repositorio sigue el flujo estándar de contribución open source:

```
1. Fork del repositorio en GitHub
        ↓
2. Clonar el fork localmente
   git clone https://github.com/TU_USUARIO/git-github.git
        ↓
3. Agregar el repositorio original como "upstream"
   git remote add upstream https://github.com/platzi/git-github.git
        ↓
4. Crear una rama para el cambio
   git checkout -b nombre-descriptivo-del-cambio
        ↓
5. Hacer cambios, commit y push
   git add archivo_modificado.py
   git commit -m "descripción clara del cambio"
   git push origin nombre-descriptivo-del-cambio
        ↓
6. Abrir Pull Request en GitHub hacia la rama main
```

### Convenciones de commits
El proyecto no tiene convención fija documentada. Se recomienda usar:
```
tipo: descripción breve en imperativo

Ejemplos:
  add: endpoint GET /peliculas en API_Python
  fix: error de codificación en index.html
  update: nueva versión del paquete a 0.2.0
  docs: actualizar README con instrucciones de instalación
```

### Rama principal
- La rama de integración es **`main`**.
- No hay rama `develop` ni estructura de ramas adicional definida.

---

## Configuración de GitHub

### Plantilla de Issues (`bug_report.md`)
Cuando alguien reporta un bug en GitHub, se usa esta plantilla con secciones para:
- Descripción del bug
- Pasos para reproducirlo
- Comportamiento esperado vs. actual
- Screenshots y logs
- Información del entorno (OS, versión de Python, etc.)

### Plantilla de Pull Requests (`pull_request_template.md`)
Cada PR debe incluir:
- ¿Qué cambia este PR?
- ¿Por qué se hace este cambio?
- ¿Cómo probarlo?
- Checklist de contribuidor (estilo de código, tests, documentación)

---

## Decisiones técnicas y limitaciones actuales

| Área | Estado actual | Posible mejora futura |
|---|---|---|
| Base de datos | Sin DB — datos hardcoded en el código | Agregar SQLite o PostgreSQL |
| Autenticación | Sin auth — endpoints abiertos | Agregar API keys o JWT |
| Tests | Sin tests automatizados | Agregar pytest para la API |
| Docker | Sin contenedores | Agregar Dockerfile por sub-proyecto |
| CI/CD | Sin pipelines | Agregar GitHub Actions |
| Conexión frontend-backend | No implementada | Usar fetch() en JS para consumir la API |
| Datos de la API | Todos en español/inglés mezclados | Estandarizar idioma |

---

## Comandos de referencia rápida

```bash
# --- API_Python ---
cd API_Python
pip install -r requirements.txt          # Instalar dependencias
uvicorn app:app --reload                 # Correr servidor de desarrollo
# Acceder en: http://localhost:8000
# Docs en:    http://localhost:8000/docs

# --- Paquete ---
cd Paquete
python setup.py sdist bdist_wheel        # Construir el paquete
pip install -e .                         # Instalar en modo editable (para desarrollo)

# --- plantilla_web ---
cd plantilla_web
python -m http.server 8080               # Servidor HTTP simple
# Acceder en: http://localhost:8080

# --- Git ---
git status                               # Ver estado de cambios
git log --oneline                        # Ver historial de commits
git diff                                 # Ver cambios no guardados
```

---

## Notas para Claude

- **El usuario es principiante** — explicar conceptos básicos cuando sea relevante.
- **Priorizar claridad sobre optimización** — el código didáctico es más valioso que el código perfecto.
- **No reestructurar sin pedir** — la estructura actual es intencional para el curso.
- **Idioma del proyecto**: español para docs y comentarios, inglés para código (convención estándar).
- Las carpetas `@backend/`, `@Frontend/`, `@Mobile/` mencionadas por el usuario son referencias conceptuales — no existen como directorios reales en el repo.
