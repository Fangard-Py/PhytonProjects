# Словарь

my_dict = {'Pavel': 27, 'Masha': 20, 'Roma': 17}
print(my_dict)
print(my_dict['Pavel'])
print(my_dict.get('Danil'))
my_dict.update({'Danil': 22,
                'Petya': 40})
pop_ = my_dict.pop('Masha')
print(my_dict)
print(pop_)

# Множество

my_set = {1, 2, 3, 4, 5, 1, 2, 3, 'Pavel'}
print(my_set)
my_set.add(6)
my_set.add('Alex')
my_set.discard(2)
print(my_set)
