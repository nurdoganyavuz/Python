number = (int(input("Please enter a number : ")))

if number <= 0:
    raise ValueError("Please enter a number greater than zero!")

sumOfDivisorNumber = 0

for i in range(1, number):
    if number % i == 0:
        sumOfDivisorNumber += i

if sumOfDivisorNumber == number:
    print("This number is a perfect number.")
else:
    print("This number is not a perfect number.")