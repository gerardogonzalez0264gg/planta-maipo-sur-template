# Programa de mentira que "lee" el cloro de una planta de agua.
# No se conecta a nada real.
import os


def leer_cloro_simulado():
    # Revisa que la contraseña exista, pero nunca la muestra en pantalla
    if not os.getenv("PLC_PASSWORD"):
        raise RuntimeError("Falta la variable PLC_PASSWORD")
    return {"planta": "Maipo Sur - laboratorio", "cloro_mg_l": 0.7}


if __name__ == "__main__":
    lectura = leer_cloro_simulado()
    print(f"Lectura simulada: {lectura['cloro_mg_l']} mg/L")
