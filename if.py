first = int(input('первое значение'))
second = int(input('второе значение'))
third = int(input('третье значение'))
if first==second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else: print(0)