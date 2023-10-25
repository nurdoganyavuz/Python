#Maaşı ve zam oranı girilen personelin zamlı maaşının hesaplanması işlemi

strSalary = input("Please enter the value of your current salary: ")
strRateOfIncrease = input("Please enter the value of rate of increase: ")

#dönüşümler
salary = int(strSalary)
rateOfIncrease = int(strRateOfIncrease)

#hesaplama
calculate = int(salary + salary * (rateOfIncrease/100))

print("Your increased salary cost: " + str(calculate))