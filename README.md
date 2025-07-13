# Sistema de Gestión de Biblioteca

## Descripción
Este proyecto es un sistema de gestión de biblioteca desarrollado con Django y SQLite. Permite administrar categorías, autores, libros y préstamos, con validaciones para garantizar la integridad de los datos (por ejemplo, ISBN-13 válido, fechas de publicación razonables). Es ideal para bibliotecas físicas o digitales.

### Características
- **Modelos**: Incluye cinco modelos:
  - **Categoría**: Clasifica los libros (ej. Ficción, No Ficción).
  - **Autor**: Registra información de autores (nombre, apellido, nacionalidad).
  - **Libro**: Gestiona libros con título, ISBN, género, categoría y autores.
  - **Usuario**: Usa el modelo `User` de Django para autenticación.
  - **Préstamo**: Registra préstamos de libros con fechas y estado (Activo/Devuelto).
- **Validadores**: Aseguran datos consistentes (por ejemplo, ISBN de 13 dígitos, fechas válidas).
- **Vistas**: Lista de categorías, libros por categoría y detalles de préstamos.
- **API REST** (opcional): Expuesta para consultar libros.
- **Formulario**: Permite registrar nuevos préstamos.
- **Admin**: Panel de administración personalizado para gestionar datos.

## Requisitos
- Python 3.8 o superior
- Django (ver `requirements.txt`)
- Opcional: Django REST Framework (para la API)

## Instalación en Windows

1. **Clona el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd biblioteca_proyecto
   ```

2. **Crea y activa un entorno virtual**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica las migraciones**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crea un superusuario**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Pobla la base de datos** (opcional):
   ```bash
   python manage.py poblar_biblioteca
   ```

7. **Inicia el servidor**:
   ```bash
   python manage.py runserver
   ```

8. **Accede al sistema**:
   - Categorías: `http://127.0.0.1:8000/categorias/`
   - Admin: `http://127.0.0.1:8000/admin/` (usa las credenciales del superusuario)


## Licencia
MIT License
