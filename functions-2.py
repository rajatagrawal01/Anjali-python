# def likho():
#     print ("Hello World")
# likho()

# def addition(a,b):
#     return a+b
# x=addition(4,5)
# print(x)

# def greeting(name,age):
#     print(f"Hello {name} , your age is {age}")

# greeting("Anjali",24)
# greeting("Rajat",25)
# greeting("Chetan",26)

# print("without keyword")
# greeting(27,"Anjali")

# print("with keyword")
# greeting(age=27,name="Anjali")

# def hello(name="Guest"):
#     print("Hello",name)

# hello()

# def addition(*args):
#     print(sum(args))

# addition(12,13,14,15)



# def stu_info(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# stu_info(Name="Anjali",Age=23,City="Indore",Section="CSE",fees=20000)

x=50 #Global
def scope():
    x=24 #Local /Temp variable
    print("Inside Function , value of x is : ",x)

scope()
print("outside Function , value of x is : ",x)