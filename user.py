from sqldataparser import SQLDataParser
class User(SQLDataParser):
    def __init__(self,db):
        self.db = db


    def getAll(self):
        return self.runSqlCommand("SELECT * FROM user")

    def findById(self,id):
        return self.runSqlCommand("SELECT * FROM user WHERE id ='{}'".format(id))


    def create(self,dataTuple):
        try:
            self.runSqlCommand("INSERT INTO user VALUES{}".format(dataTuple))
            return "Success"
        except:
            return "Filed !"


    def delete(self,id):
        self.runSqlCommand("DELETE FROM user WHERE id = '{}'".format(id))
        return "Done"

    def resetPassword(self,email,oldPassword,newPassword):
        self.runSqlCommand("UPDATE user SET password = '{}' WHERE email = '{}' and password = '{}'".format(newPassword,email,oldPassword))
        print("done")

    def user_login(self,email,password):
            if len(self.runSqlCommand("SELECT * FROM user WHERE email='{}' and password = '{}'".format(email,password))) ==0:
                return 'User Not Found'
            return 'Loged In'

    def update(self,dataList):
        try:
            self.runSqlCommand("UPDATE user SET first_name = '{}',last_name = '{}',username = '{}',email = '{}',phone = '{}',password = '{}',type = '{}',start = '{}',school = '{}',end = '{}',active = {},subject = '{}',specilization = '{}' WHERE id = '{}'".format(dataList[1],dataList[2],dataList[3],dataList[4],dataList[5],dataList[6],dataList[7],dataList[8],dataList[9],dataList[10],dataList[11],dataList[12],dataList[0]))
            return "Success"
        except:
            return "Filed !"

    def login(self,email,password):
        try:
            self.runSqlCommand("SELECT * FROM user WHARE email='{}' and password = '{}'".format(email,password))
        except:
            return "Wrong Data"