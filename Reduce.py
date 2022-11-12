#Reduce                                                                                  Reduce
import functools
numbers = [1, 2, 3, 4]
def accum(counter, item):
  return counter + item
result = functools.reduce(accum, numbers)
print(result)

#Reduce  And Lambda
letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)