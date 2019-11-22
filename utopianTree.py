# Utopian Tree

# n = int(input())

def utopianTree(n):
    currentHeight = 1
    while True:
        if n == 0:
            return currentHeight
        elif n == 1:
            return currentHeight * 2
        else:
            for j in range(n):
                if (j + 1) % 2 != 0:
                    currentHeight = currentHeight * 2
                elif (j + 1) % 2 == 0:
                    currentHeight = currentHeight + 1
            return currentHeight


    