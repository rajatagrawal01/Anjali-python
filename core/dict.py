                                                # Methods to define Dictionary
# Method 1: ==========================================================

student = {
    "Name":"Anjali",
    "Course":"Python",
    "Time":330,
    "FeesPerYear":20000,
    "Total_Duration":1.5
    }

# Method 2: ==========================================================
student2 = dict(name="Rajat",course="Java",time=430)


                                                # Method to access dictionary elements

# Method 1: ==========================================================
# value= dict_name["keyName"]

fees=student["FeesPerYear"]
duration=student["Total_Duration"]
total_fees=fees+duration

# Method 2: ==========================================================
# value= dict_name.get("keyName")

fees=student.get("FeesPerYear")
duration=student.get("Total_Duration")
total_fees=fees+duration


print("Student dictionary",student) #Accesing whole dictionary

print(student2["name"]) #Accessing single data Way 1
print(student.get("grade")) #Provides None if no Key present
print(student.get("grade","Sahi value daal")) #Accessing single data Way


