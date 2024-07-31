immutable_var = (1,2,'a','b')
print(immutable_var)
#immutable_var.append(4)
#print(immutable_var)
#immutable_var[0] = 3            Кортеж не поддерживает изменения элементов
#print(immutable_var)

mutable_list = [1,2,'a','b']
print(mutable_list)
mutable_list[0] = 2
print(mutable_list)
mutable_list[2] = 'C'
print(mutable_list)
mutable_list.append('Modified')
print(mutable_list)
mutable_list.remove('b')
print(mutable_list)
mutable_list.extend('self')
print(mutable_list)
mutable_list.extend(['self'])
print(mutable_list)