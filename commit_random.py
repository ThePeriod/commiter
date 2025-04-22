import random
import datetime

# Decide aleatoriamente si hacer commit (ej: 50% de probabilidad)
if random.random() < 0.5:
    print("No commit hoy.")
    exit(0)

# Cambia el contenido aleatoriamente
with open("README.md", "a", encoding="utf-8") as f:
    f.write(f"- Actualización aleatoria: {datetime.datetime.now()} | Valor: {random.randint(1, 10000)}\n")
