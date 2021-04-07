"""Dada una frase y un string ingresados por teclado (en ese orden), e informe la cantidad de
veces que se encuentra el strng en la frase. No distingir entre mayúsculas y minúsculas."""
sentances = input("Ingrese la frase que desee ").lower().split()
word = input("Ingrese la palabra a buscar ").lower()
cant = 0
condicion = True
palabra = list()
while condicion:
    for i in sentances:
        if i.count(word) >= 1:
            cant  = cant + 1
            palabra.append(i)
    if cant == 0:
        print("No se encontraron palabra con la cadena de caracteres {} ".format(word))
    else:
        print("La cantidad de palabras encontradas con la letra {} son {}    y las palabras son {} ".format(word,cant,palabra))
    var3 = input ("Desea seguir s/n").lower()
    if (var3 == 'n'):
        condicion = False
    else:
        cant = 0
        palabra.clear()
        var1 = input("Desea cambiar la frase, ingrese Y/y para aceptar ").lower()
        if (var1 == 'y'):
            sentances = input ("ingrese la frase ")
        word = input("Ingrese la letra/palabra a buscar en el texto  ").lower()
    
