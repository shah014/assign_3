lst = []
n = int(input("Enter the number of friends: "))
for i in range(n):
    k = input("Enter name: ")
    lst.append(k)
print(lst)
if 'John' in lst:
    print("Found")
else:
    print("Not Found")

