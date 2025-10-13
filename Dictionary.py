dict1 = { 1 : "ravi", 
          2 : "kuku",
          3 : "shivi",
          4 : "priya",
        }
print(dict1)

print(dict1.keys())
print(dict1.values())

for key in dict1.keys():
    print(key)

for val in dict1.values():
    print(val)
print("\n")

dict2  = { "name": "Alice", "age": 25, "course": "Computer Science"}
for x in dict2:
    print("KAYS ", x)

for x in dict2:
    print("VALUES", dict2[x])


dict2  = { "name": "Alice", "age": 25, "course": "Computer Science"}

for i in dict2.items():
    print(i)

for i in list(dict2.keys())[:2]:
    dict2.pop(i)
print(dict2)



# dict2.pop("name")
# print(dict2)

dict2  = { "name": "Alice", "age": 25, "course": "Computer Science"}

copied = dict2.copy()
print(copied)

sorted_dict = dict(sorted(dict2.items()))
print(sorted_dict)