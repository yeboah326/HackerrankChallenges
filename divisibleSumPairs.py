# Divisible Sum Pairs

n, k = map(int, input().split(" "))
m = list(map(int, input().split(" ")))

counter = 0

for i in range(n):
    for j in range(n):
        if j <= i:
            continue
        if (m[i] + m[j]) % k == 0:
            counter += 1

print(counter)
