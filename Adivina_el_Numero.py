from random import randint
from os import system

numero_maquina = randint(1,100)
print('\nBienvenidos a "Adivina el Número"!!\n\n' + 
      'Voy a pensar en un valor y deberás acertar\n' + 
      'de que número se trata.\n' + 
      'No te preocupes, no voy a ser cruel... si quieres te iré dando\n' + 
      'pistas sobre de que número se trata, aunque si eres\n' +
      'valiente puedes jugar sin mi ayuda. También \n' + 
      'puedes rendirte si pulsas cero.\n')

input('Si estás listo pulsa ENTER para empezar la partida...\n')
system('cls')


dificultad = int(input('Pero antes...elige la dificultad: Fácil(0) o Difícil(1): '))
system('cls')


if dificultad == 0:

    numero_jugador = int(input("Introduce un número entre 1 y 100: "))
    system('cls')

    contador = 1 

    while numero_jugador != numero_maquina:
        
        if numero_jugador == 0:
            print('\nAcepto tu rendición. Bien jugado!\n')
            break
        elif numero_jugador < 0 or numero_jugador > 100:
            print('\nRecuerda que es un número entre 1 y 100!!')
        elif numero_jugador > numero_maquina:
            print('\nMuy alto quizás, prueba con un valor más pequeño.')
        elif numero_jugador < numero_maquina:
            print('\nNo, ese número es más pequeño, prueba con otro mayor a ver que tal.')
        
        contador += 1
        
        numero_jugador = int(input("\nVuelve a introducir un número un número o introduce 0 para rendirte...: "))
        system('cls')
        
    if numero_jugador == numero_maquina:    
        print(f'\nHas ganado!! Solo te ha costado {contador} intentos.\n')

    
elif dificultad == 1:
    
    numero_jugador = int(input("Introduce un número entre 1 y 100: "))
    system('cls')

    contador = 0 

    while numero_jugador != numero_maquina:
        
        if numero_jugador == 0:
            print('\nAcepto tu rendición. Bien jugado!\n')
            break
        elif numero_jugador < 0 or numero_jugador > 100:
            print('\nRecuerda que es un número entre 1 y 100!!')
        else:
            print(f'No, {numero_jugador} no es correcto. Intentalo de nuevo.')
            
        contador += 1
        
        numero_jugador = int(input("\nVuelve a introducir un número un número o introduce 0 para rendirte...: "))
        system('cls')
        
    if numero_jugador == numero_maquina:    
        print(f'\nHas ganado!! Solo te ha costado {contador} intentos.\n')

