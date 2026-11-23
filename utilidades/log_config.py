
import logging
import os

# Crear la carpeta de registros si no existe
os.makedirs("logs", exist_ok=True)

# Configurar el registro de eventos
logging.basicConfig(
    filename="logs/software_fj.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Obtener el registrador del sistema
logger = logging.getLogger("SoftwareFJ")
