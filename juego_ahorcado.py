import random

# Lista de palabras posibles, modifica las palabras a tu gusto
palabras = ["python", "robotica", "programacion", "algoritmo", "funcion"]

def seleccionar_palabra():
    return random.choice(palabras)

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra
        else:
            progreso += "_"
    return progreso

def juego_ahorcado():
    palabra = seleccionar_palabra()
    letras_adivinadas = []
    intentos_restantes = 6

    # Inicio del Juego  
    print("¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra letra por letra. Tienes 6 intentos.")

    #Ciclo repetitivo para establecer los intentos
    while intentos_restantes > 0:
        print(f"\nPalabra: {mostrar_progreso(palabra, letras_adivinadas)}")
        print(f"Letras adivinadas: {', '.join(letras_adivinadas)}")
        print(f"Intentos restantes: {intentos_restantes}")

        letra = input("Introduce una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("¡Bien hecho! Esa letra está en la palabra.")
            if mostrar_progreso(palabra, letras_adivinadas) == palabra:
                print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
                break
        else:
            intentos_restantes -= 1
            print("Oh no... esa letra no está en la palabra.")

    #En caso de no completar el juego
    if intentos_restantes == 0:
        print(f"Lo siento, has perdido. La palabra era: {palabra}")

# Llamada a la función para iniciar el juego
juego_ahorcado()
