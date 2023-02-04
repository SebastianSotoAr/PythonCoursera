import sqlite3

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
    print("\tConsultas:\n\t\t1. Alumnos por Curso\n\t\t2. Horario de los Profesores\n\t\t3. Horario de los Cursos")
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
        SELECT "HORARIO" FROM "main"."PROFESORES" WHERE "ID_CURSO" = {curso};
        """)
        tabla = myCursor.fetchall()
    
        myConexion.close()

        for i in tabla:
            print(f"{i[0]}")

consulta()
