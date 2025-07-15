'''def add(a,b):
    z=0
    z=a+b
    print(z)


def sub(a,b):
    z=0
    z=a-b
    print(z)

def mul(a,b):
    z=0
    z=a*b
    print(z)

def div(a,b):
    z=0
    z=a/b
    print(z)'''
numbers = list(range(0, 51, 4))  # [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
results = []
for number in numbers:
    if not number % 3:          # i.e., number % 3 == 0
        results.append(number)
print(results)
