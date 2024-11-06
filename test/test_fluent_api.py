# test_fluent_api.py
# Pruebas unitarias para fluent_api.py

import unittest
from src.fluent_api import USQLQuery

class TestFluentAPI(unittest.TestCase):

    def test_select(self):
        query = USQLQuery().traeme("TODO").de_la_tabla("usuarios").donde("edad > 18").build()
        expected = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"
        self.assertEqual(query, expected)

    def test_select_distinct(self):
        query = USQLQuery().traeme("LOS DISTINTOS nombre").de_la_tabla("clientes").donde("ciudad = 'Madrid'").build()
        expected = "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';"
        self.assertEqual(query, expected)

    def test_insert(self):
        query = USQLQuery().mete_en("usuarios", ["nombre", "edad"]).los_valores(["Juan", 25]).build()
        expected = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        self.assertEqual(query, expected)

    def test_update(self):
        query = USQLQuery().actualiza("empleados").setea({"salario": 3000}).donde("puesto = 'ingeniero'").build()
        expected = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        self.assertEqual(query, expected)

    def test_select_with_join(self):
        query = USQLQuery().traeme("TODO").de_la_tabla("pedidos").mezclando("clientes").en("pedidos.cliente_id = clientes.id").donde("clientes.ciudad = 'Barcelona'").build()
        expected = "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';"
        self.assertEqual(query, expected)

    def test_select_with_group_by(self):
        query = USQLQuery().traeme("CONTANDO(TODO)").de_la_tabla("ventas").agrupando_por("producto").where_del_group_by("COUNT(*) > 5").build()
        expected = "TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5;"
        self.assertEqual(query, expected)

    def test_delete(self):
        query = USQLQuery().borra_de_la("clientes").donde("edad ENTRE 18 Y 25").build()
        expected = "BORRA DE LA TABLA clientes DONDE edad ENTRE 18 Y 25;"
        self.assertEqual(query, expected)

    def test_alter_table_add_column(self):
        query = USQLQuery().cambia("empleados").agrega_columna("direccion VARCHAR(255) NO NULO").build()
        expected = "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;"
        self.assertEqual(query, expected)

    def test_alter_table_drop_column(self):
        query = USQLQuery().cambia("empleados").elimina_columna("direccion").build()
        expected = "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;"
        self.assertEqual(query, expected)

    

if __name__ == '__main__':
    unittest.main()
