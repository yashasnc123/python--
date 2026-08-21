count1 = 0
count2 = 0

for i in range(5):
    number = int(input("Enter the number: "))

    if number % 2 == 0:
        count1 = count1 + 1
    else:
        count2 = count2 + 1

print("Even numbers =", count1)
print("Odd numbers =", count2)