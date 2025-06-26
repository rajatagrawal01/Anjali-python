x=768

unit=(x//1)%10
tens=(x//10)%10
hundreds=(x//100)%10


print("Unit:",unit)
print("Tens:",tens)
print("Hundreds:",hundreds)
reversedNumber=unit*100 + tens*10 + hundreds *1
print("reversed number:",reversedNumber)