#!/usr/bin/python
# -*- coding: utf-8 -*-
# Caja Registradora
# By Sebástian Soto Arcila

import unittest

class CajaRegistradora:

    def __init__(self):

        self.nombres = {"001":"Manzana", "002":"Banana", "003":"Kiwi", "004":"Pera",
        "005":"Melon", "006":"Mango", "007":"Papaya"}
        self.valores = {"001":3.5, "002":4.5, "003":6, "004":3.75, "005":5.75,
        "006":5, "007":6.5}
        self.codigos = ["00" + str(x) for x in range(1, len(self.nombres)+1)]
        self.descuentos = {"001":0.05, "002":0.025, "003":0, "004":0.02, "005":0.05,
        "006":0.1, "007":0.05}
        self.codigos_compra = []
        self.cantidad_compra = []
        self.cierre = True

    def escaner(self):

        self.codigo = input("Ingrese el código del producto: ")
        
        while not self.codigo in self.codigos:

            self.codigo = input("Ningun producto tiene ese código, intente de nuevo: ")
        
        self.codigos_compra.append(self.codigo)

    def cierre_escaner(self):
        
        self.cierre = True
        self.si_cierra = input("Solo escriba x si va a terminar la compra: ")

        while (self.si_cierra == "x") or (self.si_cierra == "X"):

            self.cierre = False

            self.si_cierra = ""

    def calcula_descuentos(self, codigo_descuento):

        return (self.valores[codigo_descuento]- self.valores[codigo_descuento]*
        self.descuentos[codigo_descuento])     

    def calcula_subtotal(self):
        
        self.subtotal = 0
        self.n = 0

        for x in self.codigos_compra:

            self.subtotal += self.calcula_descuentos(x)*self.cantidad_compra[self.n]
            self.n += 1

        return self.subtotal

    def calcula_devuelta(self, subtotal_devuelta):

        self.a_devolver = "str"

        while self.a_devolver != float:
            
            try:
                self.a_devolver = float(input("Ingrese la cantidad de dinero que le dio el cliente: "))

                while self.a_devolver < subtotal_devuelta:

                    self.a_devolver = float(input("El valor a pagar es mayor, vuelva a intentar: "))

                return self.a_devolver - subtotal_devuelta

            except ValueError:

                print("Debe ingresar números...")

    def pide_cantidad(self):

        self.cantidad = "str"

        while self.cantidad != int:
            
            try:
                self.cantidad = int(input("Número de unidades: "))

                while self.cantidad <= 0:

                    self.cantidad = int(input("No es válido, vuelva a intentar: "))

                return self.cantidad

            except ValueError:

                print("Debe ingresar números...")

    def guarda_cantidad(self):

        self.cantidad_compra.append(self.pide_cantidad())

    def tablero_inicial(self):

        print()
        print("Bienvenido a la tienda".center(52))
        print()
        print("Estos son los productos disponibles".center(52))
        print("\nCódigo   Nombre   Valor   Descuento   Valor con Desc")
        
        for w in self.codigos:

            ti1 = w.ljust(8)
            ti2 = self.nombres[w].ljust(8)
            ti3 = str(self.valores[w]).ljust(7)
            ti4 = str(self.descuentos[w]).ljust(11)
            ti5 = str(self.calcula_descuentos(w)).ljust(16)

            print(ti1, ti2, ti3, ti4, ti5)

        print()

    def tablero_compra(self):

        self.escaner()
        self.guarda_cantidad()

        print()
        print("Estos son los productos registrados".center(63))
        print("\nCódigo   Nombre   Valor   Descuento   Valor con Desc   Cantidad")
        
        i = 0

        for w in self.codigos_compra:

            tc1 = w.ljust(8)
            tc2 = self.nombres[w].ljust(8)
            tc3 = str(self.valores[w]).ljust(7)
            tc4 = str(self.descuentos[w]).ljust(11)
            tc5 = str(self.calcula_descuentos(w)).ljust(16)
            tc6 = str(self.cantidad_compra[i])
            i += 1

            print(tc1, tc2, tc3, tc4, tc5, tc6)

        print()
        print(("El subtotal es: " + str(self.calcula_subtotal())).center(63))
        print()

    def caja_on(self):

        self.tablero_inicial()

        while self.cierre:
            self.tablero_compra()
            self.cierre_escaner()

        print()
        print("Ha terminado la compra".center(63))
        print()
        print("\n" + ("Debe devolver: " + str(self.calcula_devuelta(self.subtotal))).center(63))
        print()
        print("Gracias por su compra".center(63))
        print()

