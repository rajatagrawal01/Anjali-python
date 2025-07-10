# Syntax of for loop

# for item in sequence:
#     operation

# for item in range(start,(<end),increment/decrement):
#     operation

# Example:

# for i in range(0,6,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# for i in range(1,11):
#     if(i%2!=0):
#         print(i,"-Is odd number")
#     else:
#         print(i,"-Is Even number")

# for i in range(1,11):
#     if(i==2):
#         continue
#     print(i)


# for i in range(1,11):
#     if(i==5):
#         break
#     print(i)

# While loop:

# var initialisation

# while condition:
#     operation
#     step

# i=0
# while i<5:
#     print(i)
#     i+=1

# for loop requires a rang (start and end)
# while loop works untill condition is true(may be always)

# num = 11
# for i in range(2,num):
#     if(num%i==0):
#         print(num , ": is not prime")
#         break
#     else:
#         print(num , ": is prime")
#         break

# 1,2,3,4,5,6
# 0,1,2,3,4,5

# while True:
#     password = input("Enter password: ")
#     if password =="password123":
#         print("Welcome")
#         break
#     else:
#         print("Wrong Password,Enter Again")