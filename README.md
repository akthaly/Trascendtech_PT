# Módulo: Gestión de Activos Internos - Trascendtech

## 1. Descripción del Módulo
Creación de un Módulo usando el ERP de Odoo, este Módulo permite a una empresa registrar, controlar y dar seguimiento a los bienes físicos y digitales que forman parte de su operación
diaria.

Listado de Activos agregados al módulo: Laptop, Monitor, Licencia, Impresora, Otro


## 2. Pasos para levantar el entorno local
El proyecto está contenerizado usando Docker para garantizar un entorno reproducible.

**Prerrequisitos:** Tener Docker y Docker Compose instalados.

**Instrucciones:**
1. Clonar este repositorio.
2. Abrir una terminal en la raíz del proyecto (donde se encuentra el `docker-compose.yml`).
3. Ejecutar el siguiente comando para levantar la base de datos PostgreSQL y el servidor de Odoo 16:
   ```bash
   docker compose up -d
4. Ingresar desde cualquier navegador (preferiblemente Chrome, Firefox, o Brave) al siguiente URL: http://localhost:8069/
5. Crear la base de datos inicial (Empleados)
6. Activar el Modo Desarrollador dentro de Odoo, actualizar el listado de aplicaciones e instalar el módulo 'Gestión de Activos Internos'.

## 3. Decisiones técnicas tomadas
-Se eligió desarrollar el módulo usando la estructura nativa de Odoo para mayor facilidad a la hora de integrar los datos con el módulo de recursos humanos para la asignación de activos.
-Para validar la creación única de el código interno se usó la restricción a nivel de la base de datos con `_sql_constraints` en lugar de hacer una validación desde Python para mayor certeza.
-Se hizo uso de el decorador @api.constraint para la restricción del estado Asignado para asegurar que esta regla se cumpla así se haga manualmente desde la web, o por medio de importación de datos.

## 4. Problemas encontrados y cómo fueron resueltos
Durante el desarrollo del módulo me encontré con distintos errores, los cuales fueron los siguientes:

1. 
    - Error en el archivo `__manifest__.py`.
    - Solución: usando el comando docker compose logs -f web se detectó que era por la falta de una coma en una linea de código y se corrigió.

2. 
    - Error de instalación del módulo desde Odoo
    - Solución leyendo los detalles del error que marcaba de Odoo fue un error de escritura, no se encontraba el archivo activo_interno_views.xml, desde el archivo `__manifest__.py` se verificó y el nombre correcto debía ser activo_interno_views.xml, se corrió.

## 5. Mejoras para una versión mejorada
Para una versión mejorada y dedicada a producción podría implementarse un campo para generación de códigos de barra o QR para el Código Interno de cada Activo. También podría implementarse detección de tiempo de un Activo en estado 'Reparación' para mayor control de los estados.