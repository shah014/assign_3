people = []
tup1 = ('Suraj', 'Sharma', 25)
tup2 = ('Lien', 'Shah', 21)
people.append(tup1)
people.append(tup2)
print(people)
age = []
for i in range(len(people)):
    age.append(people[i][2])
print(age)
avg = sum(age)/len(age)
print(f'The average age is: {avg}')
for i in range(len(people)):
    if people[i][2] > avg:
        print(f'{people[i][0]} is old')
    else:
        print(f'{people[i][0]} is young')
