PRUEBA EVALUACION 2 - Rizwan y Elia Gil

## Descripción:
Es un aplicación desarrollada con django que funciona como gestor de tareas, que permite a los usuarios registrarse y gestionar sus propias tareas.
Cada usuario puede crear nuevas tareas, modificarlas y eliminarlas y ver el listado completo de las tareas.
La app está desarrollada en lenguaje python, el framework de django siguiendo la estructura basada en MVC, tambien hemos gestionado el control de autenticación para que cada usuario solo gestione sus propias tareas.

## Tecnología usada:
    -Python como lenguaje principal.
    -Django como Framework para el desarrollo.
    -SQLite como base de datos.
    -HTML y CSS para el diseño de la página.



## Funcionalidades: 
    -Registro, inicio y cierre de sesión.
    -CRUD completo de tareas(crear, ver, editar y eliminar).
    -Asociación de cada tarea a su usuario.
    -Control de acceso de cada usuario para que solo acceda a su contenido.



## Como ejecutar:
    -Crear y activar el entorno virtual.
    -Instalar las dependencias con requirements.txt.
    -Aplicar las migraciones con "python manage.py migrate".
    -Ejecutar el servidor con "python manage.py runserver".