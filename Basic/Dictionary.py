my_dic1 = {"Name":"Amir","Age":28,"Edu":"Ph.D Computer Engineering"}
print(my_dic1.values())
print(my_dic1.keys())
print(my_dic1["Name"])
print(my_dic1)
print("Amir" in my_dic1.values())

my_dic2 = {"Names": ["Amir","Mahmoud","Aboud"], "Age": [28,29,27], "Country":["Alep","Damas","Idlib"]}
print(my_dic2.values())
print(my_dic2.keys())
print(my_dic2["Names"])
print(my_dic2)
print(my_dic2["Names"][0],my_dic2["Age"][0],my_dic2["Country"][0])

del my_dic2["Names"]
print(my_dic2)
my_dic2.clear()
print(my_dic2)

print(type(my_dic2))