# my_list = ['name', 'string data', 6, 6.4, [7, 'surname', 7.9]]
# print(my_list[4][2])

# my_list = ['name', 'string data', 6, 6.4, [7, 'surname', 7.9]]
# print(my_list[1:4])

# my_list = ['Emrah', 'Toghrul', 'Chingiz']
# for i in range(len(my_list)):
#     print(my_list[i])

# my_list = ['Emrah', 'Toghrul', 'Chingiz', 'Anar']
# my_list.append(5) # 5-i elave edir
# print(my_list)

# my_list.extend([1,4,9]) # yeni list elave edir
# print(my_list)

# my_list.pop(2) # Listdeki indexi silir
# print(my_list)

# deleted_items = my_list.pop(2)
# print(my_list)
# print(deleted_items)

# my_list.sort()
# my_list.sort(reverse=True)
# print(my_list)

# my_list.insert(2, 'Ali') # 2-ci indexe Ali elave et
# print(my_list)

# a = my_list.copy()
# a.append(55)
# print(my_list)

# my_tuple = (4, 9, 'hi')
# my_tuple = list(my_tuple)
# my_tuple.append(55) 
# my_tuple[2] = 43
# my_tuple = tuple(my_tuple)
# print(type(my_tuple))

# my_car = {
#     #key     #value
#     'marka' :'TOYOTA',
#     'year' : 2018,
#     'model' : 'PRADO'
# }
# print(my_car.get('mazda' 'Bele bir info yoxdur'))
# print(my_car ['year'])
# print(my_car.keys())
# print(my_car.values())
# print(my_car.items())
# print(my_car.pop())
# my_car['weight'] = 600
# my_car.update({'weight':600, 'wey':99})
# print(my_car)



# my_set = {'alma', 'armud', 'banan', 'armud', 'banan', 'alma', 'armud'}
# print(my_set)                                                                   #SET -- eyni olanlari silir
# x = {'alma', 'armud', 'banan', 'armud', 'banan', 'alma', 'armud'}
# print(set(x))

# set2 ={9,1,5,8,3,5,7,6,2,3}
# print(set2)

my_list = [
    {
    'yazici1' : {
         'ad': 'Dostoyevski',
         'eser': 'Cinayet ve ceza',
    },
    'yazici2' : {
         'ad': 'Stoveys',
         'eser': 'Ceza',
    },
    }
]
for i in my_list:
    print(i)

# gul = {
#     'yazici1' : {
#        'ad': 'Dostoyevski',
#        'eser': 'Cinayet ve ceza',
#     },
#     'yazici2' : {
#        'ad': 'Stoveys',
#        'eser': 'Ceza',
#     }
# }
# print(gul)