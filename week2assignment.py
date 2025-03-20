my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)#you can add all of them at once by using .extend
my_list.insert(1,15)
another_list=[50,60,70]
my_list.extend(another_list)
my_list.remove(70)
my_list.sort
value=30
if value in my_list:
    print('value is present and its index is',my_list.index(value))