from pickle import TRUE
import sqlite3

def Inicio():
    print("\n\nBienvenido a la Base de Datos de la Escuela")

    myConexion = sqlite3.connect("Base de Datos Escuela")

    myCursor = myConexion.cursor()

    try:
        myCursor.execute("""
            CREATE TABLE "CURSOS" (
                "ID"	INTEGER NOT NULL UNIQUE,
                "NOMBRE"	TEXT NOT NULL UNIQUE,
                PRIMARY KEY("ID" AUTOINCREMENT)
            );
        """)

        myCursor.execute("""
            CREATE TABLE "ALUMNOS" (
                "ID"	INTEGER NOT NULL UNIQUE,
                "NOMBRE"	TEXT NOT NULL UNIQUE,
                "ID_CURSO"	INTEGER NOT NULL,
                PRIMARY KEY("ID" AUTOINCREMENT),
                FOREIGN KEY("ID_CURSO") REFERENCES "CURSOS"("ID")
            );
        """)

        myCursor.execute("""
            CREATE TABLE "PROFESORES" (
                "ID"	INTEGER NOT NULL UNIQUE,
                "NOMBRE"	TEXT NOT NULL UNIQUE,
                "ID_CURSO"	INTEGER,
                "HORARIO"	TEXT NOT NULL,
                PRIMARY KEY("ID" AUTOINCREMENT),
                FOREIGN KEY("ID_CURSO") REFERENCES "CURSOS"("ID")
            );
        """)

        print("Se a creado la base de datos")
    except:
        print("Se a cargado la base de datos")

    myConexion.close()

def printMenu():
    print("\tEscriba Para:\n\t\t1. Registrar\n\t\t2. Consultar\n\t\t3. Salir")

    ans = input("Ingresar: ")
    return ans

def salir():
    print("Estas seguro que quieres salir.\n\tEscriba Para:\n\t\t1. Ir atráz\n\t\t2. Salir")
    m = input("Ingresar: ")

    if (m == "1"):
        return True

    else:
        return False

def electorCurso():

    myConexion = sqlite3.connect("Base de Datos Escuela")

    myCursor = myConexion.cursor()

    myCursor.execute(f"""
    SELECT "ID","NOMBRE" FROM "main"."CURSOS";
    """)
    tablaCursos = myCursor.fetchall()
    listaIdCursos = []
  
    myConexion.close()

    for entidad in tablaCursos:
        listaIdCursos.append(entidad[0])

    res = 0

    while not(res in listaIdCursos):
        print("\tElige un Curso:")

        for entidad in tablaCursos:
            print(f"\t\t{entidad[0]}. {entidad[1]}")

        res = int(input("Ingresar: "))

    return res

def electorProfesores():

    myConexion = sqlite3.connect("Base de Datos Escuela")

    myCursor = myConexion.cursor()

    myCursor.execute(f"""
    SELECT "ID","NOMBRE" FROM "main"."PROFESORES";
    """)
    tablaProfes = myCursor.fetchall()
    listaIdProfes = []
  
    myConexion.close()

    for entidad in tablaProfes:
        listaIdProfes.append(entidad[0])

    res = 0

    while not(res in listaIdProfes):
        print("\tElige un Curso:")

        for entidad in tablaProfes:
            print(f"\t\t{entidad[0]}. {entidad[1]}")

        res = int(input("Ingresar: "))

    return res

def consulta():
    print("\tConsultas:\n\t\t1. Alumnos por Curso\n\t\t2. Horario de los Profesores\n\t\t3. Horario de los Cursos\n\t\t4. Atráz")
    men = input("Ingrear: ")
    if (men == "1"):
        curso = electorCurso()

        myConexion = sqlite3.connect("Base de Datos Escuela")

        myCursor = myConexion.cursor()

        myCursor.execute(f"""
        SELECT "ID","NOMBRE" FROM "main"."ALUMNOS" WHERE "ID_CURSO" = {curso};
        """)
        tabla = myCursor.fetchall()
    
        myConexion.close()

        for i in tabla:
            print(f"{i[0]}\t{i[1]}")

    elif (men == "2"):
        profe = electorProfesores()

        myConexion = sqlite3.connect("Base de Datos Escuela")

        myCursor = myConexion.cursor()

        myCursor.execute(f"""
        SELECT "HORARIO" FROM "main"."PROFESORES" WHERE "ID" = {profe};
        """)
        tabla = myCursor.fetchall()
    
        myConexion.close()

        for i in tabla:
            print(f"{i[0]}")

    elif (men == "3"):
        curso = electorCurso()

        myConexion = sqlite3.connect("Base de Datos Escuela")

        myCursor = myConexion.cursor()

        myCursor.execute(f"""
        SELECT "HORARIO","NOMBRE" FROM "main"."PROFESORES" WHERE "ID_CURSO" = {curso};
        """)
        tabla = myCursor.fetchall()
    
        myConexion.close()

        for i in tabla:
            print(f"{i[1]} {i[0]}")

