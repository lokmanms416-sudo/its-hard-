names = input("enter the first name and the last name separated by comma:").split(", ")
for name in names:
    name = name.split(" ")
    print(name)
print("abbreviated names:")
for name in names:
    name = name.split(" ")
    print(name[0][0]+","+name[1][0])
