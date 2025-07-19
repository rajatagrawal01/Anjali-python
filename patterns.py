#     *
#    **
#   ***
#  ****
# *****

# row - column
# 1-1
# 2-2
# 3-3
# 4-4
# 5-5

# for row in range(1,6):
#     for col in range(1,row):
#         print("*")

# rows =5 
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end='')
#     print()


# i-1 #(1,2) 1
# i-2 #(1,3) 1,2
# i-3 #(1,4) 1,2,3
# i-4 #(1,4) 1,2,3,4
# i-5 #(1,4) 1,2,3,4,5


# 1-1
# 2-2 -(1,2)
# 3-3 - (1,2,3)
# 4-4
# 5-5



# *****
# ****
# ***
# **
# *

numOfRows =6 
for row in range(1,numOfRows):
    for col in range(1,numOfRows-row):
        print(" " , end=" ")
    for col in range(1,row): #(1,4)
        print("*",end=" ")
    print()

