my_list1 = [1,5,8,65,845,36,52,1456,585,257,6,66,32]
print(my_list1)
my_list2 = [5,6,"Apple",[1,6]]
my_list3 = my_list1 + my_list2

print(my_list3)
print("Apple" in my_list3)

for item in my_list2:
    print(item)

print(my_list2[1])
print(my_list2[3][0])

print(max(my_list1))
print(min(my_list1))
print(len(my_list1))
print(sorted(my_list1))
my_list1.append(55)
print(my_list1)
my_list1.extend(my_list2)
print(my_list1)

del my_list2[1]
print(my_list2)
my_list2.remove("Apple")
print(my_list2)

a = "this is my world"
my_list4 = a.split(' ')
print(my_list4)


my_list5 = [x**2 for x in range(5)]
print(my_list5)
my_list6 = my_list5 * 2
print(my_list6)

my_list7 = [1,5,6,1,9,8,7]
print(my_list7.index(6))
print(my_list7.count(1))
my_list7.reverse()
print(my_list7)
my_list7.insert(1,10)
print(my_list7)