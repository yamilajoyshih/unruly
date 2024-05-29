# -*- coding: utf-8 -*-
import pprint
import sys
import traceback
from typing import List

import unruly

# Si las pruebas se ven mal en tu terminal, probá cambiando el valor
# de esta constante a True para desactivar los colores ANSI.
TERMINAL_SIN_COLOR = False


def validar_estado(desc: List[str], grilla: unruly.Grilla):
    """Asegura que `grilla` tenga un estado similar a `desc` utilizando las
    siguientes funciones del módulo `unruly`:
        - crear_grilla
        - dimensiones
        - posicion_es_vacia
        - posicion_hay_uno
        - posicion_hay_cero
    Si el estado no es el esperado, se lanza un AssertionError con un mensaje
    extenso de por qué falló."""
    x = None
    y = None
    ancho, alto = unruly.dimensiones(grilla)
    try:
        assert (ancho, alto) == (len(desc[0]), len(desc)), (
            f"Dimension obtenida ({ancho}, {alto}) no es la esperada "
            f"({len(desc[0])}, {len(desc)})"
        )
        for y in range(alto):
            for x in range(ancho):
                c = desc[y][x]
                if c == " ":
                    assert unruly.posicion_es_vacia(grilla, x, y) is True
                    assert unruly.posicion_hay_cero(grilla, x, y) is False
                    assert unruly.posicion_hay_uno(grilla, x, y) is False
                elif c == "1":
                    assert unruly.posicion_es_vacia(grilla, x, y) is False
                    assert unruly.posicion_hay_cero(grilla, x, y) is False
                    assert unruly.posicion_hay_uno(grilla, x, y) is True
                elif c == "0":
                    assert unruly.posicion_es_vacia(grilla, x, y) is False
                    assert unruly.posicion_hay_cero(grilla, x, y) is True
                    assert unruly.posicion_hay_uno(grilla, x, y) is False
    except AssertionError as e:
        error_msg = "Estado esperado:\n"
        error_msg += "\n".join(desc) + "\n"
        error_msg += "\n"
        error_msg += "Estado actual:\n"
        error_msg += pprint.pformat(grilla) + "\n\n"
        if x is not None and y is not None:
            error_msg += f"Error en columna = {x}, fila = {y}:\n"
            error_msg += (
                f"\tposicion_hay_cero: {unruly.posicion_hay_cero(grilla, x, y)}\n"
            )
            error_msg += (
                f"\tposicion_hay_uno: {unruly.posicion_hay_uno(grilla, x, y)}\n"
            )
            error_msg += (
                f"\tposicion_es_vacia: {unruly.posicion_es_vacia(grilla, x, y)}\n"
            )
        raise AssertionError(error_msg + str(e))


def test_01_representacion_simple():
    """Crea una nueva grilla del unruly 4x4, asegurando que las funciones de
    dimensiones y posición devuelvan lo que corresponda."""
    desc = [
        "  01",
        "101 ",
        "  0 ",
        " 10 ",
    ]
    grilla = unruly.crear_grilla(desc)
    validar_estado(desc, grilla)


def test_02_representacion_mas_grande():
    """Crea una nueva grilla del unruly 8x8, asegurando que las funciones de
    dimensiones y posición devuelvan lo que corresponda."""
    desc = [
        "  01  01",
        "101 101 ",
        "  0   0 ",
        " 10  10 ",
        "  01  01",
        "101 101 ",
        "  0   0 ",
        " 10  10 ",
    ]
    grilla = unruly.crear_grilla(desc)
    validar_estado(desc, grilla)


def test_03_representacion_rectangular():
    """Crea una nueva grilla del unruly 8x4, asegurando que las funciones de
    dimensiones y posición devuelvan lo que corresponda."""
    desc = [
        "  01  01",
        "101 101 ",
        "  0   0 ",
        " 10  10 ",
    ]
    grilla = unruly.crear_grilla(desc)
    validar_estado(desc, grilla)


