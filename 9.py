lst = []
n = int(input("Enter the number of elements in list: "))
for i in range(n):
    k = int(input("Enter element to add: "))
    lst.append(k)
print(lst)
f = int(input("Enter the element to find: "))


def binary_search(lst, f):
    for i in range(len(lst)):
        if f in lst:
            return lst.index(f)
        else:
            return -1


print(binary_search(lst, f))


