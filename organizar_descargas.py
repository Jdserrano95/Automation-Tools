import os
import shutil
from pathlib import Path

# 1. Definimos las categorías y sus extensiones
MAPA_EXTENSIONES = {
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Instaladores": [".exe", ".msi"],
    "Comprimidos": [".zip", ".rar", ".7z", ".tar"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Musica": [".mp3", ".wav", ".flac"],
}

def organizar_descargas():
    # 2. Obtener la ruta de la carpeta de Descargas del usuario actual
    ruta_descargas = Path.home() / "Downloads"

    if not ruta_descargas.exists():
        print(f"No se encontró la ruta: {ruta_descargas}")
        return

    print(f"Organizando archivos en: {ruta_descargas}...")

    # 3. Iterar sobre los archivos en la carpeta
    for archivo in ruta_descargas.iterdir():
        # Ignorar si es una carpeta o un archivo oculto
        if archivo.is_dir() or archivo.name.startswith("."):
            continue

        extension = archivo.suffix.lower()
        encontrado = False

        for categoria, extensiones_validas in MAPA_EXTENSIONES.items():
            if extension in extensiones_validas:
                # 4. Definir y crear la carpeta de destino
                carpeta_destino = ruta_descargas / categoria
                carpeta_destino.mkdir(exist_ok=True)

                # 5. Mover el archivo
                try:
                    shutil.move(str(archivo), str(carpeta_destino / archivo.name))
                    print(f"Movido: {archivo.name} -> {categoria}")
                except Exception as e:
                    print(f"Error al mover {archivo.name}: {e}")
                
                encontrado = True
                break
        
        if not encontrado and extension != "":
            print(f"Sin categoría para: {archivo.name}")

if __name__ == "__main__":
    organizar_descargas()
    print("¡Limpieza completada!")
