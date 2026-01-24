# Question : given a list of tuple with info(name, subject):

info = [
    ("Alice", "Math"),
    ("Bob", "Science"), 
    ("Alice", "Science"), 
    ("Charlie", "Math"),
    ("Bob", "Math"), 
    ("Alice", "English"),
    ("Charlie", "English"),
]


# unique courses  (A)
unique = set()
# for tup in info:
#     #print(tup)
#     unique.add(tup[1])

# print(unique)
for name,course in info:
    print(name, course)


# list student enroll in english (B)
for name,course in info:
    if(course == "English"):
        print(name)


# create dictionary 
dict = {}

for name, course in info:
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)