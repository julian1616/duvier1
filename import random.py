import random

def generar_numero_aleatorio():
    return random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100

# Ejemplo de uso
numero_aleatorio = generar_numero_aleatorio()
print("Adivina el número entre 1 y 100.")
intentos = 0
while True:
    intento = int(input("Introduce tu conjetura: "))
    intentos += 1
    if intento < numero_aleatorio:
        print("Muy bajo. sapo perra.")
    elif intento > numero_aleatorio:
        print("Muy alto. Intenta de duvier toro")
    else:
        print(f"¡Correcto! ¡Has adivinado el número en {intentos} intentos!")
        break
