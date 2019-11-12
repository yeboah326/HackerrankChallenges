# Migratory Birds

n = int(input())

arr = list(map(int, input().split(" ")))

y = set(arr)

bird = {}
for i in y:
    bird[i] = arr.count(i)

initialKey, intialValue = min(bird), 0

for key, value in bird.items():
    if value > intialValue and key > initialKey:
        intialValue, initialKey = value, key

print(initialKey)

