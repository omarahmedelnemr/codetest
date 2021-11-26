from sqldataparser import SQLDataParser
class User(SQLDataParser):
    def __init__(self,db):
        self.db = db

    def getAll(self):
        return self.runSqlCommand("SELECT * FROM user")

    def findById(self,id):
        return self.runSqlCommand("SELECT * FROM user WHERE id ='{}'".format(id))

    def create(self,dataTuple):
        self.runSqlCommand("INSERT INTO user VALUES{}".format(dataTuple))

    def delete(self,id):
        self.runSqlCommand("DELETE FROM user WHERE id = '{}'".format(id))

    def resetPassword(self,id,newPassword):
        self.runSqlCommand("UPDATE user SET password = '{}' WHERE id = '{}'".format(newPassword,id))

    def update(self,id,dataList):
        self.runSqlCommand("UPDATE user SET first_name = '{}',last_name = '{}',username = '{}',email = '{}',phone = '{}',password = '{}',type = '{}',start = '{}',school = '{}',end = '{}',active = {},subject = '{}',specilization = '{}' WHERE id = '{}'".format(dataList[1],dataList[2],dataList[3],dataList[4],dataList[6],dataList[7],dataList[8],dataList[9],dataList[10],dataList[11],dataList[12],dataList[13],dataList[0]))
        #dataList[0] for ID

    def login(self,email,password):
        try:
            self.runSqlCommand("SELECT * FROM user WHARE email='{}' and password = '{}'".format(email,password))
        except:
            return "Wrong Data"