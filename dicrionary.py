info = {
    "name": "abhijeet", 
    "cgpa": 9.2, 
    "subject": ["math", "science"]
}

info["cgpa"] = 9.6

info.update({
    "city": "Delhi"
})

print(info)
print(type(info))

print(info["name"])

#dict_keys = list(info.keys())    thsi we can coverst as list
dict_keys = (info.keys())
print(dict_keys)

print(info.items())

print(info.get("cgpa"))

