#Tarea3 Ciclos
def caracteres_pares(frase):
    posicion_caracter = 0

    for letra in frase:
        if posicion_caracter%2 == 0: 
            print(letra)
        posicion_caracter = posicion_caracter + 1

caracteres_pares('supercalifragilisticoespiralidoso')


