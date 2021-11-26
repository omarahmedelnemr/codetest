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

print(userDataBase.findById('1s5h6vduNUjSbqFRunkCkcNLStLX'))

#Get All Endpoint
@app.route('/users/getAll',methods = ['POST','GET'])
def getAll():
    print(userDataBase.convertToDic(userDataBase.getAll()))
    return userDataBase.convertToDic(userDataBase.getAll())



print(userDataBase.update('omar','elnemr','omasd_as',''))

#update Endpoint
@app.route('/users/update',methods = ['POST','GET'])
def update():
    if request.method =='POST':
        userDataBase.update(list(request.form.values()))

#create endpoint
@app.route('/users/create',methods=['POST','GET'])
def create():
    if request.method == 'POST':
        userDataBase.create(tuple(request.form))

#reset password endpoint
@app.route('/users/resetpassword',methods=['POST','GET'])
def resetpassword():
    if request.method == 'POST':
        userDataBase.create(request.form['id'],request.form['password'])

# findbyid endpoint
@app.route('/users/findbyid', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        userDataBase.findById(request.form['id'])
#update endpint()
@app.route('/users/update')
def update():
    if request.method == 'POST':
        userDataBase.update(request.form.values())


#user login  endpoint
@app.route('/users/login')
def login():
    if request.method == 'POST':
        userDataBase.login(request.form['email'],request.form['password'])

#delete Endpoint
@app.route('/users/delete',methods = ['POST','GET'])
def delete():
    if request.method == 'POST':
        userDataBase.delete(request.form['id'])
        return 'Deleted'



###Classes

#Get All Endpoint
@app.route('/classes/getAll',methods = ['POST','GET'])
def getAll():
    print(classesDataBase.getAll())
    return classesDataBase.getAll()



#update Endpoint
@app.route('/classes/update',methods = ['POST','GET'])
def update():
    if request.method =='POST':
        classesDataBase.update(list(request.form.values()))
#delete Endpoint
@app.route('/classes/delete',methods = ['POST','GET'])
def delete():
    if request.method == 'POST':
        classesDataBase.delete(request.form['id'])
        return 'Deleted'



if __name__ == "__main__":
    app.run(debug=True)