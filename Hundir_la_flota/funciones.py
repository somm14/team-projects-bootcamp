from clases import*
from variables import*
import random


#1. CLASE TABLERO 
#2. VARIABLES TABLERO VACIO 
#3. VARIABLES PARA FUNCION BIENVENIDA 



#4. FUNCION BIENVENIDA 
def bienvenida(): 
    global player1, player2
    print("\n¡Bienvenido a 'Hundir la flota' ", player1, "!", sep="")
    print("\nSu oponente será la ", player2, ". Que gane el mejor.\n", sep="")
    print("Los tableros de ambos jugadores serán una cuadrícula de 10x10.")
    input(f"{player1}, tú y la máquina tendreis cada uno un tablero como este:\n\n {tablero1}\n\n\tPulsa intro para posicionar tus barcos.")
   


#5. CLASE BARCOS 
#6. VARIABLES BARCO 
#7. VARIABLE PARA POSICIONAR BARCOS 



#8. POSICIONAR BARCOS EN TABLERO
def colocar_barcos():
    global tablero1_barco, tablero2_barco, barcos_player1, barcos_player2
    tablero1_barco = barcos_player1.coloca_barco(tablero1_barco)  
    print("\n",player1, "la posición de tus barcos es la siguiente:")
    print(tablero1_barco)

    for barco in barcos_player2: #Bucle para recorrer la lista de barcos del player2 y añadirlos en el tablero
        barco.coloca_barco_aleatorio()
    
    input("\n\tPresiona Intro para empezar a disparar.")



#9. CONTROL DE ERRORES Y PETICIÓN DE FILA COLUMNA 
def coordenadas_disparo(): 
    try:       
        fila= int(input("\nNúmero de fila donde quieres disparar del 1 al 10: "))
        columna = int(input("Número de columna donde quieres disparar del 1 al 10: "))
    except:
        print("\n\tPor favor, introduce un número del 1 al 10, vuelve a intentarlo.\n")
        return coordenadas_disparo()
    if (fila < 1) or (fila > 10) or (columna < 1) or (columna > 10):      
        print("\n\tPor favor, introduce un numero del 1 al 10, vuelve a intentarlo.\n")
        return coordenadas_disparo()
    else:
        print()
        print(f"\tEl disparo se efectuará en la coordenada: ({fila},{columna})")
        return fila, columna     



#10. JUGAR (CONTADOR DE VIDAS) 
def jugar(): 
    global vidas1, vidas2, player1, player2
    while True:
        acierto = disparar(tablero2, tablero2_barco)
        if acierto:
            if vidas2 == 0:
                print(f"¡Enhorabuena {player1}, has ganado! El jugador {player2} se ha quedado con {vidas2} vidas.")
                break
        else:
            print("Has fallado es turno de la máquina.")
            #PARA SEGUIR JUNGANDO:
            respuesta = input("\nSi quieres parar el juego, escribe: Stop.\nPara continuar pulse: Intro\n").title()
            if respuesta == "Stop":
                print("El juego ha terminado. ¡Gracias por jugar!")
                break
            acierto_maquina = disparar_maquina(tablero1, tablero1_barco)
            if acierto_maquina:
                if vidas1 == 0:
                    print(f"¡Enhorabuena {player2}, has ganado! El jugador {player1} se ha quedado con {vidas1} vidas.")
                    break
            else:
                print("La computadora no ha acertado. Turno del jugador.")
    print("se acabo")  




