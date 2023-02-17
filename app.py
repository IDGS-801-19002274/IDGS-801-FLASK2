from flask import Flask, request, render_template

import forms

app = Flask(__name__)

@app.route('/calcular')
def calcular():
    return render_template("calcular.html")

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    registrar_Alumno = forms.UserForm(request.form)
    
    if request.method == 'POST':
        print(registrar_Alumno.matricula.data)
        print(registrar_Alumno.nombre.data)
        print(registrar_Alumno.apaterno.data)
        print(registrar_Alumno.email.data)
    
    return render_template('alumnos.html', form = registrar_Alumno)

if __name__ == "__main__":
    app.run(debug = True, port=3000)

