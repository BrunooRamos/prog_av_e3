import ply.lex as lex
import ply.yacc as yacc


'''
    Este módulo contiene el parser de la gramática USQL.
    Se encarga de transformar las consultas escritas en USQL a consultas SQL.

    Variables:
    - tokens: lista de tokens.
    - reserved: palabras reservadas.
    - lexer: lexer de la gramática.
    - parser: parser de la gramática.
'''

# Lista de tokens
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'STRING',
    'OPERATOR',
    'SEMICOLON',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'DOT',
)

# Palabras reservadas
reserved = {
    'TRAEME': 'TRAEME',
    'TODO': 'TODO',
    'DE': 'DE',
    'LA': 'LA',
    'TABLA': 'TABLA',
    'DONDE': 'DONDE',
    'AGRUPANDO': 'AGRUPANDO',
    'POR': 'POR',
    'MEZCLANDO': 'MEZCLANDO',
    'EN': 'EN',
    'LOS': 'LOS',
    'DISTINTOS': 'DISTINTOS',
    'CONTANDO': 'CONTANDO',
    'METE': 'METE',
    'VALORES': 'VALORES',
    'ACTUALIZA': 'ACTUALIZA',
    'SETEA': 'SETEA',
    'BORRA': 'BORRA',
    'ORDENA': 'ORDENA',
    'POR': 'POR',
    'COMO': 'COMO',
    'MUCHO': 'MUCHO',
    'TENIENDO': 'TENIENDO',
    'CUENTA': 'CUENTA',
    'EXISTE': 'EXISTE',
    'ESTO': 'ESTO',
    'ENTRE': 'ENTRE',
    'PARECIDO': 'PARECIDO',
    'A': 'A',
    'ES NULO': 'ES_NULO',
    'ES': 'ES',
    'NULO': 'NULO',
    'CAMBIA': 'CAMBIA',
    'AGREGA': 'AGREGA',
    'COLUMNA': 'COLUMNA',
    'ELIMINA': 'ELIMINA',
    'CREA': 'CREA',
    'TIRA': 'TIRA',
    'DEFECTO': 'DEFECTO',
    'UNICO': 'UNICO',
    'CLAVE': 'CLAVE',
    'PRIMA': 'PRIMA',
    'REFERENTE': 'REFERENTE',
    'NO': 'NO',
    'TRANSFORMA': 'TRANSFORMA',
    'Y': 'Y',
    'VARCHAR': 'VARCHAR',
    'INT': 'INT',
    'DATE': 'DATE',
    'FLOAT': 'FLOAT',
    'WHERE': 'WHERE',
    'DEL': 'DEL',
    'GROUP': 'GROUP',
    'BY': 'BY',
}

tokens += tuple(reserved.values())

#Pueden tener puntos y guiones bajos
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.upper(), 'IDENTIFIER')
    return t

# Expresiones regulares para tokens simples
t_SEMICOLON = r';'
t_OPERATOR = r'[\+\-\*/<>]=?|='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_DOT = r'\.'

# Ignorar espacios en blanco
t_ignore = ' \t'


def t_STRING(t):
    r'\'(.*?)\''
    return t

def t_NUMBER(t):
    r'\d+'
    return t

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Definición de la gramática
def p_usql_query(p):
    '''usql_query : select_query
                  | insert_query
                  | update_query
                  | delete_query
                  | alter_query'''
    p[0] = p[1]

def p_select_query(p):
    'select_query : TRAEME selection DE LA TABLA IDENTIFIER group_by join condition SEMICOLON'
    p[0] = f'SELECT {p[2]} FROM {p[6]}{p[7]}{p[8]}{p[9]};'


def p_insert_query(p):
    'insert_query : METE EN insertion LOS VALORES LPAREN value_list RPAREN SEMICOLON'
    p[0] = f'INSERT INTO {p[3]} VALUES ({p[7]});'

def p_update_query(p):
    'update_query : ACTUALIZA IDENTIFIER SETEA IDENTIFIER OPERATOR value condition SEMICOLON'
    p[0] = f'UPDATE {p[2]} SET {p[4]} {p[5]} {p[6]}{p[7]};'

def p_delete_query(p):
    'delete_query : BORRA DE LA TABLA IDENTIFIER condition SEMICOLON'
    p[0] = f'DELETE FROM {p[5]}{p[6]};'

