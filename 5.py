tup1 = ('Anil', 'Shah', 24)
people = []
people.append(tup1)
print(people)
tup2 = ('Suraj', 'Sharma', 25)
tup3 = ('Lien', 'Shah', 21)
people.append(tup2)
people.append(tup3)
# before sorting
print(f'Before sorting: {people}')
# sorting with age
people.sort(key=lambda x: x[2])
# after sorting with age
print(f'After sorting by age: {people}')
