import os
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.pensamiento import Pensamiento
from flask_app.models.like import Like



@app.route("/pensamientos")
def index():

    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')

    nombre_sistema = os.environ.get("NOMBRE_SISTEMA")
    pensamientos = Pensamiento.get_pensamientos()  
    like= Like.get_all()  
    return render_template("index.html", sistema=nombre_sistema, pensamientos=pensamientos, like=like)

@app.route('/procesar_pensamientos', methods=['POST'])
def procesar_pensamientos():
    
    data = {
        'usuario_id' : request.form['usuario_id'],
        'pensamiento' : request.form['pensamientos']
    }

    if not Pensamiento.validar_pensamiento(data):
        return redirect('/')
    
    Pensamiento.save(data)
    flash('Pensamiento agregado con exito', 'success')
    return redirect('/pensamientos')

@app.route('/destroy/<int:id>')
def destroy(id):

    Pensamiento.destroy(id)
    flash('Pensamiento eliminado con exito', 'success')
    return redirect('/pensamientos')

@app.route('/users/<int:id>')
def users(id):
    
    users = Pensamiento.get_pensamientos_by_id(id)
    return render_template('usuario.html', users=users)