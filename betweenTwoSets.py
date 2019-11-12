# Between Two Sets

n, m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
counter = 0

phaseOne = []

for i in range(min(a), min(b)+1):
    for x in a:
        if i % x == 0:
            phaseOne.append(i)
phaseOne = list(set(phaseOne))

for i in phaseOne:
    for y in b:
        if y % i == 0:
            counter+=1

print(counter)

