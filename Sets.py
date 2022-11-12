set_countries = {'col', 'mex', 'bol'}
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print('col' in set_countries)
set_countries.add('pe')                     # add
set_countries.update({'ar', 'ecua', 'pe'})  # update
set_countries.remove('col')                 # remove
set_countries.discard('arg')                # remove if element in set
set_countries.clear()                       #remove all

set_a = {'col', 'mex', 'bol'}               
set_b = {'pe', 'bol'}
set_c = set_a.union(set_b)                  #Union
print(set_c)
print(set_a | set_b)
set_c = set_a.intersection(set_b)           #Intersection
print(set_c)
print(set_a & set_b)
set_c = set_a.difference(set_b)             #Difference
print(set_c)
print(set_a - set_b)
set_c = set_a.symmetric_difference(set_b)   #Asymetric_difference
print(set_c)
print(set_a ^ set_b)