def test_04_reemplazar_por_vacio():
    """Crea una nueva grilla de unruly, e intenta eliminar el valor en tres
    posiciones de la grilla:
        - En una posición vacía (col=1, fil=0)
        - En una posición ocupada por un 0 (col=2, fil=3)
        - En una posición ocupada por un 1 (col=2, fil=1)
    """
    desc_inicial = [
        "  01",
        "101 ",
        "  0 ",
        " 10 ",
    ]
    desc_esperada = [
        "  01",
        "10  ",
        "  0 ",
        " 1  ",
    ]
    grilla = unruly.crear_grilla(desc_inicial)
    unruly.cambiar_a_vacio(grilla, 1, 0)
    unruly.cambiar_a_vacio(grilla, 2, 3)
    unruly.cambiar_a_vacio(grilla, 2, 1)
    validar_estado(desc_esperada, grilla)


def test_05_reemplazar_por_valor_uno():
    """Crea una nueva grilla de unruly, y escribe el valor 1 en tres posiciones
    de la grilla:
        - En una posición vacía (col=1, fil=0)
        - En una posición ocupada por un 0 (col=2, fil=3)
        - En una posición ocupada por un 1 (col=2, fil=1)

    TIP: Si este test falla, es posible que haya un error en los tipos de los
    valores de los casilleros una vez reemplazado el valor.
    Por ejemplo si originalmente en la casilla existía el valor "1" (cadena)
    y se reemplazó por el valor 0 (entero) entonces el test seguramente va a
    fallar.
    """
    desc_inicial = [
        "  01",
        "101 ",
        "  0 ",
        " 10 ",
    ]
    desc_esperada = [
        " 101",
        "101 ",
        "  0 ",
        " 11 ",
    ]
    grilla = unruly.crear_grilla(desc_inicial)
    unruly.cambiar_a_uno(grilla, 1, 0)
    unruly.cambiar_a_uno(grilla, 2, 3)
    unruly.cambiar_a_uno(grilla, 2, 1)
    validar_estado(desc_esperada, grilla)


def test_06_reemplazar_por_valor_cero():
    """Crea una nueva grilla de unruly, y escribe el valor 0 en tres posiciones
    de la grilla:
        - En una posición vacía (col=1, fil=0)
        - En una posición ocupada por un 0 (col=2, fil=3)
        - En una posición ocupada por un 1 (col=2, fil=1)

    TIP: Si este test falla, es posible que haya un error en los tipos de los
    valores de los casilleros una vez reemplazado el valor.
    Por ejemplo si originalmente en la casilla existía el valor "0" (cadena)
    y se reemplazó por el valor 0 (entero) entonces el test seguramente va a
    fallar.
    """
    desc_inicial = [
        "  01",
        "101 ",
        "  0 ",
        " 10 ",
    ]
    desc_esperada = [
        " 001",
        "100 ",
        "  0 ",
        " 10 ",
    ]
    grilla = unruly.crear_grilla(desc_inicial)
    unruly.cambiar_a_cero(grilla, 1, 0)
    unruly.cambiar_a_cero(grilla, 2, 3)
    unruly.cambiar_a_cero(grilla, 2, 1)
    validar_estado(desc_esperada, grilla)


def test_07_filas_invalidas():
    """Crea una nueva grilla de unruly con filas inválidas, y se asegura que la
    función `fila_es_valida` devuelva False para todas. Se prueban los casos
    descriptos por la documentación de `fila_es_valida`:
        - Fila tiene algunos vacíos
        - Fila no tiene la misma cantidad de unos y ceros
        - Fila contiene tres casilleros consecutivos del mismo valor
    """
    desc = [
        "1 0 1001",
        "11011001",
        "00100110",
        "11101001",
        "00111001",
        "00011101",
        "11011000",
        "11100010",
        "111 0010",
        "1 100 10",
    ]
    grilla = unruly.crear_grilla(desc)
    _ancho, alto = unruly.dimensiones(grilla)
    for fila in range(alto):
        resultado = unruly.fila_es_valida(grilla, fila)
        assert resultado is False, (
            f"Se devolvió {resultado} para la fila {fila}\n"
            "Estado actual:\n"
            f"{pprint.pformat(grilla)}\n"
        )


