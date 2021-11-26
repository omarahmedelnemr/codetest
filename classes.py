class Classes:
    def __init__(self,db):
        self.db =db

    def runSqlCommand(self,command):
        cursor = self.db.cursor()
        cursor.execute(command)
        data = cursor.fetchall()
        cursor.close()
        return data

    def getAll(self):
        return self.runSqlCommand("SELECT * FROM classes")

    def delete(self,id):
        return self.runSqlCommand("DELETE FROM classes WHERE id = '{}'".format(id))

    def update(self,id,dataList):
        self.runSqlCommand("UPDATE classes SET name = '{}',grade = '{}',year = '{}',stage = '{}',type = '{}',teacher = '{}',notes = '{}',school = '{}' WHERE id = '{}'".format(dataList[0],dataList[1],dataList[2],dataList[3],dataList[4],dataList[6],dataList[7],id))
