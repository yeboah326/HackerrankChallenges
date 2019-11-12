# Cats and a Mouse

q = int(input())


def catAndMouse():
    x, y, z = map(int, input().split(" "))
    if abs(z - x) < abs(z - y):
        return "Cat A"
    elif abs(z - x) > abs(z - y):
        return "Cat B"
    else:
        return "Mouse C"

for i in range(q):
    print(catAndMouse())
