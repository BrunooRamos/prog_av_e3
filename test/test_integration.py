import unittest
from src.database import Database
from src.fluent_api import USQLQuery
from src.usql_parser import parser

class TestIntegration(unittest.TestCase):

    def setUp(self):
        # Inicializamos la base de datos en memoria
        self.db = Database()
        self.db.create_tables_and_insert_data()

    def tearDown(self):
        # Cerramos la conexión a la base de datos
        self.db.conn.close()

    def execute_query(self, usql_query):
        """Función de utilidad para integrar la Fluent API y el parser."""
        # Convertimos la consulta Fluent API a USQL
        usql = usql_query.build()
        
        # Parseamos el USQL a SQL usando el parser
        sql_query = parser.parse(usql)
        
        # Ejecutamos la consulta en la base de datos
        self.db.cursor.execute(sql_query)
        return self.db.cursor.fetchall()

    def test_select_usuarios_mayores_18(self):
        # Consulta usando Fluent API
        query = USQLQuery().traeme("TODO").de_la_tabla("usuarios").donde("edad > 18")
        
        # Ejecutamos la consulta integrada (Fluent API -> Parser -> SQL -> DB)
        result = self.execute_query(query)

        # Verificamos que los resultados sean correctos
        expected = [('Juan', 25), ('Ana', 20), ('María', 30)]
        self.assertEqual(result, expected)

    def test_select_distintos_nombres_clientes_en_madrid(self):
        # Consulta usando Fluent API
        query = USQLQuery().traeme("LOS DISTINTOS nombre").de_la_tabla("clientes").donde("ciudad = 'Madrid'")
        
        # Ejecutamos la consulta
        result = self.execute_query(query)

        # Verificamos que los resultados sean correctos
        expected = [('Carlos',), ('Pedro',)]
        self.assertEqual(result, expected)

    def test_insert_nuevo_usuario(self):
        # Insertar un nuevo usuario usando Fluent API
        query = USQLQuery().mete_en("usuarios", ["nombre", "edad"]).los_valores(["Sofia", 22])
        
        # Ejecutamos la consulta de inserción
        self.execute_query(query)

        # Verificamos que el usuario fue insertado
        self.db.cursor.execute("SELECT nombre, edad FROM usuarios WHERE nombre = 'Sofia'")
        result = self.db.cursor.fetchall()
        expected = [('Sofia', 22)]
        self.assertEqual(result, expected)

    def test_update_salario_empleados(self):
        # Actualizar salarios de los empleados ingenieros
        query = USQLQuery().actualiza("empleados").setea({"salario": 3000}).donde("puesto = 'ingeniero'")
        
        # Ejecutamos la consulta de actualización
        self.execute_query(query)

        # Verificamos que los salarios fueron actualizados
        self.db.cursor.execute("SELECT salario FROM empleados WHERE puesto = 'ingeniero'")
        result = self.db.cursor.fetchall()
        expected = [(3000,), (3000,)]
        self.assertEqual(result, expected)

    def test_select_pedidos_con_join_clientes(self):
        # Seleccionar pedidos con un JOIN sobre la tabla de clientes
        query = USQLQuery().traeme("TODO").de_la_tabla("pedidos").mezclando("clientes").en("pedidos.cliente_id = clientes.id").donde("clientes.ciudad = 'Barcelona'")
        
        # Ejecutamos la consulta
        result = self.execute_query(query)

        # Verificamos que los resultados sean correctos
        expected = [(2, 2, 2, 'Elena', 'Barcelona', 28)]
        self.assertEqual(result, expected)

    def test_select_ventas_agrupadas_por_producto(self):
        # Seleccionar ventas agrupadas por producto
        query = USQLQuery().traeme("CONTANDO(TODO)").de_la_tabla("ventas").agrupando_por("producto").where_del_group_by("COUNT(*) > 5")
        
        # Ejecutamos la consulta
        result = self.execute_query(query)

        # Verificamos que los resultados sean correctos
        expected = [(7,)]
        self.assertEqual(result, expected)

    def test_delete_clientes_jovenes(self):
        # Borrar clientes cuya edad esté entre 18 y 25
        query = USQLQuery().borra_de_la("clientes").donde("edad ENTRE 18 Y 25")
        
        # Ejecutamos la consulta de eliminación
        self.execute_query(query)

        # Verificamos que los clientes fueron eliminados
        self.db.cursor.execute("SELECT nombre FROM clientes WHERE edad BETWEEN 18 AND 25")
        result = self.db.cursor.fetchall()
        expected = []  # Esperamos que no haya clientes en este rango de edad
        self.assertEqual(result, expected)

    def test_add_column_direccion_empleados(self):
        # Agregar columna 'direccion' a la tabla de empleados
        query = USQLQuery().cambia("empleados").agrega_columna("direccion VARCHAR(255)")
        
        # Ejecutamos la consulta de alteración de tabla
        self.execute_query(query)

        # Verificamos que la columna fue añadida
        self.db.cursor.execute("PRAGMA table_info(empleados)")
        result = self.db.cursor.fetchall()
        expected = [(0, 'salario', 'INTEGER', 0, None, 0), (1, 'puesto', 'TEXT', 0, None, 0), (2, 'direccion', 'VARCHAR(255)', 0, None, 0)]
        self.assertEqual(result, expected)

    def test_invalid_query(self):
        # Consulta inválida
        query = USQLQuery().de_la_tabla("empleados").donde("salario 3000")
        
        # Ejecutamos la consulta
        with self.assertRaises(SyntaxError):
            self.execute_query(query)

if __name__ == '__main__':
    unittest.main()
