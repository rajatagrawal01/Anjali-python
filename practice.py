Num1 = 2345
Num2 = 2345
i = 0
while i>= Num1:
    Num1 = Num1%10
    print(Num1)
    Num1 = Num1//10
if Num1 == Num2:
    print("Yes, it is same")
else:
    print("No, it is not")