def crearCurso():

    nombre = input("Nombre: ")

    myConexion = sqlite3.connect("Base de Datos Escuela")

    myCursor = myConexion.cursor()

    myCursor.execute(f"""
    INSERT INTO "main"."CURSOS"
    ("NOMBRE")
    VALUES ('{nombre}');
    """)

    myConexion.commit()

    myConexion.close()

def haceHorario():
    textoFinal = ""
    n = 0
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    print("El horario de profesor es:")
    print("\tEl dia:")
    for i in range(0, 7):
        print(f"\t\t{i+1}. {dias[i]}")
    
    try:
        n = int(input("Ingresar: "))
    except:
        n = 0

    while not(n in range(1, 8)):
        try:
            n = int(input("Eliga un dia: "))
        except:
            n = 0

    textoFinal += f"{dias[n-1]} en el horario de "

    print("\tEn el horario de:")

    n = 1

    try:
        n = int(input("Ingresar(6 a 18): "))
    except:
        n = 1

    while not(n in range(6, 19)):
        try:
            n = int(input("Elige una hora(6 a 18): "))
        except:
            n = 1

    textoFinal += f"{n} a "

    print("\tA")

    n = 1

    try:
        n = int(input("Ingresar(6 a 18): "))
    except:
        n = 1

    while not(n in range(6, 19)):
        try:
            n = int(input("Elige una hora(6 a 18): "))
        except:
            n = 1

    textoFinal += f"{n}"

    return textoFinal

def crearProfesor():

    nombre = input("Nombre: ")
    curso = electorCurso()
    horario = haceHorario()

    myConexion = sqlite3.connect("Base de Datos Escuela")

    myCursor = myConexion.cursor()

    myCursor.execute(f"""
    INSERT INTO "main"."PROFESORES"
    ("NOMBRE", "ID_CURSO", "HORARIO")
    VALUES ('{nombre}', '{curso}', '{horario}');
    """)

    myConexion.commit()

    myConexion.close()

def crearAlumno():

    myConexion = sqlite3.connect("Base de Datos Escuela")

    myCursor = myConexion.cursor()

    nombre = input("Nombre: ")
    curso = electorCurso()

    myCursor.execute(f"""
    INSERT INTO "main"."ALUMNOS"
    ("NOMBRE", "ID_CURSO")
    VALUES ('{nombre}', '{curso}');
    """)

    myConexion.commit()

    myConexion.close()

def eleccionRegistro():

    myConexion = sqlite3.connect("Base de Datos Escuela")

    myCursor = myConexion.cursor()

    myCursor.execute(f"""
    SELECT "ID" FROM "main"."CURSOS";
    """)
    NumeroCursos = len(myCursor.fetchall())
    
    myConexion.close()

    print("\tEscriba Para Agregar un:\n\t\t1. Curso")

    if (NumeroCursos != 0):
        print("\t\t2. Profesor\n\t\t3. Alumno")
        
    print("\t\t4. Atráz")

    m = input("Ingresar: ")

    if (m == "1"):
        crearCurso()

    elif ((m == "2")and((NumeroCursos != 0))):
        crearProfesor()

    elif ((m == "3")and((NumeroCursos != 0))):
        crearAlumno()



Inicio()

s = True
while s:
    n = printMenu()

    if (n == "1"):
        eleccionRegistro()

    elif(n == "2"):
        consulta()
    
    else:
        s = salir()
