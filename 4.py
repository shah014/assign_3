lst = []
print(id(lst))
lst = []
n = int(input("Enter the number of elements in list: "))
for i in range(n):
    k = input("Enter the element: ")
    lst.append(k)
print(lst)
print(id(lst))
sorted_list = sorted(lst)
print(sorted_list)
print(f'The first item on list: {sorted_list[0]}')
print(f'The second item on list: {sorted_list[1]}')