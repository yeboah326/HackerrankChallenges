# Sock Merchant

n = int(input())

colors = list(map(int, input().split(" ")))

colorDict = {}

colorSet = set(colors)


for i in colorSet:
    colorDict[i] = colors.count(i)

counter = 0

for val in colorDict.values():
    counter += val // 2


print(counter)
