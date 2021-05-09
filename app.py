from flask import Flask,render_template, request
from flaskext.mysql import MySQL
  
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
  
    app.run()