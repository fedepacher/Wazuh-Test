import sqlite3
from sqlite3 import Error

class Task5_2:

    def __init__(self, db_file):
        self._conn = self.create_connection(db_file)

    '''
    Create a database connection to the SQLite database specified by the db_file
    param db_file   database file
    return   Connection object or None
    '''
    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    '''
    Find all objects of the table
    param conn  the Connection object
    '''
    def findAllObjects(self, table):
        cur = self._conn.cursor()
        try:
            cur.execute(f'SELECT * FROM {table}')
        except Error as e:
            print(e)
            return None

        rows = cur.fetchall()
        return rows

    '''
    Find object in table 
    param conn          the Connection object
    param table         table name
    param column        table column to find content
    param data_content  data to be found
    '''
    def findObjectByColumn(self, table, column, data_content):
        cur = self._conn.cursor()
        try:
            cur.execute(f'SELECT * FROM {table} WHERE {column}=?', (data_content,))
        except Error as e:
            print(e)
            return None

        rows = cur.fetchall()
        return rows

    '''
    Return the amount of objects in the database
    param table         table name
    '''
    def countObjects(self, table):
        return len(self.findAllObjects(table))

    '''
    Check if column exist in data base
    param conn          the Connection object
    param table         table name
    return columns      list of columns
    '''
    def columnExist(self, table):
        cur = self._conn.cursor()
        columns = []
        try:
            columns = [i[1] for i in cur.execute(f'PRAGMA table_info({table})')]
        except Error as e:
            print(e)

        return columns
    
    '''
    Find column in table 
    param table         table name
    param column        table column to find content
    '''
    def getObjectByColumn(self, table, column):
        cur = self._conn.cursor()
        rows = []
        try:
            cur.execute(f'SELECT {column} FROM {table}')
            rows = [x[0] for x in cur.fetchall()]
        except Error as e:
            print(e)
                    
        return rows


    '''
    Close database connection
    '''
    def closeConn(self):
        self._conn.commit()
        self._conn.close()