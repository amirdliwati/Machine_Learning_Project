import pymysql

mydb = pymysql.connect(host="localhost",user="root",passwd="",database="pythondb")
cursor = mydb.cursor()

insert = "INSERT INTO `users_python` (`id_users`, `users_Names`) VALUES ('105', 'subhi');"
cursor.execute(insert)
mydb.commit()

update = "UPDATE `users_python` SET `id_users` = '5' WHERE `users_python`.`id_users` = 1;"
cursor.execute(update)
mydb.commit()

deletedata = "DELETE FROM `users_python` WHERE `users_python`.`id_users` = 10"
cursor.execute(deletedata)
mydb.commit()

selectdata = "select * from users_python"
cursor.execute(selectdata)
rows = cursor.fetchall()
for r in rows:
    print(r[0])
print(type(r))
mydb.commit()



mydb.close()

