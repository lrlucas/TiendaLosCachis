from bottle import get, post, request, route, run, redirect, template, response
import json
import psycopg2
import waitress


# Todos lo productos
@route('/product-all')
def main():
    conn_string = "host='localhost' dbname='tienda_los_cachis' user='postgres' password='123'"
    print("Connecting to database\n	->%s " % (conn_string))
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("select * from productos")

    return {'data': cursor.fetchall()}


# Producto por Id
@route('/product-all/<id>')
def main2(id):
    sql = {
        'id_producto': '',
        'nombre': '',
        'precio': '',
        'descripcion': '',
        'autor': '',
        'contacto': '',
        'fecha': ''
    }
    conn_string = "host='localhost' dbname='tienda_los_cachis' user='postgres' password='123'"
    print("Connecting to database\n	->%s " % (conn_string))
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute('select * from productos where id_producto =' + id)
    data = cursor.fetchall()

    for productos in data:
        product = {
            'id_producto': productos[0],
            'nombre': productos[1],
            'precio': productos[2],
            'descripcion': productos[3],
            'autor': productos[4],
            'contacto': productos[5],
            'fecha': productos[6]

        }
        return {'data': product}


# Todos los usuarios
@route('/user-all')
def main():
    conn_string = "host='localhost' dbname='tienda_los_cachis' user='postgres' password='123'"
    print("Connecting to database\n	->%s " % (conn_string))
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("select * from usuario")
    data = cursor.fetchall()

    return {'data': data}


# Usuarios por id
@route('/user-all/<id>')
def main2(id):
    sql = {
        'id_usuario': '',
        'nombre': '',
        'edad': '',
        'pais': '',
        'telefono': '',
        'correo': ''
    }
    conn_string = "host='localhost' dbname='tienda_los_cachis' user='postgres' password='123'"
    print("Connecting to database\n	->%s " % (conn_string))
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute('select * from usuario where id_usuario=' + id)
    data = cursor.fetchall()

    for usuarios in data:
        usuario = {
            'id_usuario': usuarios[0],
            'nombre': usuarios[1],
            'edad': usuarios[2],
            'pais': usuarios[3],
            'telefono': usuarios[4],
            'correo': usuarios[5]

        }
        return {'data': usuario}


if __name__ == "__main__": run(
    host='192.168.0.16',
    port=8181,
    reloader=True,
    server='waitress'
)
# ip de la maquina conectada a wifi
# 192.168.0.16
