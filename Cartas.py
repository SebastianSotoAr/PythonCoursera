from random import choice
from time import sleep

num = ["Q", "8", "J"]
pin = {"Q" : "♥", "8" : "♣", "J" : "♦"}
pos = ["I", "M", "D"]
pal = {"I" : "izquierda", "M" : "la del medio", "D" : "derecha"}

def choice_sin_remplazo(ans,k):
    lista = []
    for i in range(k):
        n = choice(ans)
        ans.remove(n)
        lista.append(n)

    return lista

def revuelve(dic):
    sleep(choice([1, 2, 3]))
    lista = choice_sin_remplazo(["I", "M", "D"],2)
    print(f"Intercambio {pal[lista[0]]} ({lista[0]}) con {pal[lista[1]]} ({lista[1]})...")
    a=dic[lista[0]]
    dic[lista[0]]=dic[lista[1]]
    dic[lista[1]]=a

    return dic

def pinta_cartas(dic):
    print(f' ___   ___   ___\n|{dic["I"]}  | |{dic["M"]}  | |{dic["D"]}  |\n| {pin[dic["I"]]} | | {pin[dic["M"]]} | | {pin[dic["D"]]} |\n|__{dic["I"]}| |__{dic["M"]}| |__{dic["D"]}|')

def juego():
    l = choice_sin_remplazo(num,3)

    pipo = {"I" : l[0], "M" : l[1], "D" : l[2]}

    pinta_cartas(pipo)
    N = input('Presiona Enter cuando estés listo(a)')

    for i in range(choice([5, 6, 7, 8, 9, 10])):
        pipo = revuelve(pipo)

    respuesta = input("¿En cuál de las cartas esta la reina de corazones? [I], [M], [D]: ")
    if pipo[respuesta] == "Q":
        pinta_cartas(pipo)
        print("¡Ganaste sumas 5 puntos a tu historial!")
        return True

    else:
        pinta_cartas(pipo)
        print("Perdiste, mas suerte para la proxima.")
        return False

print(juego())