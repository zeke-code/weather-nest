import mysql.connector
from flask import jsonify, current_app

class db_manager:
    def __init__(self, user, pwd, url, db):
        self.connection = mysql.connector.connect(
            user=current_app.config['MYSQL_USER'],
            pwd=current_app.config['MYSQL_PASSWORD'],
            url=current_app.config['MYSQL_HOST'],
            db=current_app.config['MYSQL_DB'],
        )

    def select(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        row_headers=[x[0] for x in cursor.description]
        json_data=[]
        for result in cursor.fetchall():
            json_data.append(dict(zip(row_headers, result)))
        cursor.close()
        return jsonify(json_data)
    
    def insert(self, elements, table, cols):
        cursor = self.connection.cursor()
        placeholders = ', '.join(['%s'] * len(elements[0]))
        query = 'INSERT INTO {} ({}) VALUES ({})'.format(table, cols, placeholders)
        for element in elements:
            cursor.execute(query, element)
        self.connection.commit()
        cursor.close()
        return 'Insert was successful!', 200
