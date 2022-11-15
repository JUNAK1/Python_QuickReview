#Closure with nested functions
'''
def main():
    a=1
    def nested():
        print(a)
    nested()
func = main()
func()
'''
def Mul(x):
    def num(n):
        return x * n
    return num
t10 = Mul(10)
t4  = Mul(4)

print(t10(3))
print(t4(2))
print(t10(t4(3)))


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puedes repetir cadenas'
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola'))


if __name__ == '__main__':
    run()
