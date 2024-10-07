import os # Módulo para interactuar con el sistema operativo
import shutil  # Módulo para manipular archivos y director

# Define el directorio donde se encuentran los archivos descargados
ruta_descargas = '/tu/dir/descargas'  # Cambia esta ruta a la carpeta que desees organizar

# Define las carpetas donde se moverán los archivos según su tipo
new_folder = {
    'imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'documentos': ['.pdf', '.docx', '.doc', '.txt', '.odt'],
    'hojas_calculo': ['.xls', '.xlsx', '.csv'],
    'presentaciones': ['.ppt', '.pptx'],
    'comprimidos': ['.zip', '.rar', '.tar', '.gz'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'audios': ['.mp3', '.wav', '.aac'],
    'otros': []  # Archivos que no coincidan con ninguna categoría
}

def move_file(file_path, folder):
    """
    Mueve el archivo a la carpeta de destino. Si existe un archivo con el mismo nombre,
    lo renombra añadiendo un número al final para evitar sobrescrituras.
    """
    filename = os.path.basename(file_path)
    dest_path = os.path.join(folder, filename)

    # Si ya existe un archivo con el mismo nombre, agrega un sufijo para evitar sobrescritura
    if os.path.exists(dest_path):
        base, extension = os.path.splitext(filename)
        counter = 1
        new_filename = f"{base}_{counter}{extension}"
        dest_path = os.path.join(folder, new_filename)
        while os.path.exists(dest_path):
            counter += 1
            new_filename = f"{base}_{counter}{extension}"
            dest_path = os.path.join(folder, new_filename)

    shutil.move(file_path, dest_path)
    print(f'Movido: {file_path} -> {dest_path}')

def organize_files(directory):
    # Crea las carpetas si no existen
    for folder in new_folder.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    # Mover archivos a la carpeta correspondiente
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()  # Obtiene la extensión del archivo
            moved = False

            for folder, extensions in new_folder.items():
                if file_extension in extensions:
                    folder_path = os.path.join(directory, folder)
                    move_file(file_path, folder_path)
                    moved = True
                    break

            if not moved:
                # Mover archivos desconocidos a la carpeta 'otros'
                folder_otros = os.path.join(directory, 'otros')
                if not os.path.exists(folder_otros):
                    os.mkdir(folder_otros)
                move_file(file_path, folder_otros)

if __name__ == '__main__':
    organize_files(ruta_descargas)
    print('Archivos organizados correctamente')
