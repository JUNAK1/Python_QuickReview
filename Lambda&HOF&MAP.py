#LAMBDAS
increment_v2 = lambda x: x + 1
result = increment_v2(20)
x = lambda a, b : a * b
print(x(5, 6))

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'
text = full_name('nicolas', 'perez casas')
print(text)
x=0
#HOF
def increment(x):
    return x + 1
def high_ord_func(x, func):
    return x + func(x)
reult =  high_ord_func(x, increment)

#HOF + LAMBDA
increment_v2 = lambda x: x +1
high_ord_func_v2 = lambda x, func: x + func(x)
result = high_ord_func_v2(2, increment_v2)
print(result)

#MAP + LAMBDA
numbers = [1, 2, 3, 4]
numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7,8]
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)