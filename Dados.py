def Dados():
    # Devuelve dos numeros aleatorios entre 1 y 6 inclusive, y 
    # su suma.

    from random import choice

    nl = [1, 2, 3, 4, 5, 6]
    d1 = choice(nl)
    d2 = choice(nl)
    
    print("Se tiran los dados, su resultado es:")
    print("Dado 1:", d1)
    print("Dado 2:", d2)
    print("La suma de los dados es:", (d1 + d2))

print("¡Bienvenido!")

Dados()

nval = True

while nval:
    #Revisa la respuesta del usuario.

    print("¿Desea tirar los dados nuevamente?")

    res = input("Responda si o no: ")

    si = (res == "SI" or res == "Si" or res == "sI" or res == "si")
    no = (res == "NO" or res == "No" or res == "nO" or res == "no")

    if si:
        Dados()

    elif no:
        nval = False

    else:
        print("Respuesta no válida.")
        res = input("Responda si o no:")
    

print("¡Adiós, vuelva pronto!")