prueba = CajaRegistradora()
prueba.caja_on()

# *******Inicio de Test*******

class Test(unittest.TestCase):

    def setUp(self):

        self.recibo = CajaRegistradora()

    def test_init(self):

        result = self.recibo.nombres["001"]
        self.assertEqual(result, "Manzana")

        result = self.recibo.valores["001"]
        self.assertEqual(result, 3.5)

        result = self.recibo.descuentos["001"]
        self.assertEqual(result, 0.05)

        result = self.recibo.nombres["007"]
        self.assertEqual(result, "Papaya")

        result = self.recibo.valores["004"]
        self.assertEqual(result, 3.75)

        result = self.recibo.descuentos["005"]
        self.assertEqual(result, 0.05)

    def test_escaner(self):

        print("**Escribe 001 (Para testear escaner)**")
        self.recibo.escaner()
        result = self.recibo.codigos_compra
        self.assertEqual(result, ["001"])

        print("**Escribe 004 (Para testear escaner)**")
        self.recibo.escaner()
        result = self.recibo.codigos_compra
        self.assertEqual(result, ["001", "004"])

        print("**Escribe 006 (Para testear escaner)**")
        self.recibo.escaner()
        result = self.recibo.codigos_compra
        self.assertEqual(result, ["001", "004", "006"])

        print("**Escribe 008 (Para testear escaner)**\n**Luego, Escribe 003**")
        self.recibo.escaner()
        result = self.recibo.codigos_compra
        self.assertEqual(result, ["001", "004", "006", "003"])

    def test_calcula_descuentos(self):

        result = self.recibo.calcula_descuentos("001")
        self.assertEqual(result, 3.325)

        result = self.recibo.calcula_descuentos("002")
        self.assertEqual(result, 4.3875)

        result = self.recibo.calcula_descuentos("003")
        self.assertEqual(result, 6)

    def test_calcula_subtotal(self):

        self.recibo.codigos_compra = ["001", "004", "006", "003"]
        self.recibo.cantidad_compra = [1, 1, 1, 1]
        result = self.recibo.calcula_subtotal()
        self.assertEqual(result, 17.5)

        self.recibo.codigos_compra = ["001", "002", "003", "004"]
        self.recibo.cantidad_compra = [2, 2, 2, 2]
        result = self.recibo.calcula_subtotal()
        self.assertEqual(result, 34.775)

        self.recibo.codigos_compra = ["004", "005", "006", "007"]
        self.recibo.cantidad_compra = [4, 4, 4, 4]
        result = self.recibo.calcula_subtotal()
        self.assertEqual(result, 79.25)

    def test_calcula_devuelta(self):

        print("**Escribe 200 (Para testear calcula_devuelta)**")
        result = self.recibo.calcula_devuelta(100)
        self.assertEqual(result, 100)

        print("**Escribe 200 (Para testear calcula_devuelta)**\n**Luego, escribe 600**")
        result = self.recibo.calcula_devuelta(300)
        self.assertEqual(result, 300)

        print("**Escribe pera (Para testear calcula_devuelta)**\n**Luego, escribe 100**")
        result = self.recibo.calcula_devuelta(70)
        self.assertEqual(result, 30)

    def test_pide_cantidad(self):

        print("**Escribe pepe (Para testear pide_cantidad)**\n**Luego, escribe 2**")
        result = self.recibo.pide_cantidad()
        self.assertEqual(result, 2)

    def test_guarda_cantidad(self):
        
        print("**Escribe 2 (Para testear guarda_cantidad)**")
        self.recibo.guarda_cantidad()
        result = self.recibo.cantidad_compra
        self.assertEqual([2], result)

        print("**Escribe 3 (Para testear guarda_cantidad)**")
        self.recibo.guarda_cantidad()
        result = self.recibo.cantidad_compra
        self.assertEqual([2, 3], result)

        print("**Escribe 4 (Para testear guarda_cantidad)**")
        self.recibo.guarda_cantidad()
        result = self.recibo.cantidad_compra
        self.assertEqual([2, 3, 4], result)

    def test_cierre(self):

        print("**Preciona X (Para testear cierra_escaner)")
        self.recibo.cierre_escaner()
        result = self.recibo.cierre
        self.assertEqual(result, False)

        print("**Preciona enter (Para testear cierra_escaner)")
        self.recibo.cierre_escaner()
        result = self.recibo.cierre
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()