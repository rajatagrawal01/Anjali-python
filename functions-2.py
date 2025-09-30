# def likho():
#     print ("Hello World")

# likho()

def greeting(name,age):
    print(f"Hello {name} , your age is {age}")

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

def addition(*args):
    print(sum(args))

addition(12,13,14,15,16,17)