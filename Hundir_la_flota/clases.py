import numpy as np
import random

#1. CLASE TABLERO 
class Tablero():      
    def __init__(self, tamaño = 10):
        self.tamaño = tamaño
        
    def tablero_player1(self, tamaño):
        t1 = np.full((tamaño,tamaño), " ")
        return t1  
    
    def tablero_player2(self, tamaño):
        t2 = np.full((tamaño,tamaño), " ")
        return t2 





#5. CLASE BARCOS 
class Barco:
    
    barcos = [[(0,1), (4, 3), (8, 8), (7, 1)], # barco1 (1 esolora x 4)
              [(2,2), (2,1), (5,6), (4,6), (9,6), (9,5)], # barco2 (2 esloras x 3)
              [( 9,1), (9,2), (9,3), (0,7), (1,7), (2,7)], # barco3 (3 esloras x 2)
              [(7,3), (7,4), (7,5), (7,6)]] # barco4 (4 esloras x 1)

    def coloca_barco(self, tablero):  
        for barco in self.barcos:
            for pieza in barco:
                tablero[pieza] = "O"
        return tablero
    
class Barco_npc:
    def __init__(self, tablero, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.tablero = tablero

    def coloca_barco_aleatorio(self):
        intentos_max = 100  # Número de intentos para poder posicionar todos los barcos dados
        for _ in range(intentos_max):
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            orientacion = random.choice(["N", "S", "E", "O"])

            if orientacion == "N":
                if fila - self.longitud + 1 >= 0:  # Comprueba si hay espacio hacia arriba
                    if all(self.tablero[fila - i, columna] == " " for i in range(self.longitud)):
                        for i in range(self.longitud):
                            self.tablero[fila - i, columna] = "O"
                        return True

            elif orientacion == "S": # Comprueba si hay espacio hacia abajo
                if fila + self.longitud - 1 <= 9:  
                    if all(self.tablero[fila + i, columna] == " " for i in range(self.longitud)):
                        for i in range(self.longitud):
                            self.tablero[fila + i, columna] = "O"
                        return True

            elif orientacion == "E": # Comprueba si hay espacio hacia la derecha
                if columna + self.longitud - 1 <= 9:  
                    if all(self.tablero[fila, columna + i] == " " for i in range(self.longitud)):
                        for i in range(self.longitud):
                            self.tablero[fila, columna + i] = "O"
                        return True

            elif orientacion == "O": # Comprueba si hay espacio hacia la izquierda
                if columna - self.longitud + 1 >= 0:  
                    if all(self.tablero[fila, columna - i] == " " for i in range(self.longitud)):
                        for i in range(self.longitud):
                            self.tablero[fila, columna - i] = "O"
                        return True

        return False 