#11. DISPARAR JUGADOR 
def disparar(tablero, tablerobarco):  
    global tablero2, tablero2_barco, vidas2
    fila_disparo, columna_disparo = coordenadas_disparo()
    #Comprobar si el disparo ya se ha ejecutado
    if tablero2[fila_disparo-1][columna_disparo-1] == 'X' or tablero2[fila_disparo-1][columna_disparo-1] == 'A':
        print("\nYa has disparado en esta coordenada. Vuelve a poner coordenadas diferentes")
        return disparar(tablero, tablerobarco)
    #SI HAY IMPACTO
    if tablero2_barco[fila_disparo-1][columna_disparo-1] == 'O':   
        tablero2[fila_disparo-1][columna_disparo-1] = 'X'  
        vidas2 -= 1
        print(f"\nEl jugador {player1} ha acertado. Ha quitado una vida a {player2}, le quedan {vidas2}.") 
        acierto = True
        print(f"\nVuelves a disparar {player1}")
        print("\nAsi queda el tablero del jugador", player2,"\n",tablero2)
        if acierto == True:
            return True
        else:
            return False
    #CUANDO NO HAY IMPACTO
    else:
        tablero2[fila_disparo-1][columna_disparo-1] = 'A'  
        print(f"\nEl jugador {player1} no ha acertado. Le quedan {vidas2} vidas al jugador {player2}.") 
        print("\nAsi queda el tablero del jugador", player2,"\n",tablero2)
        return False



#12. DISPARAR MAQUINA   
def disparar_maquina(tablero,tablerobarco):
    global tablero1, tablero1_barco, vidas1
    fila = random.randint(0,9)
    columna = random.randint(0,9)
    if tablero1_barco[fila][columna] == 'O':  
        tablero1[fila][columna] = 'X' 
        vidas1 -= 1
        print(f"El jugador {player2} ha acertado. Ha quitado una vida a {player1}, le quedan {vidas1}") 
        print("\nAsi queda el tablero del jugador", player1,"\n",tablero1)
        print(f"\n{player2} vuelve a disparar")
        return disparar_maquina(tablero, tablerobarco)
    else:
        tablero1[fila][columna] = 'A' 
        print(f"\nEl jugador {player2} no ha acertado. Le quedan {vidas1} vidas al jugador {player1}") 
        print("\nAsi queda el tablero del jugador", player1,"\n",tablero1)
        print("\nEs tu turno")
        return vidas1 









































# #13. SEGUIR JUGANDO
# def seguir_jugando():
#     respuesta = input("¿Quieres seguir jugando? (si/no): ").lower()
#     if respuesta == "si":
#         return True
#     elif respuesta == "no":
#         print("El juego ha terminado. ¡Gracias por jugar!")
#         return False
#     else:
#         print("Respuesta no válida. Por favor, escribe 'si' o 'no'.")
#         return seguir_jugando()
    


'''
def jugar_juego(jugador_turno, vidas_otro_jugador,tablero):
#Tenemos que crear una función para jugar que incluya todas las funciones. 
#Esta que he creado es orientativa la necesitaba para guiarme en la función por turnos

#función vida
while vidas1 > 0 and vidas2 > 0:   #el mensaje de bloque con sangría es porque arriba está la función def jugar_juego
    print("Turno del jugador 1. Vidas :{vidas1}")
    print("Turno del jugador 2. Vidas; {vidas2}")  
    #Aquí definiria la función de los turnos
    while True:
        if vidas1 <= 0:
            print(f"{player2} ha gando. El judador 1 se ha quedado con {vidas1} vidas")
            break
        elif vidas2 <= 0:
            print(f"{player1} he ganado. El judador 2 se ha quedado con {vidas2} vidas")
            break
        else:
            if vidas1 > vidas2: #REVISAR NOTAS# Empieza el turno el jugador 1, se define argumentos de la función del juego
                jugador_turno = player1
                otro_jugador = player2
                vidas_otro_jugador = vidas2
                tablero = tablero2
            else:
                jugador_turno = player2
                otro_jugador = player1
                vidas_otro_jugador = vidas1
                tablero = tablero1
            while True:
                acierto = jugar_juego(jugador_turno, vidas_otro_jugador, tablero)
                if acierto == True: 
                    vidas_otro_jugador -= 1
                    print(f"El jugador {jugador_turno} ha acertado. Ha quitado una vida a {otro_jugador}")
                    continue              
                else:
                    print(f"El jugador {jugador_turno} ha fallado. Cambio de turno al {otro_jugador}")
                    break

                    
                    No tengo muy clara esta última parte si termina de funcionar. Lo he intentado probar en python tutor pero antes me pide tableros y otras 
                    funciones que aún no estan definidas. 

                    Esto de aquí acabo es una alternativa al final de la función turnos que aún tengo que pulir si no funciona lo de arriba 
                    else:
                        print("Es turno de "({player2 if jugador_turno == player1 if not player1})
                        break
                                                               
    print("El juego ha terminado")


    # Funciones para disparar y comprobar si hay barcos
'''
# FUNCION PARA CONTINUAR EN EL JUEGO
#Seria la funcion 13


