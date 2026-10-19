from funciones_smn import leer_observaciones, cantidad_ciudades_leidas, cantidad_ciudades_completas, mostrar_resumen
import sys
from pathlib import Path
import json

#================================== TERMINAL ==================================

if __name__ == '__main__':
    # Verificar que le hayas pasado argumento correctamente a la terminal
    if len(sys.argv) > 2: # Si le pasaste mas de 2 argumentos a la terminal= error
        print("Error: Ingresó demasiados parámetros antes de cerrar el programa.")
        sys.exit(1)

    elif len(sys.argv) == 1: # Si le pasas 1 le das una ayuda al usuario diciendo q carpetas tiene en datos
        print("Error: Falta ingresar la ruta del archivo.")
        datos_txt =list(Path("datos").glob("*.txt"))
        datos_json = list(Path("obs_json").glob("*.json"))
        print(f"Archivos disponibles: {len(datos_txt)} .txt y {len(datos_json)} .json")
        sys.exit(1)

    else: # Si le pasas 2 archivos el poscision 1 va a ser el path
        ruta_archivo = Path(sys.argv[1])

        # Verificar si es .txt o .json
        if ruta_archivo.suffix == ".txt":

            #Creacion de las dos variables
            diccionario_final, lineas_invalidas = leer_observaciones(ruta_archivo)

            # Imprime el aviso si hubo errores
            if lineas_invalidas > 0:
                print(f"Aviso: Se ignoraron {lineas_invalidas} líneas por formato inválido.\n")
            
            print('Parseando Fecha a Json...')
            for valores in diccionario_final.values(): 
                # Sobreescribo el resultado de "Fecha" para que el Json lo acepte
                valores["Fecha"] = valores["Fecha"].isoformat(timespec='minutes')


            salida = Path("obs_json")
            print('archivo del SMN, convirtiendo a json...')

            if salida.exists():
                print("Ya existe el directorio")
            else:
                salida.mkdir(parents=True, exist_ok=True) # creo archivo
                print('el directorio obs_json no existe, creándolo...')
            
            ruta = salida / f"{ruta_archivo.stem}.json"

            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(diccionario_final, archivo, ensure_ascii=False, indent=2)

           
            mostrar_resumen(diccionario_final)

        elif ruta_archivo.suffix == ".json":
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                datos_json = json.load(archivo)

            print(f"Ciudades totales: {cantidad_ciudades_leidas(datos_json)}")
            print(f"Ciudades completas: {cantidad_ciudades_completas(datos_json)}")

        else:
            print("Error: la extensión no es ni .txt ni .json.")
