'''numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)
print(numbers)'''
#List Comprehension
Operation_list = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(Operation_list)

#Dic Comprehension
#-                                      -----
dict = {}
for i in range(1, 5):
  dict[i] = i * 2
print(dict)
dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2)
#-                                        -----
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1, 100)
print(population)
population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)
#-                                        -----
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
print(list(zip(names, ages)))
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)
#-                                        -----
population_v2 = { country: random.randint(1, 100)  for country in countries}
print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population > 50 }
print(result)

text = 'Hola, soy Nicolas'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)