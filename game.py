import world
import os
import random


def move(w_map, emoj_player, x_player, y_player):
    direzione = input("Dove vuoi andare? (w, a, s, d): ")

    #controllo della direzione
    while direzione not in ['w', 'a', 's', 'd']:
        print("Direzione non valida. Riprova.")
        direzione = input("Dove vuoi andare? (w, a, s, d): ")
        

    match direzione:
        case 'w':
            w_map[x_player][y_player] = '🧱'
            x_player -= 1

            #controllo fuori mappa
            while controllo_fuori_dalla_mappa(w_map, x_player, y_player):
                print("Fuori mappa. Riprova.")
                return move(w_map, emoj_player, x_player + 1, y_player)
            
            w_map[x_player][y_player] = emoj_player
        case 'a':
            w_map[x_player][y_player] = '🧱'
            y_player -= 1

            #controllo fuori mappa
            while controllo_fuori_dalla_mappa(w_map, x_player, y_player):
                print("Fuori mappa. Riprova.")
                return move(w_map, emoj_player, x_player, y_player + 1)
            
            w_map[x_player][y_player] = emoj_player
        case 's':
            w_map[x_player][y_player] = '🧱'
            x_player += 1

            #controllo fuori mappa
            while controllo_fuori_dalla_mappa(w_map, x_player, y_player):
                print("Fuori mappa. Riprova.")
                return move(w_map, emoj_player, x_player - 1, y_player)
            
            w_map[x_player][y_player] = emoj_player
        case 'd':
            w_map[x_player][y_player] = '🧱'
            y_player += 1

            #controllo fuori mappa
            while controllo_fuori_dalla_mappa(w_map, x_player, y_player):
                print("Fuori mappa. Riprova.")
                return move(w_map, emoj_player, x_player, y_player - 1)
            
            w_map[x_player][y_player] = emoj_player
            
    return w_map

def display(w_map):
    righe = len(w_map)
    colonne = len(w_map[0])
    #stampa del display
    for i in range(righe):
        for j in range(colonne):
            print(w_map[i][j], end=" ")
        print("\n")

def start_player(w_map, x_player, y_player, e_p):
    w_map[x_player][y_player] = e_p

def trova_player(w_map):
    pos = []
    for i in range(len(w_map)):
        for j in range(len(w_map[0])):
            if w_map[i][j] == '👨':
                pos = [i, j]
                return pos
        
def controllo_fuori_dalla_mappa(w_map, x_player, y_player)-> bool:
    limite_x = len(w_map)
    limite_y = len(w_map[0])

    if x_player < 0 or x_player >= limite_x:
        return True
    if y_player < 0 or y_player >= limite_y:
        return True
    return False


def game():

    os.system('clear')

    Vittoria = True

    emoj_player = '👨'
    emoj_monster = '👹'


    #matrice di dimensione random per il mondo (min di caselle 3 X 3)
    righe = random.randint(3,6)
    colonne = random.randint(3,6)
    w_map = [["🧱" for x in range(colonne)] for y in range(righe)]

    #posizione del giocatore
    x_player = random.randint(0, righe-1)
    y_player = random.randint(0, colonne-1)

    start_player(w_map, x_player, y_player, emoj_player)

    print("Benvenuto nel Gioco\n\n\nSpawn iniziale\n\n")

    display(w_map) 

    #inizio del gioco
    while Vittoria:
        os.system('clear')
        display(move(w_map, emoj_player, x_player, y_player))

        #aggiornare la posizione del giocatore
        posizione_player = trova_player(w_map)
        x_player = posizione_player[0]
        y_player = posizione_player[1]


#Gioco effettivo


game()

