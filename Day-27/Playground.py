def add(*args):
    index = args[0]
    sum = 0
    for n in args:
        sum += n
    return sum


def calculate(**kwargs):
    print(kwargs)



print(add(2,3,4,54,5,1,3))
calculate(add= 3, multiply=5)





