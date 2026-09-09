

import sqlite3


def main():

    db = sqlite3.connect("information.db")
    db.row_factory = sqlite3.Row
    db.execute("create table if not exists Admin(Name text , Age int)")
    db.execute("insert into Admin(Name , Age) values (?,?)",("Amir",28))
    db.commit()
    cusros = db.execute("select * from Admin")
    for Row in cusros:
        print("Name: {} \n Age: {}".format(Row[0],Row[1]))


if __name__ == '__main__': main()

