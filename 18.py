# importing package for dealing with json in python
import json

print(dir(json))

# to learn more on json we use
# help(json)

# dictionary mapping 'name' to your name and 'age' to your age

my_info = {"name": "Anil Shah", "age": 25}

# writing it to a json string
with open("my_info.json", "w") as write:
    json.dump(my_info, write)

# back to python form from json
with open("my_info.json", "r") as read:
    res = json.load(read)
print(res)

