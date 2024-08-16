
print(30%0)


def func(arg):
    if arg == 0:
        return 0
    else:
        return (arg%2) + 10 * func(arg//2)

def funcao(x):
    if x == 1:
        return 1
    else:
        return x + funcao(x-1) * funcao(x-2)