def test_08_filas_validas():
    """Crea una nueva grilla de unruly correctamente terminado, y se asegura
    que la función `fila_es_valida` devuelva True para todas."""
    desc = [
        "10010101",
        "11001010",
        "00110101",
        "01101001",
        "10010110",
        "11001001",
        "00110110",
        "01101010",
    ]
    grilla = unruly.crear_grilla(desc)
    _ancho, alto = unruly.dimensiones(grilla)
    for fila in range(alto):
        resultado = unruly.fila_es_valida(grilla, fila)
        assert resultado is True, (
            f"Se devolvió {resultado} para la fila {fila}\n"
            "Estado actual:\n"
            f"{pprint.pformat(grilla)}\n"
        )


def test_09_columnas_invalidas():
    """Crea una nueva grilla de unruly con columnas inválidas, y se asegura
    que la función `columna_es_valida` devuelva False para todas. Se prueban
    los casos descriptos por la documentación de `columna_es_valida`:
        - Columna tiene algunos vacíos
        - Columna no tiene la misma cantidad de unos y ceros
        - Columna contiene tres casilleros consecutivos del mismo valor
    """
    desc = [
        "1101001100",
        " 101001110",
        "0011100010",
        " 1001110 1",
        "11011110 1",
        "0010010101",
        "0010000110",
        "1101110011",
    ]
    grilla = unruly.crear_grilla(desc)
    ancho, _alto = unruly.dimensiones(grilla)
    # Primeras 7 columnas son inválidas
    for columna in range(ancho):
        resultado = unruly.columna_es_valida(grilla, columna)
        assert resultado is False, (
            f"Se devolvió {resultado} para la columna {columna}\n"
            "Estado actual:\n"
            f"{pprint.pformat(grilla)}\n"
        )


def test_10_columnas_validas():
    """Crea una nueva grilla de unruly correctamente terminado, y se asegura
    que la función `columna_es_valida` devuelva True para todas."""
    desc = [
        "10010101",
        "11001010",
        "00110101",
        "01101001",
        "10010110",
        "11001001",
        "00110110",
        "01101010",
    ]
    grilla = unruly.crear_grilla(desc)
    ancho, _alto = unruly.dimensiones(grilla)
    for columna in range(ancho):
        resultado = unruly.columna_es_valida(grilla, columna)
        assert resultado is True, (
            f"Se devolvió {resultado} para la columna {columna}\n"
            "Estado actual:\n"
            f"{pprint.pformat(grilla)}\n"
        )


def test_11_grillas_correctamente_terminadas():
    """Se prueban algunas grillas de unruly que están correctamente terminadas.
    para validar el funcionamiento de `grilla_terminada`
    """
    descripciones = [
        [
            "10010101",
            "11001010",
            "00110101",
            "01101001",
            "10010110",
            "11001001",
            "00110110",
            "01101010",
        ],
        [
            "101100",
            "011010",
            "100101",
            "010011",
            "101010",
            "010101",
        ],
        [
            "10110100",
            "01001011",
            "01101100",
            "10110010",
            "01001011",
            "10010101",
        ]
    ]

    for desc in descripciones:
        grilla = unruly.crear_grilla(desc)
        resultado = unruly.grilla_terminada(grilla)
        assert resultado is True, (
            f"Se devolvió {resultado} para la siguiente grilla terminada:\n"
            f"{pprint.pformat(grilla)}"
        )


def test_12_grillas_incompletas_o_mal_terminadas():
    """Se prueban algunas grillas de unruly que están incorrectamente
    terminadas o incompletas para validar el funcionamiento de
    `grilla_terminada`"""
    descripciones = [
        [
            "101100",
            "011010",
            "100101",
            "010101",
            "1010 0",
            "010101"
        ],
        [
            "101100",
            "011011",
            "100101",
            "010101",
            "101010",
            "110100"
        ],
        [
            "101100",
            "011011",
            "100101",
            "010101",
            "101010",
            "010101"
        ],
    ]

    for desc in descripciones:
        grilla = unruly.crear_grilla(desc)
        resultado = unruly.grilla_terminada(grilla)
        assert resultado is False, (
            f"Se devolvió {resultado} para la siguiente grilla invalida:\n"
            f"{pprint.pformat(grilla)}"
        )


