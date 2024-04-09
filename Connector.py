import json
import datetime
import mariadb

# create connection
def create_conn():
    conn_params= {
        "user" : "recomendador",
        "password" : "Y724VEGiLoFI",
        "host" : "alternativa-test.cuy74r3obobg.us-east-1.rds.amazonaws.com",
        "database" : "alternativa_db"
    }
    return mariadb.connect(**conn_params)

# close connection
def close_conn(connection):
    if (connection):
        connection.close()

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)

# select query
def get_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)

    # Obtén los nombres de las columnas
    column_names = [desc[0] for desc in cursor.description]

    rows = cursor.fetchall()
    json_data = []
    for row in rows:
        # Crea un diccionario para cada fila
        row_dict = {column: value for column, value in zip(column_names, row)}
        json_data.append(row_dict)

    cursor.close()
    return json_data