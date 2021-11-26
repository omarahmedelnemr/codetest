class  SQLDataParser:
    def __init__(self):
        pass

    def runSqlCommand(self,command):
        cursor = self.db.cursor()
        cursor.execute(command)
        data = cursor.fetchall()
        cursor.close()
        return data
