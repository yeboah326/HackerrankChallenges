# Bon Appetit

n, k = map(int, input().split(" "))
costs = list(map(int, input().split(" ")))

charged = int(input())

if charged != (sum(costs) / 2):
    print('Bon Appetit')
else:
    print(int(charged - (sum(costs) - costs[k]) / 2))

