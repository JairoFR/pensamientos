import os
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.base_modelo import BaseModelo
from flask_bcrypt import Bcrypt        




class Pensamiento(BaseModelo): #Cambiar a nombre de modelo en singular  

    modelo = 'pensamientos' #nombre de tabla
    columnas_tabla = ['usuario_id', 'pensamiento'] #campos de columnas sin creted_at y update_at

    def __init__( self , data ):
        self.id = data['id']
        self.usuario_id= data['usuario_id']  
        self.pensamiento = data['pensamiento']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_pensamientos(cls):
        query = "SELECT * FROM pensamientos JOIN usuarios ON pensamientos.usuario_id = usuarios.id  ORDER BY pensamientos.id  Desc;"
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query)
        return results
    
    
    @classmethod
    def get_pensamientos_by_id(cls, data):
        query = f"SELECT * FROM pensamientos JOIN usuarios ON pensamientos.usuario_id = usuarios.id  WHERE usuarios.id = %(data)s;"
        data = { 'data' : data }
       
        results = connectToMySQL(os.environ.get("BASE_DATOS_NOMBRE")).query_db(query, data)
  
        return results

    @staticmethod
    def validar_pensamiento(data):
        is_valid = True

        if  (len(data['pensamiento']) < 5) or (len(data['pensamiento'])> 255):
            flash("pensamiento debe contener mas de 5  y menos de 255 caracteres.","error")
            is_valid=False
        
        return is_valid