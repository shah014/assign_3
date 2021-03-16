lst = []
n = int(input("Enter the number of elements in list: "))
for i in range(n):
    k = input("Enter the element: ")
    lst.append(k)
print(lst)
# step1: Check to group the ele having same len and are not same
for i in lst:
    for j in lst:
        if len(i) == len(j) and i != j:
            for k in range(len(i)):
                for k1 in range(len(j)):
                    if i[k] == j[k]:
                        res = j

    print("Anagram of {} is:".format(i), res)


