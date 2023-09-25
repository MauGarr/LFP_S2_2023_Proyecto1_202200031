from Instrucciones.aritmeticas import *
from Instrucciones.trigonometricas import *
from Abstract.lexema import *
from Abstract.numero import *

# Patron, Lexema y Token

reserved = {
    'ROPERACIONES'          : 'operaciones',
    'ROPERACION'            : 'operacion',
    'RVALOR1'               : 'valor1',
    'RVALOR2'               : 'valor2',
    'RSUMA'                 : 'suma',
    'RRESTA'                : 'resta',
    'RMULTIPLICACION'       : 'multiplicacion',
    'RDIVISION'             : 'division',
    'RPOTENCIA'             : 'potencia',
    'RRAIZ'                 : 'raiz',
    'RINVERSO'              : 'inverso',
    'RSENO'                 : 'seno',
    'RCOSENO'               : 'coseno',
    'RTANGENTE'             : 'tangente',
    'RMODULO'               : 'modulo',
    'RCONFIGURACIONES'      : 'configuraciones',
    'RTEXTO'                : 'texto',
    'RFONDO'                : 'fondo',
    'RFUENTE'               : 'fuente',
    'RFORMA'                : 'forma',
    'COMA'                  : ',',
    'PUNTO'                 : '.',
    'DPUNTOS'               : ':',
    'CORI'                  : '[',
    'CORD'                  : ']',
    'LLAVEI'                : '{',
    'LLAVED'                : '}'
}

lexemas = list(reserved.values())  # ['Operacion', 'Valor1', 'Valor2', 'Suma',...]
global n_fila
global n_columna
global instrucciones
global lista_lexemas

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []

def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = 0
    
    while cadena:
        char = cadena[puntero]
        puntero += 1    

        if char == '\"':
            lexema, cadena = armar_lexema(cadena[puntero:])
            if lexema and cadena: 
                n_columna += 1
                #Armo lexema como clase 
                l = Lexema(lexema, n_linea, n_columna)
                #Se agrega el lexema a la lista de lexemas
                lista_lexemas.append(l)
                n_columna += len(lexema) + 1
                puntero = 0
        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna += 1
                #Armo lexema como clase
                n = Numero(token, n_linea, n_columna)
                #Se agrega el lexema a la lista de lexemas
                lista_lexemas.append(n)
                n_columna += len(str(token)) + 1
                puntero = 0
        elif char == '[' or char == ']':  # talvez genere error
            #Armo lexema como clase
            c = Lexema(lexema, n_linea, n_columna)
            #Se agrega el lexema a la lista de lexemas
            lista_lexemas.append(c)
            cadena = cadena[1:]
            n_columna += 1
            puntero = 0
        elif char == '\t':
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == '\n':
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
        else: 
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
    
    for lexema in lista_lexemas:
        print(lexema)

def armar_numero(cadena):
    numero = ''
    puntero = ''
    is_decimal = False
    for char in cadena:
        puntero += char
        if char == '.':
            is_decimal = True 
        if char == '\"' or char == ' ' or char == '\n' or char == '\t' or char == ',':
            if is_decimal:
                return float(numero), cadena[len(puntero) - 1:]
            else:
                return int(numero), cadena[len(puntero) - 1:]
        else: 
            numero += char
    return None, None

def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''
    for char in cadena:
        puntero += char 
        if char == '\"':
            return lexema, cadena[len(puntero):]
        else:
            lexema += char
    return None, None

def operar():
    global lista_lexemas
    global instrucciones
    operacion = ''
    n1 = ''
    n2 = ''
    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'Operacion':
            operacion = lista_lexemas.pop(0)
        elif lexema.operar(None) == 'Valor1':
            n1 = lista_lexemas.pop(0)
            if n1.operar(None) == '[':
                n1 = operar()
        elif lexema.operar(None) == 'Valor2':
            n2 = lista_lexemas.pop(0)
            if n2.operar(None) == '[':
                n2 = operar()

        if operacion and n1 and n2:
            return Aritmetica(n1, n2, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n2.getFila()}: {n2.getColumna()}')
        
        elif operacion and n1 and operacion.operar(None) == ('Seno' or 'Coseno' or 'Tangente'):
            return Trigonometrica(n1, operacion, f'Inicio: {operacion.getFila()}: {operacion.getColumna()}', f'Fin: {n1.getFila()}: {n1.getColumna()}')
    return None

def operar_recursivo():
    global instrucciones
    while True:
        operacion = operar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break

    for instruccion in instrucciones:
        print(instruccion.operar(None))


entrada = '''{
{
    "operaciones": [
        {
            "operacion": "suma",
            "valor1": 4.5,
            "valor2": 5.32
        },
        {
            "operacion": "resta",
            "valor1": 4.5,
            "valor2": [
                {
                    "operacion": "potencia",
                    "valor1": 10,
                    "valor2": 3
                }
                ]
        },
        {
            "operacion": "suma",
            "valor1": [
                {
                    "operacion": "seno",
                    "valor1": 90
                }
            ],
            "valor2": 5.32
        },
        {
            "operacion": "multiplicacion",
            "valor1": 7,
            "valor2": 3
        },
        {
            "operacion": "division",
            "valor1": 15,
            "valor2": 3
        }
    ],
    "configuraciones": [
        {
            "texto": "Operaciones",
            "fondo": "blue",
            "fuente": "white",
            "forma": "circle"
        }
    ]
}
}'''

instruccion(entrada)
operar_recursivo()