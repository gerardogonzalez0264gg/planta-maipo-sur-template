# Prueba simple: comprueba que el programa sigue funcionando
import os
from lector_cloro import leer_cloro_simulado

# Si no hay contraseña, pone una falsa solo para la prueba
os.environ.setdefault("PLC_PASSWORD", "VALOR-FICTICIO-DE-PRUEBA")

resultado = leer_cloro_simulado()
assert resultado["cloro_mg_l"] == 0.7
print("Prueba funcional correcta; el secreto no fue mostrado")
