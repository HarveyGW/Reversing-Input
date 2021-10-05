'''Reversing the integer input'''

#With Using Maths
number=int(input("Enter a No: "))
hundreds=number//100
tens=(number%100)//10
units=number%10
print(units,tens,hundreds)

#Without Using Maths
number=input("Enter a No: ")
print(number[::-1])
