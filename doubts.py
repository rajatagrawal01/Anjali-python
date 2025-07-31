# a[0]=1, a[1]=2, a[2]=3, a[3]=4, a[4]=5

# b[0]=2, b[1]=3, b[2]=1 ,b[3]=0, b[4]=5

# a[i] == b[j]

# 0- 0,1,2,3,4
# 1- 0,1,2,3,4
# 2- 0,1,2,3,4
# 3- 0,1,2,3,4
# 4- 0,1,2,3,4


a=[1,2,3,4,5]
b=[2,3,1,0,5]
missing =[]

for i in range(len(a)):
    matched=0
    for j in range(len(b)):
        if(a[i]==b[j]):
            matched=1
            break
    # else:
    #     missing.append(a[i])
    if(matched==0):
        missing.append(a[i])
        
print("Missing numbers",missing)


