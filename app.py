# write 'hello world' to the console
print('hello world')
import random

def jugar_una_vez():
    opciones = ['piedra', 'papel', 'tijera']
    eleccion_computadora = random.choice(opciones)
    eleccion_jugador = input("Elige piedra, papel o tijera: ").lower()

    if eleccion_jugador not in opciones:
        print("Opción inválida. Por favor elige piedra, papel o tijera.")
        return (0, 0)  # Empate técnico debido a entrada inválida

    print(f"Jugador eligió {eleccion_jugador}, computadora eligió {eleccion_computadora}.")

    if eleccion_jugador == eleccion_computadora:
        print("Es un empate.")
        return (0, 0)
    elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or \
         (eleccion_jugador == "tijera" and eleccion_computadora == "papel") or \
         (eleccion_jugador == "papel" and eleccion_computadora == "piedra"):
        print("¡Ganaste!")
        return (1, 0)
    else:
        print("Perdiste.")
        return (0, 1)

def jugar():
    puntaje_jugador = 0
    puntaje_computadora = 0

    while True:
        resultado_ronda = jugar_una_vez()
        puntaje_jugador += resultado_ronda[0]
        puntaje_computadora += resultado_ronda[1]

        seguir_jugando = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if seguir_jugando != 's':
            break

    print(f"Puntaje final - Jugador: {puntaje_jugador}, Computadora: {puntaje_computadora}")

jugar()