from flask import render_template, url_for, flash, redirect, request, jsonify
from forms import LoginContrasena

def init_app(app):

    @app.route("/")
    def inicio():
        form = LoginContrasena()
        return render_template('inicio.html', form=form)

    @app.route("/login", methods=['POST'])
    def login():
        form = LoginContrasena(request.form)
        if form.validate_on_submit():
            user_email = form.email.data
            user_pass = form.contrasena.data
            
            # Aquí se verifica si las credenciales son correctas
            if user_email == 'ejemplo@correo.com' and user_pass == '12345678':
                return jsonify({'success': True})
            else:
                return jsonify({'success': False, 'message': 'Correo electrónico o contraseña incorrectos'}), 401

        else:
            # Filtrando los errores para solo incluir aquellos relevantes para el usuario
            errores = {campo.name: campo.errors for campo in form if campo.name in ['email', 'contrasena']}
            return jsonify({'success': False, 'errors': errores}), 400

    @app.route("/dashboard")
    def dashboard():
        return render_template('inicioDashBoard.html')

        

