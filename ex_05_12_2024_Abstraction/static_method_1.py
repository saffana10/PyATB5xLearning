class ExcelReader():

    @staticmethod
    def read_from_excel():
        print("Reading from excel")

class MySQLDBConnection():

    @staticmethod
    def readMYSQLfile():
        print("Reading from MYSQL")

class Tc():

    def testcase(self):
        MySQLDBConnection.readMYSQLfile()
        ExcelReader.read_from_excel()

tc = Tc()
tc.testcase()
