mensaje=''
reservadas = {
    'numeric': 'NUMERIC',
    'write': 'WRITE',
    'during': 'DURING',
    'iteof': 'ITEOF',
    'otherwise': 'OTHERWISE',
    'sasto': 'SASTO',
    'into':'INTO',
    'realize':'REALIZE',
}

tokens = [
             'PTCOMA',
             'DUPOINT',
             'LLAVIZQ',
             'LLAVDER',
             'PARIZQ',
             'PARDER',
             'IGUAL',
             'MAS',
             'MENOS',
             'POR',
             'DIVIDIDO',
             'POTENCIA',
             'CONCAT',
             'MAYIGU',
             'MENIGU',
             'MENQUE',
             'MAYQUE',
             'IGUALQUE',
             'NIGUALQUE',
             'DECIMAL',
             'ENTERO',
             'CADENA',
             'ID',
             'MODULO',
         ] + list(reservadas.values())

# Tokens
t_PTCOMA=r';'
t_DUPOINT = r':'
t_LLAVIZQ = r'{'
t_LLAVDER = r'}'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_IGUAL = r'~'
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_POTENCIA = r'\^'
t_CONCAT = r'&'
t_MENQUE = r'<'
t_MAYQUE = r'>'
t_MAYIGU= r'>~'
t_MENIGU=r'<~'
t_IGUALQUE = r'~~'
t_NIGUALQUE = r'!~'
t_MODULO = r'%'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        global mensaje
        mensaje="Float value too large "+str( t.value)
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        global mensaje
        mensaje="Integer value too large "+str(t.value)
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_TRUE(t):
  r'true'
  t.value = True
  return t

def t_FALSE(t):
  r'false'
  t.value = False
  return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')  # Check for reserved words
    return t


def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # remuevo las comillas
    return t

# Comentario de múltiples líneas ---> <---
def t_COMENTARIO_MULTILINEA(t):
    r'--->(.|\n)*?---'
    t.lexer.lineno += t.value.count('\n')


# Comentario simple #  ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1


# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    global mensaje
    mensaje = "Illegal character " + str( t.value[0])
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Construyendo el analizador léxico
import ply.lex as lex

lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left', 'CONCAT'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),
    ('left', 'POTENCIA', 'MODULO'),
    ('right', 'UMENOS'),
)

# Definición de la gramática

from expresiones import *
from instrucciones import *

def p_init(t):
    'init            : instrucciones'
    t[0] = t[1]


def p_instrucciones_lista(t):
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]


def p_instrucciones_instruccion(t):
    'instrucciones    : instruccion '
    t[0] = [t[1]]


def p_instruccion(t):
    '''instruccion      : write_instr
                        | definicion_instr
                        | asignacion_instr
                        | during_instr
                        | iteof_instr
                        | iteof_otherwise_instr
                        | sasto_instr
                        | realize_during_instr'''
    t[0] = t[1]

def p_instruccion_write(t):
    'write_instr     :  WRITE PARIZQ expresion_cadena PARDER PTCOMA'
    t[0] = Write(t[3])


def p_instruccion_definicion(t):
    '''definicion_instr   : NUMERIC ID PTCOMA'''
    t[0] = Definicion(t[2])

def p_asignacion_instr(t):
    '''asignacion_instr   :  ID IGUAL expresion_numerica PTCOMA'''
    t[0] = Asignacion(t[1], t[3])

def p_during_instr(t):
    'during_instr     : DURING DUPOINT  expresion_comparativa  LLAVIZQ instrucciones LLAVDER'
    t[0] = During(t[3], t[5])

def p_realize_during_instr(t):
    'realize_during_instr     : REALIZE LLAVIZQ  instrucciones  LLAVDER DURING  expresion_comparativa PTCOMA '
    t[0] = During(t[6], t[3])


def p_iteof_instr(t):
    'iteof_instr  : ITEOF DUPOINT expresion_comparativa  LLAVIZQ instrucciones LLAVDER'
    t[0] = Iteof(t[3], t[5])

def p_iteof_otherwise_instr(t):
    'iteof_otherwise_instr      : ITEOF DUPOINT expresion_comparativa  LLAVIZQ instrucciones LLAVDER OTHERWISE LLAVIZQ instrucciones LLAVDER'
    t[0] = Otherwise(t[3], t[5], t[9])

def p_sasto_instr(t):
    'sasto_instr     : SASTO  DUPOINT  expresion_comparativa PTCOMA expresion_numerica INTO LLAVIZQ instrucciones LLAVDER '
    t[0] = Sasto(t[3], t[5], t[8])

def p_expresion_binaria(t):
    '''expresion_numerica : expresion_numerica MAS expresion_numerica
                         | expresion_numerica MENOS expresion_numerica
                         | expresion_numerica POR expresion_numerica
                         | expresion_numerica DIVIDIDO expresion_numerica
                         | expresion_numerica MODULO expresion_numerica
                         | expresion_numerica POTENCIA expresion_numerica '''
    if t[2] == '+':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)
    elif t[2] == '%':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MODULO)
    elif t[2] == '^':
        t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POTENCIA)


def p_expresion_unaria(t):
    'expresion_numerica : MENOS expresion_numerica %prec UMENOS'
    t[0] = ExpresionNegativo(t[2])


def p_expresion_agrupacion(t):
    'expresion_numerica : PARIZQ expresion_numerica PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion_numerica : ENTERO
                          | DECIMAL'''
    t[0] = ExpresionNumero(t[1])

def p_expresion_id(t):
    'expresion_numerica   : ID'
    t[0] = ExpresionIdentificador(t[1])


def p_expresion_concatenacion(t):
    'expresion_cadena     : expresion_cadena CONCAT expresion_cadena'
    t[0] = ExpresionConcatenar(t[1], t[3])


def p_expresion_cadena(t):
    'expresion_cadena     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])


def p_expresion_cadena_numerico(t):
    'expresion_cadena     : expresion_numerica'
    t[0] = ExpresionCadenaNumerico(t[1])


def p_expresion_comparativa(t):
    '''expresion_comparativa : expresion_numerica MAYQUE expresion_numerica
                             | expresion_numerica MENQUE expresion_numerica
                             | expresion_numerica IGUALQUE expresion_numerica
                             | expresion_numerica MAYIGU expresion_numerica
                             | expresion_numerica MENIGU expresion_numerica
                             | expresion_numerica NIGUALQUE expresion_numerica'''
    if t[2] == '>':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.MAYOR_QUE)
    elif t[2] == '<':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.MENOR_QUE)
    elif t[2] == '~~':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.IGUAL)
    elif t[2] == '!~':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.DIFERENTE)
    elif t[2] == '>~':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.MAYOR_IGUAL_QUE)
    elif t[2] == '<~':
        t[0] = ExpresionComparativa(t[1], t[3], OPERACION_COMPARATIVA.MENOR_IGUAL_QUE)


def p_error(t):
    global mensaje
    mensaje = "Error sintáctico en  " + str( t.value)
    print("Error sintáctico en '%s'" % t.value)


import ply.yacc as yacc

parser = yacc.yacc()

def parse(input):
    return parser.parse(input)
