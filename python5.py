#condition statements if elif else 1
number_1=int(input("enter the number1:"))
number_2=int(input("enter your number2:"))
if number_1 < number_2:
    print("yes number 2 is greater than  or equal to number 1")
elif number_1 == number_2:
    print(" both are equal")
else:
    print("yes number1 is greater than  or equal to number2")
    
#2
marks =int(input("enter the marks :"))
if marks >= 90:
    print("grade a")
elif marks >= 80:
    print("grade b")
elif marks >= 70:
    print("grade c")
elif marks >= 60:
    print("grade d")
else:
    print("grade e")
    