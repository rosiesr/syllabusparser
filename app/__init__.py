from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-value'
app.config['UPLOAD_EXTENSIONS'] = ['.pdf', '.txt', '.docx']
app.config['UPLOAD_PATH'] = 'uploads'

from app import routes