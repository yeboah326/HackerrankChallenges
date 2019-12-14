# a = [4,6,5,3,3,1]
a = list(map(int, input().rstrip().split()))
# listOfLists = []

# for i in sorted(a):
#     m = list(filter((lambda x: i-1 <= x and x <= i + 1), a))
#     if (listOfLists.count(m) == 0 and len(list(set(m))) <= 2):
#         listOfLists.append(m) 
#     for i in listOfLists:
#         length = len(i) if len(i) > length else length


def pickingNumbers(a):
    listOfLists = []
    length = 0
    for i in a:
        m = list(filter((lambda x: i-1 == x or i == x), a))
        n = list(filter((lambda x: i+1 == x or i == x), a))

        if (listOfLists.count(m) == 0):
                listOfLists.append(m)
        if (listOfLists.count(n) == 0):
                listOfLists.append(n)
        for i in listOfLists:
            length = len(i) if len(i) > length else length
    return length

print(pickingNumbers(a))