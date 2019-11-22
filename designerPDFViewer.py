# Designer PDF Viewer

from string import ascii_lowercase as letters

def designerPDFViewer():
    heights = list(map(int, input().split(" ")))
    letterHeights = {}

    for i in range(len(letters)):
        letterHeights[letters[i]] = heights[i]
    
    newString = input()

    maxHeight = 0
    
    for j in newString:
        if maxHeight < letterHeights[j]:
            maxHeight = letterHeights[j]
    
    return maxHeight * len(newString)

print(designerPDFViewer())
