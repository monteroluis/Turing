class Instruccion:
    '''This is an abstract class'''


class Write(Instruccion):
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self, cad):
        self.cad = cad


class During(Instruccion):
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expcomparativa, instrucciones=[]):
        self.expcomparativa = expcomparativa
        self.instrucciones = instrucciones


class Definicion(Instruccion):
    '''
        Esta clase representa la instrucción de definición de variables.
        Recibe como parámetro el nombre del identificador a definir
    '''

    def __init__(self, id):
        self.id = id


class Asignacion(Instruccion):
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''

    def __init__(self, id, expNumerica):
        self.id = id
        self.expNumerica = expNumerica


class Iteof(Instruccion):
    '''
        Esta clase representa la instrucción if.
        La instrucción if recibe como parámetro una expresión coparativa y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expcomparativa, instrucciones=[]):
        self.expcomparativa = expcomparativa
        self.instrucciones = instrucciones


class Otherwise(Instruccion):
    '''
        Esta clase representa la instrucción if-else.
        La instrucción if-else recibe como parámetro una expresión comparativa y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
        a ejecutar si la expresión lógica es falsa.
    '''

    def __init__(self, expcomparativa, instrIfVerdadero=[], instrIfFalso=[]):
        self.expcomparativa = expcomparativa
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso


class Sasto(Instruccion):
    '''
           Esta clase representa la instrucción for.
           La instrucción sasto  recibe como parámetro una expresión comparativa, una numerica  y la lista
           de instrucciones a ejecutar.
     '''

    def __init__(self, expcomparativa, expNumerica, instrucciones=[]):
        self.expcomparativa = expcomparativa
        self.expNumerica = expNumerica
        self.instrucciones = instrucciones


class Realize_during(Instruccion):
    '''
             Esta clase representa la instrucción do while.
             La instrucción sasto  recibe como parámetro una expresión comparativa, una numerica  y la lista
             de instrucciones a ejecutar.
    '''

    def __init__(self,expcomparativa, instrucciones=[]):
        self.expcomparativa = expcomparativa
        self.instrucciones = instrucciones
