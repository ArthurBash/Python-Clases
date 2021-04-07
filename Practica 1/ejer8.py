nombre1 = """ 'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina' """
nombre2 = """'Agustin',
 'AGUSTIN',
 'Agustín',
 'Ailen',
 'Alfredo',
 'Amalia',
 'Ariana',
 'Bautista',
 'Braian',
 'Carla',
 'CESAR',
 'Daniel',
 'Diego',
 'ELIANA',
 'Facundo',
 'Facundo',
 'Facundo',
 'Facundo',
 'Federico',
 'Federico',
 'Flavia',
 'Francisco',
 'Germán',
 'Guido',
 'GUSTAVO',
 'Hilario',
 'Ignacio',
 'IVAN',
 'Jimmy',
 'Joaquín',
 'Jose',
 'Josue',
 'JUAN',
 'Juan',
 'Laura',
 'LAURA',
 'Lautaro',
 'Lautaro',
 'Ludmila',
 'Marcos',
 'Marcos',
 'MARIANELA',
 'MARTIN',
 'MATEO',
 'Mateo',
 'Matias',
 'MAURO',
 'Maximiliano',
 'NESTOR',
 'Nicolas',
 'Pedro',
 'Ramiro',
 'Sofía',
 'Tobias',
 'Tomás',
 'Tomás',
 'Ulises',
 'Yanina'"""
eval1 = """81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74"""
eval2 ="""30, 
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10 """
nuevo_nombre1 = nombre1.replace(",","").replace("\"","")
lista_nombre1 = nuevo_nombre1.splitlines()
lista_nombre1 = list(map(lambda x: x.strip(),lista_nombre1))

nuevo_nombre2 = nombre2.replace(",","").replace("\"","")
lista_nombre2 = nuevo_nombre2.splitlines()
lista_nombre2 = list(map(lambda x: x.strip(),lista_nombre2))

eval1_list = eval1.replace(",","").splitlines()
eval1_list = [int(x) for x in eval1_list]


eval2_list = eval2.replace(",","").splitlines()
eval2_list = [int(x) for x in eval2_list]

#print (eval1_list)

#Punto 1
lista_repetidos =  [x for x in lista_nombre1 if x in lista_nombre2]
#print(lista_repetidos)

#Punto 2
Lista_nombres_notas = list(zip(lista_nombre1,eval1_list,eval2_list))
lista_notas = (list(zip(eval1_list,eval2_list)))
lista_notas_totales = list()
for x in lista_notas:
    lista_notas_totales.append(sum(x))


print("{4}{0:10s}{4} {4}{1:5s}{4} {4}{2:5s}{4} {4}{3:5s}{4} \n".format("Nombre","Nota1","Nota2","Total", "|"))

cant = 0
for cd in Lista_nombres_notas:
    print("{4}{0:10s}{4}   {4}{1:2d}{4}   {4}{2:2d}{4}  {4}{3:3d}{4} ".format(cd[0],cd[1],cd[2],lista_notas_totales[cant], "|"))
    cant += 1
