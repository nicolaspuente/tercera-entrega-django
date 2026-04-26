# Proyecto Final Django - Blog

## Descripción

Este proyecto es una aplicación web desarrollada con Django que funciona como un blog. Permite a los usuarios registrarse, iniciar sesión y gestionar publicaciones. También incluye un sistema de mensajería entre usuarios y la posibilidad de editar un perfil personal.

El objetivo del proyecto es integrar los conceptos vistos durante el curso, como modelos, vistas, formularios, autenticación y manejo de templates.

---

## Funcionalidades principales

- Registro de usuarios  
- Inicio y cierre de sesión  
- Edición de perfil (datos personales, avatar, biografía, etc.)  
- Cambio de contraseña  
- Creación de publicaciones  
- Edición y eliminación de publicaciones  
- Visualización de publicaciones (listado y detalle)  
- Subida de imágenes en cada publicación  
- Editor de texto enriquecido (CKEditor)  
- Sistema de mensajería entre usuarios  
- Panel de administración de Django  

---

## Tecnologías utilizadas

- Python  
- Django  
- SQLite  
- HTML  
- CKEditor  

---

## Estructura del proyecto

El proyecto está dividido en distintas aplicaciones:

- **app**: contiene la vista de inicio  
- **pages**: gestiona las publicaciones del blog  
- **accounts**: maneja el registro, login, perfil y autenticación  
- **messenger**: permite el envío y recepción de mensajes entre usuarios  

---
git add .

## Cómo ejecutar el proyecto

1. Clonar el repositorio  

2. Crear un entorno virtual  
```bash
python -m venv venv
```

3. Activar el entorno virtual  
```bash
venv\Scripts\activate
```

4. Instalar las dependencias  
```bash
pip install -r requirements.txt
```

5. Aplicar migraciones  
```bash
python manage.py migrate
```

6. Ejecutar el servidor  
```bash
python manage.py runserver
```

7. Abrir en el navegador  
```txt
http://127.0.0.1:8000/
```

---

## Notas importantes

- El archivo `db.sqlite3` no está incluido en el repositorio  
- La carpeta `media/` tampoco se incluye para evitar subir archivos pesados  
- Para acceder al panel de administración se debe crear un superusuario:  


python manage.py createsuperuser


---

## Autor

Nicolás Puente