def test_13_colocar_y_terminar_una_grilla():
    """¡Último test! Se crea una grilla que está muy cerca de terminarse, se
    colocan los números que faltan, y se valida su solución."""
    desc_inicial = [
        "101101",
        "011010",
        "100101",
        "000011",
        "101110",
        "010101",
    ]

    grilla = unruly.crear_grilla(desc_inicial)
    assert not unruly.grilla_terminada(grilla), (
        f"Grilla inicial se consideró como terminada:\n"
        f"{pprint.pformat(grilla)}"
    )
    unruly.cambiar_a_cero(grilla, 5, 0)
    unruly.cambiar_a_cero(grilla, 3, 4)
    unruly.cambiar_a_uno(grilla, 1, 3)
    assert unruly.grilla_terminada(grilla), (
        f"Grilla final no se consideró como terminada:\n"
        f"{pprint.pformat(grilla)}"
    )


# Sólo se van a correr aquellos tests que estén mencionados dentro de la
# siguiente constante
TESTS = (
    test_01_representacion_simple,
    test_02_representacion_mas_grande,
    test_03_representacion_rectangular,
    test_04_reemplazar_por_vacio,
    test_05_reemplazar_por_valor_uno,
    test_06_reemplazar_por_valor_cero,
    test_07_filas_invalidas,
    test_08_filas_validas,
    test_09_columnas_invalidas,
    test_10_columnas_validas,
    test_11_grillas_correctamente_terminadas,
    test_12_grillas_incompletas_o_mal_terminadas,
    test_13_colocar_y_terminar_una_grilla,
)

# El código que viene abajo tiene algunas *magias* para simplificar la corrida
# de los tests y proveer la mayor información posible sobre los errores que se
# produzcan. ¡No te preocupes si no lo entendés completamente!

# Colores ANSI para una salida más agradable en las terminales que lo permitan
COLOR_OK = "\033[1m\033[92m"
COLOR_ERR = "\033[1m\033[91m"
COLOR_RESET = "\033[0m"


def print_color(color: str, *args, **kwargs):
    """
    Mismo comportamiento que `print` pero con un
    primer parámetro para indicar de qué color se
    imprimirá el texto.

    Si la constante TERMINAL_SIN_COLOR es True,
    esta función será exactamente equivalente
    a utilizar `print`.
    """
    if TERMINAL_SIN_COLOR:
        print(*args, **kwargs)
    else:
        print(color, end="")
        print(*args, **kwargs)
        print(COLOR_RESET, end="", flush=True)


def main():
    tests_fallidos = []
    tests_a_correr = [int(t) for t in sys.argv[1:]]
    for i, test in [
        (i, test)
        for i, test in enumerate(TESTS)
        if not tests_a_correr or i + 1 in tests_a_correr
    ]:
        print(f"Prueba {i + 1 :02} - {test.__name__}: ", end="", flush=True)
        try:
            test()
            print_color(COLOR_OK, "[OK]")
        except AssertionError as e:
            tests_fallidos.append(test.__name__)
            print_color(COLOR_ERR, "[ERROR]")
            print_color(COLOR_ERR, " >", *e.args)
            break
        except Exception:
            tests_fallidos.append(test.__name__)
            print_color(COLOR_ERR, "[BOOM - Explotó]")
            print("\n--------------- Python dijo: ---------------")
            traceback.print_exc()
            print("--------------------------------------------\n")
            break

    if not tests_fallidos:
        print()
        print_color(COLOR_OK, "###########")
        print_color(COLOR_OK, "# TODO OK #")
        print_color(COLOR_OK, "###########")
        print()
    else:
        print()
        print_color(COLOR_ERR, "##################################")
        print_color(COLOR_ERR, "              ¡ERROR!             ")
        print_color(COLOR_ERR, "Falló el siguiente test:")
        for test_con_error in tests_fallidos:
            print_color(COLOR_ERR, " - " + test_con_error)
        print_color(COLOR_ERR, "##################################")
        print(
            "TIP: Si la información de arriba no es suficiente para entender "
            "el error, revisá el código de las pruebas que fallaron en el "
            "archivo unruly_test.py."
        )


main()
