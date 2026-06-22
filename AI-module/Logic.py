#Logic-Based Representation

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Not Adult")
    
# Prolog Syntex 

parent = {
    "john": "mary"
}

name = input("Enter parent name: ")

if name in parent:
    print(parent[name])
else:
    print("Not found")