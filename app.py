from flask import Flask

UPLOAD_FOLDER = '/Users/rosierothschild/syllabusparser/Uploads/'
#UPLOAD_FOLDER = '/Users/danielbolja/Documents/GitHub/syllabusparser/Uploads/'

app = Flask(__name__)
app.secret_key = "02894357029348750923847502934875"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024