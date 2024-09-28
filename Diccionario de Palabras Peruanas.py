buscador = input("¿Con que palabra tienes duda?")
diccionario = {"Palta": "Relacionado a algo embarazoso", "Causa": "Amigo o amiga", "Pe": "Abreviación de la palabra 'pues', "Chamba": }
if buscador in diccionario:
    print(diccionario[buscador])
else:
    print("Perdone, seguimos buscando el significado a la palabra.")
