
# lambda انشاء دالة
sume = lambda x,y : x+y
print(sume(5,6))
############################################################################
Mylist = [56,573,6,8,12,58,69,3,52,47,89,36,58,521,5,865,87,5]
odd_number = list(filter(lambda x : x%2 ,Mylist))
print(odd_number)

even_numbers = list(filter(lambda x : x%2 == 0 ,Mylist))
print(even_numbers)


#############################################################################
# mab تساعد على تطبيق دالة على جميع عناصر قائمة
square_numbers = list(map(lambda x : x ** 2 ,Mylist))
print(square_numbers)