from flask import Flask, request, render_template, url_for, redirect 

app =Flask(__name__)

usuarios=[]
id_contador=1

@app.route("/",methods=["GET","POST"])
def crud():
    global id_contador
    
    if request.method=='POST': #Si accedemos a la ruta con datos en el formulario
        nombre=request.form.get("nombre") #guarda en una variable de python lo que el usuario entrega en el form
        correo=request.form.get("correo")
        usuarios.append({"id":id_contador,"nombre_usuario":nombre,"correo_usuario":correo}) # insertando un usuario
        id_contador+=1
        return redirect(url_for("crud"))
    
    id_eliminar=request.args.get("borrar") #Siempre queda como texto
    if id_eliminar: #si me entregan un id a eliminar
        #TODO: Eliminar el usuario con el id del parametro de la lista
        for item in usuarios:
            if str(item['id'])==id_eliminar:
                usuarios.remove(item)
                break
        return redirect(url_for("crud")) #Llamar al nombre de la función    
       
    return render_template("registro.html",usuarios=usuarios) #lista que entregamos al html

#Ruta de actualización de los datos del usuario
@app.route("/update/<int:id>",methods=['GET', 'POST']) #Ruta con parámetros
def update(id):
    print(usuarios) #esta es la lista global
    estudiante_a_editar=''
    #TODO: identificar el diccionario del usuario con id entregado
    for diccionario in usuarios:
        if diccionario['id']==id:
            estudiante_a_editar=diccionario
            print("El estudiante a editar es: ", estudiante_a_editar)
            break
    
    if request.method=='POST':
        #TODO:actualizar el diccionario del estudiante con los datos del formulario
        estudiante_a_editar['nombre_usuario']=request.form.get('nombre')
        estudiante_a_editar['correo_usuario']=request.form.get('correo')
        return redirect(url_for("crud"))
    
    #Si despues de recorrer toda la lista, no encontramos el id entregado
    if estudiante_a_editar=='':
        return f"no existe el usuario con id: {id}" #Salgo de la función
    
    return render_template("editar.html",estudiante_a_editar=estudiante_a_editar)
    
if __name__=="main":
	app.run(debug=True)