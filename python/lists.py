listA = [1, 2, 3]
listB = listA
listC = listB.copy()

listA[1] = 999
listB[2] = 75

listC[0] = 0

print("List a = ", listA)
print("list b = ", listB)
print("list c = ", listC)