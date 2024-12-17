from clases import*

#2. VARIABLES TABLERO VACIO 
tablero1 = Tablero() 
tablero1 = tablero1.tablero_player1(10)

tablero2 = Tablero(10)
tablero2 = tablero2.tablero_player2(10)


#3.VARIABLES PARA FUNCION BIENVENIDA 
player1 = input("Introduzca su nombre:")  
player2 = "computadora" 


#6. VARIABLES BARCO 
barcos_player1 = Barco()   




#7. VARIABLE PARA POSICIONAR BARCOS
tablero1_barco = tablero1.copy()     
tablero2_barco = tablero2.copy() 

barcos_player2 = [
    Barco_npc(tablero2_barco, "barco1", 1),
    Barco_npc(tablero2_barco, "barco2", 1),
    Barco_npc(tablero2_barco, "barco3", 1),
    Barco_npc(tablero2_barco, "barco4", 1),
    Barco_npc(tablero2_barco, "barco5", 2),
    Barco_npc(tablero2_barco, "barco6", 2),
    Barco_npc(tablero2_barco, "barco7", 2),
    Barco_npc(tablero2_barco, "barco8", 3),
    Barco_npc(tablero2_barco, "barco9", 3),
    Barco_npc(tablero2_barco, "barco10", 4)
]


#10 VARIABLES VIDAS 
vidas1 = 20
vidas2 = 20




