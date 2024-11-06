import sqlite3

class Database:

    '''
    Database class
    This class creates an sqlite database in memory.

    Attributes:
    - conn: Connection to the database.
    - cursor: Cursor to interact with the database.

    Tables:
    - usuarios: Contains the name and age of users.
    - clientes: Contains the name, city and age of clients.
    - empleados: Contains the salary and position of employees.
    - pedidos: Contains the id of the client who made the order.
    - ventas: Contains the product sold.
    '''

    def __init__(self):

        '''
        Database class constructor
        This method creates a connection to the database and a cursor to interact with it.
        '''

        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

    def create_tables_and_insert_data(self):

        '''
        create_tables_and_insert_data method
        This method creates the tables in the database and inserts data in them

        parameters:
        - None

        returns:
        - None
        '''

        self.cursor.execute('''
        CREATE TABLE usuarios (
            nombre TEXT,
            edad INTEGER
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            ciudad TEXT,
            edad INTEGER
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE empleados (
            salario INTEGER,
            puesto TEXT
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            FOREIGN KEY(cliente_id) REFERENCES clientes(id)
        )
        ''')

        self.cursor.execute('''
        CREATE TABLE ventas (
            producto TEXT
        )
        ''')

        # Inserción de datos en 'usuarios'
        self.cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25)")
        self.cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Ana', 20)")
        self.cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Luis', 17)")
        self.cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('María', 30)")

        # Inserción de datos en 'clientes'
        self.cursor.execute("INSERT INTO clientes (nombre, ciudad, edad) VALUES ('Carlos', 'Madrid', 22)")
        self.cursor.execute("INSERT INTO clientes (nombre, ciudad, edad) VALUES ('Elena', 'Barcelona', 28)")
        self.cursor.execute("INSERT INTO clientes (nombre, ciudad, edad) VALUES ('Pedro', 'Madrid', 19)")
        self.cursor.execute("INSERT INTO clientes (nombre, ciudad, edad) VALUES ('Lucía', 'Sevilla', 32)")

        # Inserción de datos en 'empleados'
        self.cursor.execute("INSERT INTO empleados (salario, puesto) VALUES (2500, 'ingeniero')")
        self.cursor.execute("INSERT INTO empleados (salario, puesto) VALUES (2000, 'analista')")
        self.cursor.execute("INSERT INTO empleados (salario, puesto) VALUES (3000, 'ingeniero')")
        self.cursor.execute("INSERT INTO empleados (salario, puesto) VALUES (1500, 'técnico')")

        # Inserción de datos en 'pedidos'
        self.cursor.execute("INSERT INTO pedidos (cliente_id) VALUES (1)")
        self.cursor.execute("INSERT INTO pedidos (cliente_id) VALUES (2)")
        self.cursor.execute("INSERT INTO pedidos (cliente_id) VALUES (3)")
        self.cursor.execute("INSERT INTO pedidos (cliente_id) VALUES (1)")

        # Inserción de datos en 'ventas'
        productos = ['Producto A', 'Producto B', 'Producto A', 'Producto C', 'Producto A',
                    'Producto A', 'Producto B', 'Producto A', 'Producto A', 'Producto D', 'Producto A']
        for producto in productos:
            self.cursor.execute("INSERT INTO ventas (producto) VALUES (?)", (producto,))

        self.conn.commit()

