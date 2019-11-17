# Magic Square Forming


def formingMagicSquares():
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    magicSquares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
    
    costs = []
    
    for j in range(8):
        tempCost = 0
        for k in range(3):
            tempCost += subtractListMember(s[k], magicSquares[j][k])
        costs.append(tempCost)
    
    return min(costs)

def subtractListMember(listOne: list, listTwo: list):
    listResult = []
    for i in range(len(listOne)):
        listResult.append(abs(listOne[i] - listTwo[i]))
    return sum(listResult)

print(formingMagicSquares())
