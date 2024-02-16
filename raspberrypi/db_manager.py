import mysql.connector
from flask import jsonify


class db:
    def __init__(self, user, pwd, url, db):
        self.connection = mysql.connector.connect(user=user, password=pwd, host=url, database=db)

    def select(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        row_headers=[x[0] for x in cursor.description]
        json_data = []
        for result in cursor.fetchall():
            json_data.append(dict(zip(row_headers, result)))
        cursor.close()
        return jsonify(json_data)
    
    def insert(self, elements, table, col):
        columns = col.split(', ')
        placeholders = ', '.join(['%s'] * len(columns))
        query = 'INSERT INTO ' + table + ' (' + ', '.join(columns) + ') VALUES (' + placeholders + ')'
        cursor = self.connection.cursor()
        cursor.execute(query, elements)
        self.connection.commit()
        cursor.close()
        return 'Insert was successful!', 200
