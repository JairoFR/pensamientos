import os
from flask_app.config.mysqlconnection import connectToMySQL

class BaseModelo:

    @classmethod
    def get_all(cls):
        query = f"SELECT * FROM {cls.modelo} ;"
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query)
        return results
    
    @classmethod
    def destroy(cls, id):

        query  = f"DELETE FROM {cls.modelo} WHERE id = %(id)s;"
        data = { 'id' : id }
        return connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query,data)
    
    @classmethod
    def save(cls, data ):
        
        columnas = ''
        filas = ''
        for columna in cls.columnas_tabla:
            columnas +=columna + ', '
            filas += f'%({columna})s ,' 
  
        query = f"INSERT INTO {cls.modelo} ( {columnas}created_at, updated_at ) VALUES ( {filas}NOW() , NOW() );"
        resultado = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db( query, data ) 
        return resultado
    
    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM {cls.modelo} where id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)

        return cls(results[0]) if len(results) > 0 else None 
    
