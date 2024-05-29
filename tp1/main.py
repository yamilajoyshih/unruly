import random

import niveles
import unruly

VACIO= " "
UNO= "1"
CERO= "0"


def grafico_visual(grilla):
    grilla_alineada=[]
    for fila in grilla:
        fila_str="".join(str(valor_de_la_celda) for valor_de_la_celda in fila)
        fin_de_fila= "|" + fila_str + "|"
        grilla_alineada.append(fin_de_fila)

    return "\n".join(grilla_alineada)

def pedir_valor_a_usuario(grilla):
    filas, columnas = unruly.dimensiones(grilla)
    while True:
        columna= input("ingrese columna:")
        if not columna.isdigit() or int(columna)> columnas:
            continue
        
        columna=int(columna)
            
        fila= (input("ingrese fila:"))
        if not fila.isdigit() or int(fila)> filas:
            continue
        
        fila=int(fila)

        valor_del_usuario= (input("ingrese 0 o 1 o VACIO: "))
        if valor_del_usuario not in [CERO,UNO,VACIO]:
            continue

        return fila, columna, valor_del_usuario


def main():
    nivel = random.choice(niveles.NIVELES)
    grilla = unruly.crear_grilla(nivel)
    while not unruly.grilla_terminada(grilla):
        fila, columna, valor_del_usuario= pedir_valor_a_usuario(grilla)
        grilla[fila][columna]= valor_del_usuario
        if valor_del_usuario== 0:
            unruly.cambiar_a_cero(grilla, columna, fila)
        if valor_del_usuario== 1:
            unruly.cambiar_a_uno(grilla, columna, fila)
        if valor_del_usuario== VACIO:
            unruly.cambiar_a_vacio(grilla, columna, fila)
        print(grafico_visual(grilla))
        if unruly.grilla_terminada(grilla):
            print("Felicitaciones, has ganado :) ")
            return

        salir_del_juego=(input("si desea salir del juego, ingrese stop: "))
        if salir_del_juego.lower()=="stop":
            return

main()

    
        
     
     




