import os
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_modelo import BaseModelo
from flask_bcrypt import Bcrypt        




class Like(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'likes' #nombre de tabla
    columnas_tabla = ['usuario_id', 'pensamiento_id', 'favorito'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.id = data['id']
        self.usuario_id= data['usuario_id']  
        self.pensamiento_id = data['pensamiento_id']
        self.favorito = data['favorito']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_id(cls, id):
        query = f"SELECT * FROM {cls.modelo} where pensamiento_id = %(id)s;"
        data = { 'id' : id }
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
        return cls(results[0]) if len(results) > 0 else None 
    
  