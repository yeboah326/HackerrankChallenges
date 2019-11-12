# Birthday Chocolate

n = int(input())

s = list(map(int, input().split(" ")))

d, m = map(int, input().split(" "))


def birthdayChocolate(m, d):
    ss = []
    count = 0
    for i in range(len(s)):
        if m > len(s):
            break
        else:
            ss.append(s[i: m])
            m += 1
    for i in ss:
        if sum(i) == d:
            count += 1
        else:
            continue
    return count

print(birthdayChocolate(2, 3))




