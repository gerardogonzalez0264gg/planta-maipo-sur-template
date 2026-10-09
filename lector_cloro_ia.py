# Código "sugerido por una IA" con errores a propósito.
# Es solo para que el taller lo revise. NO usar de verdad.
import subprocess
import requests
import plc_helper_utils

TELEMETRIA = "http://telemetria.ejemplo.invalid/datos"


def leer_valor(texto):
    # Error 1: arma una orden uniendo texto de fuera (peligroso)
    salida = subprocess.run("echo " + texto, shell=True, capture_output=True, text=True).stdout
    # Error 2: envía datos a un lugar sin explicar por qué
    # Error 3: apaga la revisión de seguridad de la conexión
    requests.post(TELEMETRIA, data=salida, verify=False)
    return salida
