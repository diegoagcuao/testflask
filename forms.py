from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginContrasena(FlaskForm):
    email = StringField(
        'Correo Electrónico', 
        validators=[
            DataRequired(message="Debe ingresar un correo"), 
            Email(message="Debe ingresar un correo valido")
        ],
        render_kw={
            "class": "form-control", 
            "placeholder": "Correo electronico"
        }
    )
    contrasena = PasswordField(
        'Contraseña', 
        validators=[
            DataRequired(message="Debe ingresar una contraseña"), 
            Length(min=8, message="La contraseña debe tener al menos 6 caracteres.")
        ],
        render_kw={
            "class": "form-control", 
            "placeholder": "contraseña"}
    )
    submit = SubmitField(
        'Ingresar al sistema',
        render_kw={
            "class": "btn btn-primary"
        }
    )
