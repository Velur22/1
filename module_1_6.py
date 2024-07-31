my_dict = {'Egor':2000,'Misha':1993,'Ivan':2003}
print(my_dict)
print(my_dict['Egor'])
print(my_dict.get('Saha'))
my_dict.update({'Alex':2005,'Valentin':2002})
print(my_dict)
my_dict.pop('Egor')
print(my_dict)


my_set = {1,2,2,2,1,1,3,2}
print(my_set)
my_set.update({4,5})
print(my_set)
my_set.discard(2)
print(my_set)
