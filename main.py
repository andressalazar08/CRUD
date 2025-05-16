from flask import Flask, request, render_template, url_for, redirect 

app =Flask(__name__)

usuarios=[]
id_contador=1

@app.route("/",methods=["GET","POST"])
def crud():
    global id_contador
    
    if request.method=='POST': #Si accedemos a la ruta con datos en el formulario
        nombre=request.form.get("nombre")
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


if __name__=="main":
	app.run(debug=True)