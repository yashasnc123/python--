total = 0
number = int(input("Enter the number: "))

while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("Sum of digits:", total)