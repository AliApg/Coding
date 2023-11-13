import sqlite3 as db

ty = ["text", "int", "float", "list"]


def table(a):
    if type(a) != list:
        print("Your input must be a list!")
    else:
        while "tbname" not in locals() or tbname.lower() == "end":
            tbname = input("Enter Table Name: ")
            while tbname.strip() == "":
                tbname = input(
                    "Table name cannot be empty!\nEnter Table Name again: ")
            if tbname.lower() == "end":
                continue
            b = [tbname]
            while "column" not in locals() or column.lower() != "end":
                flag = False
                column = input("Enter column name: ")
                while column.strip() == "":
                    column = input("column name cannot be empty!\nTry Again: ")
                for i in b[1::2]:
                    if column == i:
                        flag = True
                        print('column name already exists!')
                        break
                if flag == True:
                    continue
                if column.lower() == "end":
                    continue
                coltype = input("enter your column data-type: ")
                while coltype not in ty:
                    coltype = input(
                        "the column data-type is invalid\nTry Again: ")
                b += [column, coltype]
            a.append(b)


class database:
    def __init__(self):
        self.tablenames = []

    def mkdb(self, database_name):
        self.dbname = database_name
        # self.make=db.connect(self.dbname+".db")
        # self.cr=self.make.cursor()
        self.cr = db.connect(f"{self.dbname}.db").cursor()

    def mktable(self):
        for i in self.tablenames:
            string = f'{i[0]} ('
            for j in range(1, len(i), 2):
                string += f'{i[j]} {i[j + 1]},'
            string = f'{string[:-1]})'
            self.cr.execute(f"create table {string}")


obj = database()
obj.mkdb("mydb")
table(obj.tablenames)
obj.mktable()
