nums = [6,4,6,8,2,9,3,5,9,2,4,7,9]
uniques = []
for i in nums:
    if i not in uniques:
        uniques.append(i)
print(uniques)