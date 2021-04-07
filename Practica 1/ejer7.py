
nombre = """"'Agustin',
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

nombreLista = nombre.strip().replace(",","").replace("\","")
nombresLista = nombreLista.splitlines()
nombres1 = list(map(lambda x  : x.strip(), nombresLista)) 




eval1Lista = eval1.strip().replace(",","").splitlines()
eval1ListaFinal = [int(nota) for nota in eval1Lista]

eval2Lista = eval2.strip().replace(",","").splitlines()
eval2ListaFinal = [int(nota) for nota in eval2Lista]

ambas_notas = list(zip(nombres1,eval1ListaFinal,eval2ListaFinal))
notasFinales = list(zip(eval1ListaFinal,eval2ListaFinal))

listaNotasFinales = list()
for n in notasFinales:
    listaNotasFinales.append(sum(n)) 

Estudiantes_notas = list(zip(nombres1,listaNotasFinales))

#print (Estudiantes_notas)

notasPromedio = list(map(lambda x: x / 2 , listaNotasFinales))
#print (notasPromedio)
cantidad =  sum(notasPromedio) / len(notasPromedio)
#print (cantidad)

Estudiantes_notas_promedio = list(zip(nombres1,notasPromedio))
Lista_Satisface = list()
for i in Estudiantes_notas_promedio:
    if i[1] >= cantidad:
        Lista_Satisface.append(i)


print ("Los estudiantes tienen estas notas {} \n".format(ambas_notas))
print ("La suma de las notas {}\n".format(Estudiantes_notas))
print("Los alumnos que estan arriba del promedio son {}\n".format(Lista_Satisface))
