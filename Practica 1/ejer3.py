texto = """Una playa es un accidente geográfico junto a una masa de agua que consta de partículas sueltas. Las partículas que componen una playa suelen estar hechas de roca, como arena, grava, guijarros, guijarros, etc., o de fuentes biológicas, como conchas de moluscos o algas coralinas. Los sedimentos se depositan en diferentes densidades y estructuras, dependiendo de la acción del oleaje local y el clima, creando diferentes texturas, colores y gradientes o capas de material.

Aunque algunas playas se forman en lugares de agua dulce, la mayoría de las playas se encuentran en áreas costeras donde la acción de las olas o de las corrientes marinas deposita y repasa los sedimentos. La erosión costera y el cambio de las geologías de las playas se producen a través de procesos naturales, como la acción de las olas y los fenómenos meteorológicos extremos. Donde las condiciones del viento son adecuadas, las playas pueden estar respaldadas por dunas costeras que ofrecen protección y regeneración para la playa. Sin embargo, estas fuerzas naturales se han vuelto más extremas debido al cambio climático, alterando permanentemente las playas a un ritmo muy rápido. Algunas estimaciones describen que hasta el 50 por ciento de las playas arenosas de la tierra desaparecerán para el 2100 debido al aumento del nivel del mar impulsado por el cambio climático.1​

Las playas de arena ocupan alrededor de un tercio de las costas del mundo.1​ Estas playas son populares para la recreación, desempeñando importantes funciones sociales, económicas y culturales, a menudo impulsando las industrias turísticas locales. Para apoyar estos usos, algunas playas cuentan con infraestructuras artificiales, como puestos de salvavidas, vestuarios, duchas, chozas y bares. También pueden tener lugares de hospitalidad (como resorts, campamentos, hoteles y restaurantes) cercanos o viviendas, tanto para residentes permanentes como de temporada.

Las playas a nivel mundial sufren impactos directos e indirectos de la acción humana. Los impactos directos incluyen malas prácticas de construcción en dunas y costas, mientras que los impactos humanos indirectos incluyen contaminación del agua, contaminación plástica y erosión costera por el aumento del nivel del mar y el cambio climático. Algunas prácticas de gestión costera están diseñadas para preservar o restaurar los procesos naturales de las playas, mientras que algunas playas se restauran activamente a través de prácticas como la nutrición de las playas.


Basura en una playa de Hawái.
Las playas salvajes, también conocidas como playas prístinas, playas sin desarrollar o sin descubrir, son playas que no se desarrollan para el turismo o la recreación. Estas playas preservadas son ecosistemas que cumplen funciones importantes para mantener la biodiversidad acuática o marina, como lugares de reproducción de tortugas marinas o áreas de anidación de aves marinas o pingüinos. Las playas preservadas y sus dunas asociadas son importantes para la protección contra el clima extremo para los ecosistemas del interior y la infraestructura humana."""


textoVar = texto.lower().split()
letra = str(input("Ingrese con la letra que comienza  "))
palabras = list()
condicion = True
while condicion: 
    for p in textoVar:
        if p.startswith(letra):
            palabras.append(p)
    if (len(palabras) == 0):
        print("No hay palabras con {}".format(letra))
    else:
        print ("Las palabras con la letra {} son {} ".format(letra,palabras))
    print("")
    var1 = str(input("Ingrese 's/S' si quiere buscar por otra letra " )).lower()
    if (var1.lower() == 's'):
        letra = str(input("Ingrese la letra a buscar  "))
        palabras.clear()
    else:
        condicion = False

    

    

