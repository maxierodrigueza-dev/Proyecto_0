from funciones_smn import leer_observaciones, cantidad_ciudades_leidas, cantidad_ciudades_completas, mostrar_resumen
import sys
from pathlib import Path

#================================== TERMINAL ==================================

if __name__ == '__main__':
    # Verificar que le hayas pasado argumento correctamente a la terminal
    if len(sys.argv) > 2: # Si le pasaste mas de 2 argumentos a la terminal= error
        print("Error: Ingresó demasiados parámetros antes de cerrar el programa.")
        sys.exit(1)

    elif len(sys.argv) == 1: # Si le pasas 1 le das una ayuda al usuario diciendo q carpetas tiene en datos
        print("Error: Falta ingresar la ruta del archivo.")
        datos_txt =list(Path("datos").glob("*.txt"))
        
        print(f"Archivos disponibles: {len(datos_txt)} .txt ")
        sys.exit(1)

    else: # Si le pasas 2 archivos el poscision 1 va a ser el path
        ruta_archivo = Path(sys.argv[1])

        # Verificar si es .txt 
        if ruta_archivo.suffix == ".txt":

            #Creacion de las dos variables
            diccionario_final, lineas_invalidas = leer_observaciones(ruta_archivo)

            # Imprime el aviso si hubo errores
            if lineas_invalidas > 0:
                print(f"Aviso: Se ignoraron {lineas_invalidas} líneas por formato inválido.\n")

            mostrar_resumen(diccionario_final)

        else:
            print("Error: la extensión solo acepta .txt")
