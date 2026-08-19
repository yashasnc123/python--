#nested if else statement
age=int(input("enter your age:"))
attendance=int(input("enter your attendance:"))
if age>=18:
    if attendance>=75:
        print("your are eligible for exam")
    else:
        print("attendance too low")
else:
    print("age requirement not met")