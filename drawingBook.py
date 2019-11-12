# Drawing Book


n = int(input())

p = int(input())

book = []

for i in range(0, n + 1, 2):
    book.append([i, i+1])

destinationPage = [p, p + 1] if p % 2 == 0 else [p-1 , p]

flips = book.index(destinationPage) if book.index(destinationPage) < book.index(book[-1]) - book.index(destinationPage) else book.index(book[-1]) - book.index(destinationPage)

print(flips)

