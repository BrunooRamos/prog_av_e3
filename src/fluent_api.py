# fluent_api.py
# Este módulo implementa una Fluent API para construir consultas USQL.

class USQLQuery:

    '''
    Clase USQLQuery.
    Esta clase se encarga de construir consultas USQL.
    '''

    def __init__(self):

        '''
        Constructor de la clase USQLQuery.
        Inicializa la consulta como una cadena vacía.
        '''

        self.query = ""

    def traeme(self, columns):

        '''
        Método traeme.
        Este método agrega a la consulta la cláusula 'TRAEME'.

        Parámetros:
        - columns: lista de columnas a seleccionar.
        
        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"TRAEME {columns} "
        return self

    def de_la_tabla(self, table):

        '''
        Método de_la_tabla.
        Este método agrega a la consulta la cláusula 'DE LA TABLA'.

        Parámetros:
        - table: nombre de la tabla.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"DE LA TABLA {table} "
        return self

    def donde(self, condition):

        '''
        Método donde.
        Este método agrega a la consulta la cláusula 'DONDE'.

        Parámetros:
        - condition: condición de filtrado.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''
        self.query += f"DONDE {condition} "
        return self

    def mete_en(self, table, columns):

        '''
        Método mete_en.
        Este método agrega a la consulta la cláusula 'METE EN'.

        Parámetros:
        - table: nombre de la tabla.
        - columns: lista de columnas.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"METE EN {table} ({', '.join(columns)}) "
        return self

    def los_valores(self, values):

        '''
        Método los_valores.
        Este método agrega a la consulta la cláusula 'LOS VALORES'.

        Parámetros:
        - values: lista de valores a insertar.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        formatted_values = ', '.join(f"'{v}'" if isinstance(v, str) else str(v) for v in values)
        self.query += f"LOS VALORES ({formatted_values}) "
        return self

    def actualiza(self, table):

        '''
        Método actualiza.
        Este método agrega a la consulta la cláusula 'ACTUALIZA'.

        Parámetros:
        - table: nombre de la tabla.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"ACTUALIZA {table} "
        return self

    def setea(self, assignments):

        '''
        Método setea.
        Este método agrega a la consulta la cláusula 'SETEA'.

        Parámetros:
        - assignments: diccionario de asignaciones.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        assigns = ', '.join(f"{k} = {v}" for k, v in assignments.items())
        self.query += f"SETEA {assigns} "
        return self

    def borra_de_la(self, table):

        '''
        Método borra_de_la.
        Este método agrega a la consulta la cláusula 'BORRA DE LA'.

        Parámetros:
        - table: nombre de la tabla.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"BORRA DE LA TABLA {table} "
        return self
    
    def mezclando(self, table):

        '''
        Método mezclando.
        Este método agrega a la consulta la cláusula 'MEZCLANDO'.

        Parámetros:
        - table: nombre de la tabla.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"MEZCLANDO {table} "
        return self
    
    def en(self, join_condition):

        '''
        Método en.
        Este método agrega a la consulta la cláusula 'EN'.

        Parámetros:
        - join_condition: condición de join.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"EN {join_condition} "
        return self
    
    def agrupando_por(self, column):

        '''
        Método agrupando_por.
        Este método agrega a la consulta la cláusula 'AGRUPANDO POR'.

        Parámetros:
        - column: nombre de la columna.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"AGRUPANDO POR {column} "
        return self
    
    def where_del_group_by(self, condition):

        '''
        Método where_del_group_by.
        Este método agrega a la consulta la cláusula 'WHERE DEL GROUP BY'.

        Parámetros:
        - condition: condición de filtrado.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"WHERE DEL GROUP BY {condition} "
        return self
    
    def agrega_columna(self, column):

        '''
        Método agrega_columna.
        Este método agrega a la consulta la cláusula 'AGREGA LA COLUMNA'.

        Parámetros:
        - column: nombre de la columna.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"AGREGA LA COLUMNA {column} "
        return self
    
    def cambia(self, table):

        '''
        Método cambia.
        Este método agrega a la consulta la cláusula 'CAMBIA LA TABLA'.

        Parámetros:
        - table: nombre de la tabla.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''

        self.query += f"CAMBIA LA TABLA {table} "
        return self
    
    def elimina_columna(self, column):

        '''
        Método elimina_columna.
        Este método agrega a la consulta la cláusula 'ELIMINA LA COLUMNA'.

        Parámetros:
        - column: nombre de la columna.

        Retorno:
        - Retorna una instancia de la clase USQLQuery.
        '''
        self.query += f"ELIMINA LA COLUMNA {column} "
        return self

    def build(self):

        '''
        Método build.
        Este método construye la consulta USQL.

        Parámetros:
        - No tiene parámetros.

        Retorno:
        - Retorna la consulta USQL.
        '''
        
        return self.query.strip() + ";"
