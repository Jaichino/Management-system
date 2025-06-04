##############################################################################
# Importaciones
##############################################################################

import shutil
import os

from utils.resouce_path import get_resource_path, get_output_path

##############################################################################
# Función para creación de fichas cosmetológicas
##############################################################################

def crear_ficha_cosmetologica(cliente_id: int, nombre: str):
    ''' Función para creación de fichas comestológicas. Primero se obtienen
        las rutas necesarias, se crea nombre de archivo y obtiene la ruta en
        la que se guardará.
        Si la ruta del archivo existe, se abre dicho PDF existente. En caso
        contrario, se hace una copia del modelo de ficha ubicado en 
        utils/planillas y se genera un nuevo archivo pdf.

        :param int cliente_id: ID del cliente de ficha cosmetologica
        :param str nombre: Nombre del cliente
    '''
    # Carpeta de destino
    carpeta_destino = 'fichas_cosmetologicas'
    ubicacion_plantilla = r"utils/plantillas/modelo_ficha_cosmetologica.pdf"

    # Rutas
    path_plantilla = get_resource_path(ubicacion_plantilla)
    path_fichas = get_output_path(carpeta_destino)
    path_fichas.mkdir(exist_ok=True) # Crea la carpeta si no existe

    # Nombramiento del archivo
    nombre_archivo = f'ficha_{cliente_id}_{nombre.replace(' ','_')}.pdf'
    ficha_cliente_path = path_fichas / nombre_archivo

    # Verificación si cliente tiene una ficha
    if ficha_cliente_path.exists():
        # Se abre ficha
        os.startfile(ficha_cliente_path)

    else:
        # Si no tiene ficha, se copia plantilla y se renombra
        shutil.copy(path_plantilla, ficha_cliente_path)
        # Se abre ficha
        os.startfile(ficha_cliente_path)
