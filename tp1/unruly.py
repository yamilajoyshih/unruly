# -*- coding: utf-8 -*-
"""Lógica del juego Unruly"""
from typing import List, Tuple, Any

Grilla = Any
#constantes globales 
UNO= "1"
CERO= "0"
VACIO= " "


def crear_grilla(desc: List[str])-> Grilla: 
    filas= len(desc) 
    columnas= len(desc[0]) 
    grilla=[] 
    for fila in range (filas):
        fila_nueva=([])
        for columna in range (columnas):
            valor_de_la_celda=desc[fila][columna]
            fila_nueva.append(valor_de_la_celda)
        grilla.append(fila_nueva)
    for fila in grilla:
        print("".join(fila))
    return grilla
    
"""Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Se puede asumir que la cantidad de las
    filas y columnas son múltiplo de dos. **No** se puede asumir que la
    cantidad de filas y columnas son las mismas.
    Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
         ' '  Vacío
         '1'  Casillero ocupado por un 1
         '0'  Casillero ocupado por un 0

    Ejemplo:

    >>> crear_grilla([
        '  1 1 ',
        '  1   ',
        ' 1  1 ',
        '  1  0',
    ])
    """



def dimensiones(grilla: Grilla) -> Tuple[int, int]:
    """Devuelve la cantidad de columnas y la cantidad de filas de la grilla
    respectivamente (ancho, alto)"""
    alto= len(grilla)
    ancho=len(grilla[0])
    return ancho, alto

def posicion_es_vacia(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está vacía"""
    return grilla[fil][col] == VACIO


def posicion_hay_uno(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está el valor 1"""
    return grilla[fil][col]== UNO


def posicion_hay_cero(grilla: Grilla, col: int, fil: int) -> bool:
    """Devuelve un booleano indicando si la posición de la grilla dada por las
    coordenadas `col` y `fil` está el valor 0"""
    return grilla [fil][col] == CERO


def cambiar_a_uno(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, colocando el valor 1 en la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    grilla[fil][col]= UNO


def cambiar_a_cero(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, colocando el valor 0 en la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    grilla[fil][col]= CERO



def cambiar_a_vacio(grilla: Grilla, col: int, fil: int):
    """Modifica la grilla, eliminando el valor de la posición de la grilla
    dada por las coordenadas `col` y `fil`"""
    grilla[fil][col]= VACIO

def es_valida(valor_de_la_celda) -> bool:
    """Devuelve un booleano indicando si la lista de valores cumple las tres condiciones para ser considerada valida """
    if VACIO in valor_de_la_celda:
        return False
    suma_de_unos = sum(1 for valor in valor_de_la_celda if valor == UNO )
    suma_de_ceros = sum (1 for valor in valor_de_la_celda if valor == CERO)
    if suma_de_unos != suma_de_ceros:
        return False
    for i in range (len(valor_de_la_celda)-2):
        if valor_de_la_celda[i] == valor_de_la_celda[i+1] == valor_de_la_celda [i+2]:
            return False
    return True 

def fila_es_valida(grilla: Grilla, fil: int) -> bool:
    """Devuelve un booleano indicando si la fila de la grilla denotada por el
    índice `fil` es considerada válida.

    Una fila válida cuando se cumplen todas estas condiciones:
        - La fila no tiene vacíos
        - La fila tiene la misma cantidad de unos y ceros
        - La fila no contiene tres casilleros consecutivos del mismo valor
    """
    valor_de_la_celda= grilla[fil]
    return es_valida (valor_de_la_celda)

    

def columna_es_valida(grilla: Grilla, col: int) -> bool:
    """Devuelve un booleano indicando si la columna de la grilla denotada por
    el índice `col` es considerada válida.

    Las condiciones para que una columna sea válida son las mismas que las
    condiciones de las filas."""
    valor_de_la_celda=[fila[col]for fila in grilla] 
    return es_valida (valor_de_la_celda)

    
   


def grilla_terminada(grilla: Grilla) -> bool:
    """Devuelve un booleano indicando si la grilla se encuentra terminada.

    Una grilla se considera terminada si todas sus filas y columnas son
    válidas."""
    for i in range (len(grilla)): 
        if not fila_es_valida(grilla, i):
            return False 
    for j in range (len(grilla[0])):
        if not columna_es_valida(grilla, j):
            return False
    return True 