def p_alter_query(p):
    '''alter_query : CAMBIA LA TABLA IDENTIFIER AGREGA LA COLUMNA column_data SEMICOLON
                   | CAMBIA LA TABLA IDENTIFIER ELIMINA LA COLUMNA IDENTIFIER SEMICOLON'''
    if p[5] == 'AGREGA':
        p[0] = f'ALTER TABLE {p[4]} ADD COLUMN {p[8]};'
    elif p[5] == 'ELIMINA':
        p[0] = f'ALTER TABLE {p[4]} DROP COLUMN {p[8]};'

def p_column_data(p):
    '''column_data : IDENTIFIER data_type constraints
                   | IDENTIFIER data_type'''
    p[0] = f'{p[1]} {p[2]} {p[3]}' if len(p) > 3 else f'{p[1]} {p[2]}'

def p_data_type(p):
    '''data_type : VARCHAR LPAREN NUMBER RPAREN
                 | INT
                 | DATE
                 | FLOAT'''
    p[0] = f'{p[1]}{p[2]}{p[3]}{p[4]}' if len(p) > 2 else p[1]

def p_constraints(p):
    '''constraints : NO NULO
                   | UNICO
                   | CLAVE PRIMA'''
    if p[2] == 'NULO':
        p[0] = 'NOT NULL'
    elif p[1] == 'UNICO':
        p[0] = 'UNIQUE'
    elif p[1] == 'CLAVE':
        p[0] = 'PRIMARY KEY'


def p_selection(p):
    '''selection : TODO
                 | CONTANDO LPAREN TODO RPAREN
                 | LOS DISTINTOS IDENTIFIER'''
    
    if p[1] == 'TODO':
        p[0] = '*'
    elif p[1] == 'LOS' and p[2] == 'DISTINTOS':
        p[0] = f'DISTINCT {p[3]}'
    elif p[1] == 'CONTANDO':
        p[0] = f'COUNT(*)'

def p_join(p):
    '''join : empty
            | MEZCLANDO IDENTIFIER EN IDENTIFIER DOT IDENTIFIER OPERATOR IDENTIFIER DOT IDENTIFIER'''
    p[0] = f' JOIN {p[2]} ON {p[4]}.{p[6]} {p[7]} {p[8]}.{p[10]}' if len(p) > 2 else ''

def p_group_by(p):
    '''group_by : empty
                | AGRUPANDO POR IDENTIFIER grouping_condition'''
    p[0] = f' GROUP BY {p[3]} {p[4]}' if len(p) > 2 else p[1]

def p_grouping_condition(p):
    '''grouping_condition : empty
                         | WHERE DEL GROUP BY left_side_id OPERATOR value'''
    p[0] = f'HAVING {p[5]} {p[6]} {p[7]}' if len(p) > 2 else p[1]

def p_left_side_id(p):
    '''left_side_id : IDENTIFIER
                    | IDENTIFIER LPAREN OPERATOR RPAREN'''
    p[0] = p[1] if len(p) == 2 else f'COUNT(*)'

def p_insertion(p):
    '''insertion : IDENTIFIER
                 | IDENTIFIER LPAREN column_list RPAREN'''
    p[0] = p[1] if len(p) == 2 else f'{p[1]} ({p[3]})'

def p_column_list(p):
    '''column_list : IDENTIFIER
                   | column_list COMMA IDENTIFIER'''
    p[0] = p[1] if len(p) == 2 else f'{p[1]}, {p[3]}'

def p_value_list(p):
    '''value_list : value
                  | value_list COMMA value'''
    p[0] = p[1] if len(p) == 2 else f'{p[1]}, {p[3]}'

def p_condition(p):
    '''condition : DONDE expression
                 | empty'''
    p[0] = f' WHERE {p[2]}' if len(p) > 2 else p[1]

def p_expression(p):
    '''expression : IDENTIFIER OPERATOR value
                  | IDENTIFIER DOT IDENTIFIER OPERATOR value
                  | IDENTIFIER ENTRE value Y value'''
    if len(p) == 4:
        p[0] = f'{p[1]} {p[2]} {p[3]}'
    elif len(p) == 6 and p[2] == '.':
        p[0] = f'{p[1]}.{p[3]} {p[4]} {p[5]}'
    elif len(p) == 6 and p[2] == 'ENTRE':
        p[0] = f'{p[1]} BETWEEN {p[3]} AND {p[5]}'

def p_value(p):
    '''value : NUMBER
             | STRING'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    p[0] = ''

def p_error(p):
    raise SyntaxError(f'Syntax error at token {p.type}')

parser = yacc.yacc()