from flask import Flask,render_template,url_for,request
import mysql.connector
import yaml
from user import User
from classes import Classes


app = Flask(__name__)
db = yaml.safe_load(open('db.yaml'))

mydb = mysql.connector.connect(
  host=db['mysql_host'],
  user=db['mysql_user'],
  password=db['mysql_password'],
  database=db['mysql_db'],
  port = db['mysql_port']
)

userDataBase = User(mydb)
classesDataBase = Classes(mydb)


#home
@app.route('/users')
def home():
    return render_template('/index.html',data =[])


#Get All Endpoint
@app.route('/users/getAll',methods = ['POST','GET'])
def getAll():
    return render_template('index.html',data = userDataBase.getAll())

# findbyid endpoint
@app.route('/users/findbyid', methods=['POST', 'GET'])
def findbyid():
    if request.method == 'POST':
        return '{}'.format(userDataBase.findById(request.form['id']))


#create endpoint
@app.route('/users/create',methods=['POST','GET'])
def create():
    if request.method == 'POST':
        return userDataBase.create(list(request.form.values()))


#delete Endpoint
@app.route('/users/delete',methods = ['POST','GET'])
def delete():
    if request.method == 'POST':
        return userDataBase.delete(request.form['id'])



#reset password endpoint With email And Old Password And New Password
@app.route('/users/resetpassword',methods=['POST','GET'])
def resetpassword():
    if request.method == 'POST':
        userDataBase.resetPassword(request.form['email'],request.form['oldPassword'],request.form['newPassword'])
        return ''

#user login  endpoint
@app.route('/users/login',methods =['POST','GET'])
def login():
    if request.method == 'POST':
        return userDataBase.user_login(request.form['email'],request.form['password'])




#update Endpoint
@app.route('/users/update',methods = ['POST','GET'])
def update():
    # if request.method =='POST':
        userDataBase.update(list(request.form.values()))
        return ''



###Classes

#Get All Endpoint
@app.route('/classes/getAll',methods = ['POST','GET'])
def classes_getAll():
    return render_template('index.html',data = classesDataBase.getAll())


#create classes endpoint
@app.route('/classes/create',methods=['POST','GET'])
def classes_create():
    if request.method == 'POST':
        return classesDataBase.create(list(request.form.values()))


#update Endpoint
@app.route('/classes/update',methods = ['POST','GET'])
def classes_update():
    if request.method =='POST':
        classesDataBase.update(list(request.form.values()))
        return ''


#delete Endpoint
@app.route('/classes/delete',methods = ['POST','GET'])
def classes_delete():
    if request.method == 'POST':
        return classesDataBase.delete(request.form['id'])

if __name__ == "__main__":
    app.run(debug=True)