import unittest
from src.usql_parser import parser

class TestUSQLParser(unittest.TestCase):

    def test_select(self):
        query = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"
        result = parser.parse(query)
        expected = "SELECT * FROM usuarios WHERE edad > 18;"
        self.assertEqual(result, expected)

    def test_select_distinct(self):
        query = "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';"
        result = parser.parse(query)
        expected = "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid';"
        self.assertEqual(result, expected)

    def test_insert(self):
        query = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        result = parser.parse(query)
        expected = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25);"
        self.assertEqual(result, expected)

    def test_update(self):
        query = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        result = parser.parse(query)
        expected = "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero';"
        self.assertEqual(result, expected)

    def test_select_with_join(self):
        query = "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';"
        result = parser.parse(query)
        expected = "SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = 'Barcelona';"
        self.assertEqual(result, expected)

    def test_select_with_group_by(self):
        query = "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5;"
        result = parser.parse(query)
        expected = "SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5;"
        self.assertEqual(result, expected)

    def test_delete(self):
        query = "BORRA DE LA TABLA clientes DONDE edad ENTRE 18 Y 25;"
        result = parser.parse(query)
        expected = "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25;"
        self.assertEqual(result, expected)

    def test_alter_table_add_column(self):
        query = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;"
        result = parser.parse(query)
        expected = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;"
        self.assertEqual(result, expected)

    def test_alter_table_drop_column(self):
        query = "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;"
        result = parser.parse(query)
        expected = "ALTER TABLE empleados DROP COLUMN direccion;"
        self.assertEqual(result, expected)

    def test_invalid_query(self):
        query = "TRAEME TODO DE TABLA usuarios edad > 18"
        with self.assertRaises(SyntaxError):
            parser.parse(query)
    
    def test_invalid_query2(self):
        query = "dasfwge"
        with self.assertRaises(SyntaxError):
            parser.parse(query)

if __name__ == '__main__':
    unittest.main()
