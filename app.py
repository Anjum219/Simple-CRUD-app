from flask import Flask, render_template, request
from flaskext.mysql import MySQL
  
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'simple_app'
 
mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/') 
@app.route('/enter', methods = ['POST', 'GET'])
def enter():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        userDetails = request.form
        first_name = userDetails['first_name']
        last_name = userDetails['last_name']
        email = userDetails['email']
        mobile_no = userDetails['mobile_no']
        cursor = mysql.get_db().cursor()
        cursor.execute(''' INSERT INTO users VALUES(%s, %s, %s, %s)''', (first_name, last_name, email, mobile_no))
        mysql.connection.commit()
        cursor.close()
        return "Done!!"

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8000)