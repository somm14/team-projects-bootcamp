import pandas as pd
import sqlite3
from queries import*

def bienvenida():
    print('''Bienvenido detective a esta investigación.\n
          Ha ocurrido un crimen y el detective necesita tu ayuda.\n 
          El detective te dio el informe de la escena del crimen, pero de alguna manera lo perdiste.\n
          Recuerdas vagamente que el crimen fue un ​asesinato​ que ocurrió en algún momento del ​15 de enero de 2018​ y que tuvo lugar en ​SQL City​.\n 
          Comience recuperando el informe de la escena del crimen correspondiente de la base de datos del departamento de policía.''')

def pistas_1():
    print('''Pistas:\n
          - Crimen: asesinato
          - Fecha: 15 de enero del 2018
          - Lugar: SQL City
''')
    
# Conectamos con la base de datos chinook.db
conn = sqlite3.connect("./data/sql-murder-mystery.db")

# Obtenemos un cursor que utilizaremos para hacer las queries
cursor = conn.cursor()

#Informe
def informe():
    informe = pd.read_sql(query1, conn)
    print("Imforme del crimen:")
    for lineas in informe["description"]:
        print(lineas)

def pistas_2():
    print('''\nSiguientes pistas:\n
          - Primer testigo: Vive en la última casa de Northwestern Dr
          - Segundo testigo: Se llama Annabel y viven en algún lugar de Franklin Ave
''')

#Testimonio del testigo 1
def testigo_1():
    df_testimonio_1 = pd.read_sql(query2, conn)
    numero = df_testimonio_1["address_number"].max() #Buscamos la última casa
    df_testigo1_num = df_testimonio_1[df_testimonio_1["address_number"] == numero]
    df_testigo_1 = df_testigo1_num[["name", "transcript", "address_number"]]
    testimonio = df_testigo_1["transcript"]
    for linea in testimonio:
        testimonio_1 = linea
        print("Testimonio del primer testigo:\n")
        print(f"\t{testimonio_1.replace(".", "\n")}")

def mensaje():
    print('''\n
Una vez conocido el testimonio del primer testigo, 
vamos a ver el testimonio del segundo testigo.

Después recopilamos las pistas
''')

# Testimonio del testigo 2

def testigo_2():
    df_testigo_2 = pd.read_sql(query3, conn)
    testimonio2 = df_testigo_2["transcript"]
    for linea in testimonio2:
        testimonio_2 = linea
        print("\nTestimonio del segundo testigo:\n")
        print(f"\t{testimonio_2.replace(",", "\n")}")

def pistas_3():
       print('''\nSiguientes pistas:\n
          - El presunto asesino está en el gimnasio 'GET FIT NOW', 
             es miembro GOLD, y su número de miembro comienza por '48Z'
          - Además, se subió a un coche cuya matrícula incluía 'H42W'.
          - El presunto asesino estuvo ahí el 9 de enero.
''')

# Posibles asesinos
def buscando_asesino():
    posibles_asesinos = pd.read_sql(query4, conn)
    print(f'''\n
Las personas que son GOLD
y cuyo código de miembro comienza por '48Z' son:''')
    print("\n",posibles_asesinos["name"][0])
    print(posibles_asesinos["name"][1])

def posible_asesino():
    asesino = pd.read_sql(query5, conn)
    print("\nInvestigando la matrícula, descubrimos que el presunto asesino es:")
    print(f"\n{asesino["name"][1]}")

def verificacion_1():
    print('''\n
La verificación en la solución es la sigiente:
          "Congrats, you found the murderer! 
          But wait, there's more... If you think you're up for a challenge, try querying the interview transcript of the murderer to find the real villain behind this crime. 
          If you feel especially confident in your SQL skills, try to complete this final step with no more than 2 queries. 
          Use this same INSERT statement with your new suspect to check your answer."
    ''')

def pistas_4():
    print('''\n
    Al comprobar la verificación, nos cuenta que hay un asunto más.
    Nos piden ver la declaración del asesino
    ''')

def testimonio_asesino():
    testimonio_asesino = pd.read_sql(query6, conn)
    entrevista_asesino = testimonio_asesino["transcript"]
    for linea in entrevista_asesino:
        entrevista = linea
        print("\n",entrevista.replace(".", "\n"))

def pistas_5():
    print('''\n
Siguientes pistas:
          - Mujer con una altura de 5'5" o 5'7".
          - Tiene el pelo rojo y conduce un Tesla Model S.
          - Además, asistió 3 veces al SQL Symphony Concert
''')

def asesina():
    asesina = pd.read_sql(query9, conn)
    nombre_asesina = asesina["name"][0]
    print("\nEl nombre de la mujer que contrató a Jeremy:")
    print(nombre_asesina)

def verificacion_2():
    print('''
Congrats, you found the brains behind the murder! 
Everyone in SQL City hails you as the greatest SQL detective of all time. 
Time to break out the champagne!
''')