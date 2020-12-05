from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import SubmitField

class MyForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Submit')