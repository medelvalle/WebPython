from flask import Flask, render_template, request, redirect, url_for
# importamos el modulo para acceder a los directorios
import os
#importamos la base de datos
import database as db

#definimos las rutas absolutas del proyecto
template_dir= os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
#unimos las rutas de la carpetas src y templates
template_dir= os.path.join(template_dir, "WebCaC","template")
#indicamos que busque el archivo index.html, lo hace al lanzar la app
app=Flask(__name__,template_folder=template_dir)

#generamos la primer ruta de la app
#@app.route('/') . el decorador vincula una funcion con un sitio web. Representa el elemento raiz del sitio o homepage
#importante es en la primer linea, importar render_template

@app.route('/')
def home():
    cursor= db.database.cursor() #traemos la conexion de la base
    cursor.execute("select * FROM usuarios") #ejecutamos la BD
    miResultado= cursor.fetchall() # toma todos los registros devueltos de la consulta

    #convertir los datos al diccionario
    insertarObjetos= []
    nombreDeColumnas= [columna[0] for columna in cursor.description] #armamos las columnas

    for unRegistro in miResultado: #recorremos y vamos insertando a la lista
        insertarObjetos.append(dict(zip(nombreDeColumnas,unRegistro)))#convertimos a diccionario

    cursor.close()    
    return render_template('index.html', data=insertarObjetos)

#Metodos para las paginas web internas
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/AI')
def AI():
    cursor= db.database.cursor() #traemos la conexion de la base
    cursor.execute("select * FROM usuarios") #ejecutamos la BD
    miResultado= cursor.fetchall() # toma todos los registros devueltos de la consulta
    #convertir los datos al diccionario
    insertarObjetos= []
    nombreDeColumnas= [columna[0] for columna in cursor.description] #armamos las columnas
    for unRegistro in miResultado: #recorremos y vamos insertando a la lista
        insertarObjetos.append(dict(zip(nombreDeColumnas,unRegistro)))#convertimos a diccionario
    cursor.close()
    return render_template('AI.html', data=insertarObjetos)

@app.route('/web')
def web():
    return render_template('desarrollo.html')

@app.route('/bigData')
def bigData():
    return render_template('bigdata.html')

@app.route('/cloud')
def cloud():
    return render_template('cloudcomunity.html')

# Metodo para agregar usuarios
@app.route('/usuario', methods=['POST'])
def addUser():
    nombre=request.form['nombre']
    empresa=request.form['empresa']
    vacantes=request.form['vacantes']

    if nombre and empresa and vacantes:
        cursor=db.database.cursor()
        sql="INSERT INTO usuarios (nombre, empresa, vacantes) VALUES (%s, %s, %s)"
        data=(nombre,empresa,vacantes)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('AI'))

@app.route('/eliminar/<string:id>')
def eliminar(id):
    cursor=db.database.cursor()
    sql="DELETE FROM usuarios WHERE id=%s"
    data=(id,)
    cursor.execute(sql,data)
    db.database.commit()
    return redirect(url_for('AI'))

@app.route('/editar/<string:id>', methods=['POST'])
def edit(id):
    nombre=request.form['nombre']
    empresa=request.form['empresa']
    vacantes=request.form['vacantes']

    if nombre and empresa and vacantes:
        cursor=db.database.cursor()
        sql="UPDATE usuarios SET nombre = %s, empresa = %s, vacantes = %s WHERE id=%s"
        data=(nombre, empresa, vacantes, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('AI'))

#ejecucion al servidor localhost 4000
if __name__=='__main__':
    app.run(debug=True,port=4000)