# # PARA UTILIZARLA.
# '''
# Creo que que se debería hacer así pero no me ha dado tiempo a probarla
# '''
# while True:
#     # Aquí iría el código para disparar en el juego

#     # Después de disparar, se pregunta al jugador si quiere seguir jugando
#     if not seguir_jugando():
#         break



#10. VARIABLES VIDAS
'''
#11. CONTADOR DE VIDAS [Genma]   [Víctor]#salen varios errores con las vidas edito contador vidas
def contador_vidas(vidas):
    global vidas1, vidas2
    if vidas1 == 0:
        print("Ohhh has perdido, gana la", player2)
        return False
    elif vidas2 == 0:
        print("Enhorabuena!!! Has ganado a la", player2)
        return False
    else:
        print(f"{player1} tiene {vidas1} vidas y {player2} tiene {vidas2} vidas.")
        return True

def contador_vidas(vidas1, vidas2):  #[Víctor] He cogido la función de Genma y la anterior mia. He hecho una fusión como vegeta y goku pero ha dado errores :(
    if vidas1 == 0:
        print(f"{player2} ha gando. El judador 1 se ha quedado con {vidas1} vidas")
        return False
    elif vidas2 == 0:
        print(f"{player1} he ganado. El judador 2 se ha quedado con {vidas2} vidas")
        return False
    else:
        print(f"{player1} tiene {vidas1} vidas y {player2} tiene {vidas2} vidas.")
        return True
'''
# #10. CONTADOR VIDAS segunda versión del contador vidas, he dejado las dos anteriores entre comillas   
# def contador_vidas(player1, player2, vidas1, vidas2): #[Victor] Función para actualizar la vida restante de los jugadores, he cogido recorte de la de [Genma] 
#     if player1:  # Daba error al tener solo vidas, tuve que enlazar player 1 con vidas 1 y por descarte se enlaza player2 con vidas2
#         vidas1 -= 1    #Si juegua
#     else:
#         vidas2 -= 1

#     if vidas1 == 0:
#         print(f"¡Enhorabuena {player2} has ganado! El jugador {player1} se ha quedado con {vidas1} vidas.")
#         return False
#     elif vidas2 == 0:
#         print(f"¡Enhorabuena {player1}has ganado! El jugador {player2} se ha quedado con {vidas2} vidas.")
#         return False

#     # Dice vidas restantes, pero ya está incluida en las funciones de disparar. Mañana podemos probar a quitarla a ver si no afecta
#     print(f"{player1} tiene {vidas1} vidas y {player2} tiene {vidas2} vidas.")
#     return True
# 
# 
'''
#14 FUNDICON BUCLE
def jugar():
    global vidas
    while True:
        vidas, acierto = disparar(tablero2, tablero2_barco)
        if vidas == False:
            break
        elif acierto == False:
            break
        else:
            continue
    #while True:
        #disparar_maquina(tablero1, tablero1_barco)
    jugar()

'''

        
# #QUEDAN BARCOS?      [Genma] Creo que está no hace falta con el contador de vidas.
# def hay_barcos(tablero):
#     # Comprueba si quedan barcos en el tablero
#     for fila in tablero:
#         if 'B' in fila:
#             return True
#     return False
    

