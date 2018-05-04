# Make a list intersector

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 88]

intersectList = []
for aelement in a:
    if (aelement in b) and not (aelement in intersectList):
        intersectList.append(aelement)

print(intersectList)