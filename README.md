# Biblioteca Bolero

Proyecto con un CRUD de lieratura hispanoamericana.

## Inicio Rápido

¿Quieres probarlo inmediatamente? Sigue estos pasos:

```bash
git clone <url-del-repositorio>
cd crud_python
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install django
python manage.py migrate
python manage.py runserver
```

Luego visita:
- **📋 Lista de libros**: http://127.0.0.1:8000/libros/
- **🔧 Panel Admin**: http://127.0.0.1:8000/admin/ (admin/admin123)

## 🚀 Característicastema de Gestión de Libros - CRUD con Django

Un sistema completo de gestión de libros desarrollado con Django que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una colección de libros.

## Características

- ✅ **Lista de libros**: Visualiza todos los libros registrados
- ✅ **Agregar libros**: Formulario para registrar nuevos libros
- ✅ **Ver detalles**: Información completa de cada libro
- ✅ **Editar libros**: Modificar información existente
- ✅ **Eliminar libros**: Remover libros con confirmación
- ✅ **Panel de administración**: Interfaz de Django Admin
- ✅ **Interfaz responsive**: Templates HTML limpios y funcionales

## 📋 Modelo de Datos

### Libro
- **Título**: Nombre del libro (máx. 200 caracteres)
- **Autor**: Nombre del autor (máx. 100 caracteres)
- **Descripción**: Descripción detallada del libro
- **Fecha de publicación**: Fecha de publicación
- **ISBN**: Código ISBN único (13 caracteres)

## 🛠️ Tecnologías Utilizadas

- **Backend**: Django 6.0.1
- **Base de datos**: SQLite (por defecto)
- **Frontend**: HTML5, CSS básico
- **Python**: 3.14

## 📁 Estructura del Proyecto

```
crud_python/
│
├── manage.py                    # Archivo principal de Django
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este archivo
│
├── sistema_libros/              # Aplicación principal
│   ├── __init__.py
│   ├── settings.py              # Configuración del proyecto
│   ├── urls.py                  # URLs principales
│   ├── app_urls.py              # URLs de la aplicación
│   ├── models.py                # Modelo Libro
│   ├── views.py                 # Vistas del CRUD
│   ├── forms.py                 # Formularios
│   ├── admin.py                 # Configuración del admin
│   ├── wsgi.py                  # Configuración WSGI
│   └── migrations/              # Migraciones de BD
│
├── categorias/                  # Aplicación categorías (preparada)
├── libreria/                    # Aplicación librería (preparada)
│
└── templates/                   # Templates HTML
    └── libros/
        ├── lista_libros.html    # Lista de libros
        ├── detalle_libro.html   # Detalles del libro
        ├── crear_libro.html     # Formulario crear
        ├── editar_libro.html    # Formulario editar
        └── eliminar_libro.html  # Confirmación eliminar
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd crud_python
```

### 2. Crear entorno virtual
```bash
python -m venv .venv
```

### 3. Activar entorno virtual

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

*O alternativamente:*
```bash
pip install django
```

### 5. Realizar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```
*Nota: Ya existe un superusuario de prueba (admin/admin123). Solo necesitas crear uno nuevo si quieres credenciales diferentes.*

### 7. Ejecutar servidor de desarrollo
```bash
python manage.py runserver
```

El servidor estará disponible en: `http://127.0.0.1:8000/`

## 🔐 Credenciales de Prueba

Para facilitar las pruebas, el proyecto incluye un usuario administrador preconfigurado:

- **URL de administración**: `http://127.0.0.1:8000/admin/`
- **Usuario**: `admin`
- **Contraseña**: `admin123`
- **Email**: `admin@test.com`

### 📚 Datos de Prueba

El proyecto incluye dos libros de ejemplo para facilitar las pruebas:

1. **Don Quijote de la Mancha** - Miguel de Cervantes (1605)
2. **Cien años de soledad** - Gabriel García Márquez (1967)

Puedes ver estos libros en: `http://127.0.0.1:8000/libros/`

> ⚠️ **Importante**: Estas son credenciales de desarrollo. En producción, cambia estas credenciales por unas seguras.

## 🌐 URLs Disponibles

### Frontend
- **Lista de libros**: `http://127.0.0.1:8000/libros/`
- **Crear libro**: `http://127.0.0.1:8000/libros/crear/`
- **Detalle libro**: `http://127.0.0.1:8000/libros/<id>/`
- **Editar libro**: `http://127.0.0.1:8000/libros/<id>/editar/`
- **Eliminar libro**: `http://127.0.0.1:8000/libros/<id>/eliminar/`

### Administración
- **Panel Admin**: `http://127.0.0.1:8000/admin/`

## 💡 Uso del Sistema

### 1. Agregar un nuevo libro
1. Ve a `http://127.0.0.1:8000/libros/crear/`
2. Completa el formulario con la información del libro
3. Haz clic en "Guardar Libro"

### 2. Ver lista de libros
- Ve a `http://127.0.0.1:8000/libros/` para ver todos los libros

### 3. Ver detalles de un libro
- Haz clic en cualquier libro de la lista para ver sus detalles completos

### 4. Editar un libro
- En la página de detalles, haz clic en "Editar"
- Modifica los campos necesarios y guarda

### 5. Eliminar un libro
- En la página de detalles, haz clic en "Eliminar"
- Confirma la eliminación

## 🔧 Desarrollo

### Estructura de archivos importantes

**Modelos** (`sistema_libros/models.py`):
```python
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
```

**URLs** (`sistema_libros/app_urls.py`):
- Lista: `''` → `lista_libros`
- Detalle: `'<int:libro_id>/'` → `detalle_libro`
- Crear: `'crear/'` → `crear_libro`
- Editar: `'<int:libro_id>/editar/'` → `editar_libro`
- Eliminar: `'<int:libro_id>/eliminar/'` → `eliminar_libro`

### Aplicaciones preparadas para expansión

El proyecto incluye dos aplicaciones adicionales listas para desarrollo:
- **`categorias/`**: Para gestionar categorías de libros
- **`libreria/`**: Para gestionar información de librerías

## 📝 Próximas mejoras

- [ ] Implementar categorías de libros
- [ ] Agregar sistema de búsqueda
- [ ] Implementar paginación
- [ ] Agregar imágenes de portada
- [ ] Implementar sistema de usuarios
- [ ] API REST con Django REST Framework
- [ ] Mejoras en el diseño UI/UX

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

**Desarrollado con ❤️ usando Django**