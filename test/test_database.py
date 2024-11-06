import unittest
from src.database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Configuración inicial antes de cada prueba
        self.db = Database()
        self.db.create_tables_and_insert_data()

    def tearDown(self):
        # Cerramos la conexión después de cada prueba
        self.db.conn.close()

    def test_usuarios_data(self):
        # Verificar que los datos en la tabla 'usuarios' sean correctos
        self.db.cursor.execute("SELECT * FROM usuarios")
        rows = self.db.cursor.fetchall()
        expected = [('Juan', 25), ('Ana', 20), ('Luis', 17), ('María', 30)]
        self.assertEqual(rows, expected)

    def test_clientes_data(self):
        # Verificar que los datos en la tabla 'clientes' sean correctos
        self.db.cursor.execute("SELECT nombre, ciudad, edad FROM clientes")
        rows = self.db.cursor.fetchall()
        expected = [('Carlos', 'Madrid', 22), ('Elena', 'Barcelona', 28), ('Pedro', 'Madrid', 19), ('Lucía', 'Sevilla', 32)]
        self.assertEqual(rows, expected)

    def test_empleados_data(self):
        # Verificar que los datos en la tabla 'empleados' sean correctos
        self.db.cursor.execute("SELECT * FROM empleados")
        rows = self.db.cursor.fetchall()
        expected = [(2500, 'ingeniero'), (2000, 'analista'), (3000, 'ingeniero'), (1500, 'técnico')]
        self.assertEqual(rows, expected)

    def test_pedidos_data(self):
        # Verificar que los datos en la tabla 'pedidos' sean correctos
        self.db.cursor.execute("SELECT cliente_id FROM pedidos")
        rows = self.db.cursor.fetchall()
        expected = [(1,), (2,), (3,), (1,)]
        self.assertEqual(rows, expected)

    def test_ventas_data(self):
        # Verificar que los datos en la tabla 'ventas' sean correctos
        self.db.cursor.execute("SELECT producto FROM ventas")
        rows = self.db.cursor.fetchall()
        expected = [('Producto A',), ('Producto B',), ('Producto A',), ('Producto C',), ('Producto A',),
                    ('Producto A',), ('Producto B',), ('Producto A',), ('Producto A',), ('Producto D',), ('Producto A',)]
        self.assertEqual(rows, expected)

    def test_usuarios_edad_mayores_de_18(self):
        # Consulta que obtenga a los usuarios mayores de 18 años
        self.db.cursor.execute("SELECT nombre FROM usuarios WHERE edad > 18")
        rows = self.db.cursor.fetchall()
        expected = [('Juan',), ('Ana',), ('María',)]
        self.assertEqual(rows, expected)

    def test_pedidos_de_cliente(self):
        # Consulta para obtener todos los pedidos del cliente con ID = 1
        self.db.cursor.execute("SELECT id FROM pedidos WHERE cliente_id = 1")
        rows = self.db.cursor.fetchall()
        expected = [(1,), (4,)]
        self.assertEqual(rows, expected)

    def test_empleados_sueldo_mayor_a_2000(self):
        # Consulta para obtener a los empleados con salario mayor a 2000
        self.db.cursor.execute("SELECT puesto FROM empleados WHERE salario > 2000")
        rows = self.db.cursor.fetchall()
        expected = [('ingeniero',), ('ingeniero',)]
        self.assertEqual(rows, expected)

if __name__ == '__main__':
    unittest.main()
