import os
import shutil
import re

def organizar_archivos_pacientes(carpeta_origen):
    """
    Organiza archivos de pacientes en carpetas según cédula y nombre.
    Formato esperado: TIPO-CEDULA-NOMBRE COMPLETO.extensión
    """
    
    # Verificar que la carpeta existe
    if not os.path.exists(carpeta_origen):
        print(f"Error: La carpeta '{carpeta_origen}' no existe")
        return
    
    # Obtener todos los archivos en la carpeta
    archivos = [f for f in os.listdir(carpeta_origen) 
                if os.path.isfile(os.path.join(carpeta_origen, f))]
    
    if not archivos:
        print("No se encontraron archivos en la carpeta")
        return
    
    archivos_organizados = 0
    archivos_omitidos = 0
    
    for archivo in archivos:
        # Dividir por guiones
        partes = archivo.split('-')
        
        # Verificar que hay al menos 3 partes (TIPO-CEDULA-NOMBRE)
        if len(partes) >= 3:
            cedula = partes[1].strip()
            # El nombre puede contener guiones, así que unimos el resto
            nombre_con_ext = '-'.join(partes[2:])
            # Quitar la extensión del nombre
            nombre = os.path.splitext(nombre_con_ext)[0].strip()
            
            # Crear nombre de carpeta: CEDULA-NOMBRE
            nombre_carpeta = f"{cedula}-{nombre}"
            ruta_carpeta = os.path.join(carpeta_origen, nombre_carpeta)
            
            # Crear la carpeta si no existe
            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)
                print(f"Carpeta creada: {nombre_carpeta}")
            
            # Mover el archivo a la carpeta
            ruta_origen = os.path.join(carpeta_origen, archivo)
            ruta_destino = os.path.join(ruta_carpeta, archivo)
            
            try:
                shutil.move(ruta_origen, ruta_destino)
                print(f"  → Archivo movido: {archivo}")
                archivos_organizados += 1
            except Exception as e:
                print(f"  ✗ Error al mover {archivo}: {e}")
                archivos_omitidos += 1
        else:
            print(f"  ✗ Formato incorrecto, omitido: {archivo}")
            archivos_omitidos += 1
    
    print(f"\n{'='*50}")
    print(f"Proceso completado:")
    print(f"  - Archivos organizados: {archivos_organizados}")
    print(f"  - Archivos omitidos: {archivos_omitidos}")
    print(f"{'='*50}")

# Ejemplo de uso
if __name__ == "__main__":
    # Cambiar esta ruta por la carpeta donde están tus archivos
    carpeta = "."
    
    # O usar la carpeta actual
    # carpeta = "."
    
    print("Organizador de archivos de pacientes")
    print("="*50)
    print(f"Carpeta de origen: {carpeta}\n")
    
    organizar_archivos_pacientes(carpeta)