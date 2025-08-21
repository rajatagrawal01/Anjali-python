student = {
    "Name":"Anjali",
    "Course":"Python",
    "Time":330,
    "FeesPerYear":20000,
    "Total_Duration":1.5
    }

# print("Old Dictionary",student)

#student["FeesPerYear"]= 100000          # Updating data in already existing key
student["course2"] = "Data Science"     # Adding a new key and data

student.update({"Course":"NodeJs","Time":430,"FeesPerYear":30000}) # Updating Multipls data in already existing key

del student["course2"]

# student.popitem()
# student.clear()

# print("New Dictionary",student)

for key in student:
    print(key,":",student[key])

for key,value in student.items():
    print(key,":",value)

# ==================================================Accessing list==================================================

# print(student.keys())
# print(student.values())
# print(student.items())