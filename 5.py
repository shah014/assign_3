#
# list1.sort(key=lambda x: x[1])
# print(list1)
tup1 = ('Anil', 'Shah', 24)
people = []
people.append(tup1)
print(people)
tup2 = ('Suraj', 'Sharma', 25)
tup3 = ('Lien', 'Shah', 29)
people.append(tup2)
people.append(tup3)
# before sorting
print(people)
# sorting with age
people.sort(key=lambda x: x[2])
# after sorting with age
print(people)
