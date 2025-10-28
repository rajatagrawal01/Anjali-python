file = open("notes.txt", "r")

# content = file.read(100)
content = file.readlines()
print(content)
file.close()