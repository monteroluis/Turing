import gramatica as g
import ts as TS
from expresiones import *
from instrucciones import *

mensaje = ''


def procesar_write(instr, ts):
   # print('>> ', resolver_cadena(instr.cad, ts))
    global mensaje
    mensaje += '>> ' + str(resolver_cadena(instr.cad, ts)) + '\n'



def procesar_definicion(instr, ts):
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, 0)  # inicializamos con 0 como valor por defecto
    ts.agregar(simbolo)


def procesar_asignacion(instr, ts):
    val = resolver_expresion_aritmetica(instr.expNumerica, ts)
    simbolo = TS.Simbolo(instr.id, TS.TIPO_DATO.NUMERO, val)
    ts.actualizar(simbolo)


def procesar_during(instr, ts):
    while resolver_expresion_comparativa(instr.expcomparativa, ts):
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)


def procesar_realize_during(instr, ts):
    while resolver_expresion_comparativa(instr.expcomparativa, ts):
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)
        if resolver_expresion_comparativa(instr.expcomparativa, ts):
            break;


def procesar_iteof(instr, ts):
    val = resolver_expresion_comparativa(instr.expcomparativa, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)


def procesar_otherwise(instr, ts):
    val = resolver_expresion_comparativa(instr.expcomparativa, ts)
    if val:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrIfVerdadero, ts_local)
    else:
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrIfFalso, ts_local)


def procesar_sasto(instr, ts):
    val = resolver_expresion_aritmetica(instr.expNumerica, ts)
    print(val)
    while resolver_expresion_comparativa(instr.expcomparativa, ts):
        ts_local = TS.TablaDeSimbolos(ts.simbolos)
        procesar_instrucciones(instr.instrucciones, ts_local)


def resolver_cadena(expCad, ts):
    if isinstance(expCad, ExpresionConcatenar):
        exp1 = resolver_cadena(expCad.exp1, ts)
        exp2 = resolver_cadena(expCad.exp2, ts)
        return exp1 + exp2
    elif isinstance(expCad, ExpresionDobleComilla):
        return expCad.val
    elif isinstance(expCad, ExpresionCadenaNumerico):
        return str(resolver_expresion_aritmetica(expCad.exp, ts))
    else:
        print('Error: Expresión cadena no válida')


def resolver_expresion_comparativa(expCom, ts):
    exp1 = resolver_expresion_aritmetica(expCom.exp1, ts)
    exp2 = resolver_expresion_aritmetica(expCom.exp2, ts)
    if expCom.operador == OPERACION_COMPARATIVA.MAYOR_QUE: return exp1 > exp2
    if expCom.operador == OPERACION_COMPARATIVA.MENOR_QUE: return exp1 < exp2
    if expCom.operador == OPERACION_COMPARATIVA.IGUAL: return exp1 == exp2
    if expCom.operador == OPERACION_COMPARATIVA.DIFERENTE: return exp1 != exp2
    if expCom.operador == OPERACION_COMPARATIVA.MAYOR_IGUAL_QUE: return exp1 >= exp2
    if expCom.operador == OPERACION_COMPARATIVA.MENOR_IGUAL_QUE: return exp1 <= exp2


def resolver_expresion_aritmetica(expNum, ts):
    if isinstance(expNum, ExpresionBinaria):
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if expNum.operador == OPERACION_ARITMETICA.MAS: return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS: return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR: return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO: return exp1 / exp2
        if expNum.operador == OPERACION_ARITMETICA.MODULO: return exp1 % exp2
        if expNum.operador == OPERACION_ARITMETICA.POTENCIA: return exp1 ** exp2
    elif isinstance(expNum, ExpresionNegativo):
        exp = resolver_expresion_aritmetica(expNum.exp, ts)
        return exp * -1
    elif isinstance(expNum, ExpresionNumero):
        return expNum.val
    elif isinstance(expNum, ExpresionIdentificador):
        return ts.obtener(expNum.id).valor


def procesar_instrucciones(instrucciones, ts):
    ## lista de instrucciones recolectadas
    for instr in instrucciones:
        if isinstance(instr, Write):
            procesar_write(instr, ts)
        elif isinstance(instr, Definicion):
            procesar_definicion(instr, ts)
        elif isinstance(instr, Asignacion):
            procesar_asignacion(instr, ts)
        elif isinstance(instr, During):
            procesar_during(instr, ts)
        elif isinstance(instr, Iteof):
            procesar_iteof(instr, ts)
        elif isinstance(instr, Otherwise):
            procesar_otherwise(instr, ts)
        elif isinstance(instr, Sasto):
            procesar_sasto(instr, ts)
        elif isinstance(instr, Realize_during):
            procesar_realize_during(instr, ts)
        else:
            print('Error: instrucción no válida')


def salida():
    global mensaje
    datos = mensaje
    mensaje = ''
    print(datos)
    return datos
