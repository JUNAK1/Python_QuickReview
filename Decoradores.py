#Special Closure
def decorator(func):
    def envoltura():
        print('Hello')
        func()
    return envoltura
def saludo():
    print('Hola!')
saludo()
saludo = decorator(saludo)
saludo()
