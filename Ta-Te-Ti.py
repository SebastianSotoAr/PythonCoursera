#!/usr/bin/python
# -*- coding: utf-8 -*-
# Juedo Ta-Te-Ti

def Esp(fun):
    def wrap(s, n = 0, p = 0):
        # Hace un reglon con "#".
        if n == 1:
            print("#"*40)

        res = fun(s, n)

        if p == 2:
            print("#"*40)
        return res
        
    return wrap

@Esp
def Tex(str, E = 0, F = 0):
   # Centra los texos entre "#".

   str1 = str.center(len(str) + 2)
   str2 = str1.center(40, "#")
   print(str2)

def Tablero(t1, t2):
   # Hace una fila del tablero
   for fila in range(3):
        strXO = "|".join(t1[fila])
        strN = "|".join(t2[fila])
        strT = "|" + strXO + "| ## |" + strN + "|" 
        Tex(strT)

def XoO():
   # Indica los turnos

    for ronda in range(9):
        if ronda % 2 == 0:
            turno = "X"

        else:
            turno = "O"

        yield turno

def Pos(Num):
   # Escribe en el tablero
   # Resive numeros enter 1 y 9 inclusive

    columna = (Num - 1) % 3
    fila = (Num - 1) // 3
    return [fila, columna]

XoO = XoO()

Tex("-".join(["Ta","Te","Ti"]), 1)
Tex("bienvenidos".title())
Tex("jugador 1".title())
Tex("elija su símbolo".title(), 0, 2)

pl = {"X" : None, "O" : None}
while pl["X"] == None:
   # Revisa la respuesta.

   res = input("Escriba \"X\" ó \"O\": ")

   es_x = (res == "X") or (res == "x")
   es_o = (res == "O") or (res == "o") or (res == "0")

   if es_x:
      pl["X"] = 1
      pl["O"] = 2
   
   elif es_o:
      pl["X"] = 2
      pl["O"] = 1

   else:
        Tex("la respuesta no es valida".title(), 1, 2)

pl_keys = list(pl.keys())
pl_values = list(pl.values())
pl1 = pl_keys[pl_values.index(1)]
pl2 = pl_keys[pl_values.index(2)]

Tex("El Jugador 1: {}".format(pl1), 1)
Tex("El Jugador 2: {}".format(pl2), 0, 2)

TabXO = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
TabN = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

Tablero(TabXO, TabN)

ronda = 0
win = None
Pos_Usadas = []
while (ronda < 9) and (win == None):
    # Decide cuando termina el juego

    ronda += 1
    Turno = XoO.__next__()
    Tex("Es El Turno Del Jugador {}({})".format(pl[Turno], Turno), 1,)
    Tex("elije la casilla".title(), 0, 2)
    
    UnoANueve = ["1","2","3","4","5","6","7","8","9"]
    res2 = 0
    while not (res2 in UnoANueve):
        # Revisa la respuesta

        res2 = input("escribe un numero del 1 al 9 : ".title())
        
        if not (res2 in UnoANueve):
            Tex("la respuesta no valida".title(), 1, 2)

        elif res2 in Pos_Usadas:
            Tex("la casilla esta ocupada".title(), 1, 2)
            res2 = 0
        
        Pos_Usadas.append(res2)
    
    res2 = int(res2)
    print("#"*40)
    TabXO[Pos(res2)[0]][Pos(res2)[1]] = Turno
    Tablero(TabXO, TabN)

    for l in range(3):

        if (TabXO[l][0] == TabXO[l][1]) and (TabXO[l][1] == TabXO[l][2]) and not (TabXO[l][2] == "_"):
            win = pl[Turno]
        
        elif (TabXO[0][l] == TabXO[1][l]) and (TabXO[1][l] == TabXO[2][l]) and not (TabXO[2][l] == "_"):
            win = pl[Turno]

    if TabXO[1][1] == "_":
        pass

    elif (TabXO[0][0] == TabXO[1][1]) and (TabXO[1][1] == TabXO[2][2]):
            win = pl[Turno]
    
    elif (TabXO[2][0] == TabXO[1][1]) and (TabXO[1][1] == TabXO[0][2]):
            win = pl[Turno]

if not(win == None):
    Tex("El Juego A Termina, Gana Jugador {}".format(win), 1, 2)

else:
    Tex("el juego termina en empate".title(), 1, 2)
