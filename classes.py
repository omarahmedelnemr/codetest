from sqldataparser import SQLDataParser

class Classes(SQLDataParser):
    def __init__(self,db):
        self.db =db

    #clean data ,convert String int To INT ,Remove The Submit Data
    def clean(self,li):
        li[1] = int(li[1])
        li[2] = int(li[2])
        li = li[:-1]
        return li

    def getAll(self):
        return self.runSqlCommand("SELECT * FROM classes")

    def create(self,dataTuple):
        try:
            dataTuple = self.clean(dataTuple)
            self.runSqlCommand("INSERT INTO classes VALUES{}".format(tuple(dataTuple)))
            return "Success"
        except:
            return "Filed !"

    def delete(self,id):
        return self.runSqlCommand("DELETE FROM classes WHERE id = '{}'".format(id))

    def update(self,dataList):
        try:
            dataList = self.clean(dataList)
            self.runSqlCommand("UPDATE classes SET name = '{}',grade = {},year = {},stage = '{}',type = '{}',teacher = '{}',notes = '{}',school = '{}' WHERE name = '{}'".format(dataList[0],dataList[1],dataList[2],dataList[3],dataList[4],dataList[5],dataList[6],dataList[7],dataList[0]))
            return "Success"
        except:
            return "Filed !"