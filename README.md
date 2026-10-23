# Proyecto 0

Herramienta en Python para procesar y analizar observaciones meteorológicas del Servicio Meteorológico Nacional (SMN).

## Funciones Principales

*   **Cantidad de ciudades leídas:** Calcula el total de registros procesados.
*   **Temperaturas extremas:** Identifica la ciudad con la temperatura máxima y mínima.
*   **Top N ciudades:** Función genérica para ordenar ciudades de mayor a menor según cualquier campo (temperatura, viento, etc.).
*   **Vientos extremos:** Determina las velocidades de viento máxima y mínima.
*   **Separador de viento:** Convierte cadenas como "Norte 3" en tuplas (dirección, velocidad) y maneja el caso de "Calma".
*   **Reporte de faltantes:** Genera un diccionario agrupando por campo las ciudades que contienen datos nulos (None).

## Enlaces de Interés

- [Sitio oficial del SMN - Descarga de datos](https://www.smn.gob.ar/descarga-de-datos)

## Preparación de los datos

1. Ingresá al sitio del SMN desde el enlace provisto arriba y descargá el archivo con los datos meteorológicos (`.rar` o `.zip`).
2. Creá una carpeta llamada `datos` en el directorio principal de este proyecto.
3. Extraé los archivos de texto (`.txt`) del archivo comprimido y guardalos dentro de la carpeta `datos`.

## Ejecución

Para procesar un archivo, abrí la terminal en la carpeta del proyecto y ejecutá el siguiente comando:

```bash
python smn.py datos/nombre_archivo.txt
```

## Ejemplo de ejecución en terminal

```text
archivo del SMN, convirtiendo a json...
Parseando Fecha a Json...
el directorio obs_json no existe, creándolo...
Archivo guardado exitosamente en obs_json/nombre_archivo.json
Ciudades totales: 121
Ciudades completas: 25
