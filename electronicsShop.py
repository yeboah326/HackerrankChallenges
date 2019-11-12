# Electronics Shop

s, n, m = map(int, input().split(" "))

nList = list(map(int, input().split(" ")))

mList = list(map(int, input().split(" ")))


def electronicsShop(s=s):
    compareSum = 0
    maxSum = 0
    for i in nList:
        for j in mList:
            compareSum = i + j
            if compareSum <= s:
                maxSum = compareSum if compareSum > maxSum else maxSum
            else:
                continue
    return maxSum if 0 < maxSum <= s else -1

print(electronicsShop())