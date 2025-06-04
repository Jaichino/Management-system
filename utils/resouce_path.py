##############################################################################
# Importaciones
##############################################################################
from pathlib import Path
import sys

##############################################################################
# Métodos para el manejo de rutas ejecutable / codigo
##############################################################################
def get_resource_path(relative_path: str | Path) -> Path:
    """Obtiene la ruta absoluta al recurso, compatible con PyInstaller."""
    try:
        base_path = Path(sys._MEIPASS)
    except AttributeError:
        base_path = Path(__file__).resolve().parent.parent
    
    return base_path / relative_path


def get_output_path(relative_path: str | Path) -> Path:
    ''' Función para obtener rutas de guardado de archivos
    '''
    if getattr(sys, 'frozen', False):
        base_path = Path(sys.executable).parent.parent # raíz en ejecutable
    else:    
        base_path = Path(__file__).resolve().parent.parent  # raíz del proyecto

    return base_path / relative_path