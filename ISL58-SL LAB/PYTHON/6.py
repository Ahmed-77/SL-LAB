mydict = {
    "name":"Archie",
    "identity":"Student",
    "age":"17"
}

print(mydict)

key = mydict["name"]
value = mydict.get("name")

print("Key is ")
for key in mydict:
    print(key)
    
print("Value is ")
for key in mydict:
    print(mydict[key])
