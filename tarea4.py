import logging
import shutil

def analizar_espacio():

    logging.basicConfig(filename="/home/jjesus/logs/espacio.log", level=logging.INFO, 
                    format="%(asctime)s- %(levelname)s: %(message)s") 

    total, used, free = shutil.disk_usage("/")

    percent_used = (used / total) * 100

    if percent_used > 80:
        logging.error(f"Espacio ocupado en la particion raiz: {percent_used:.2f}%")
    elif percent_used > 60:
        logging.warning(f"Espacio ocupado en la particion raiz: {percent_used:.2f}%")
    else:
        logging.info(f"Espacio ocupado en la particion raiz: {percent_used:.2f}%")

if __name__ == "__main__": 
    analizar_espacio()