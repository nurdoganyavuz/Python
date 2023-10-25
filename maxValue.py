#Kullanıcının girdiği üç sayı arasında en büyük olanı bulma işlemi

strNumberOne = input("Please enter the value of first number: ")
strNumberTwo = input("Please enter the value of second number: ")
strNumberThree = input("Please enter the value of third number: ")

#dönüşümler
numberOne = int(strNumberOne)
numberTwo = int(strNumberTwo)
numberThree = int(strNumberThree)

numbers = [numberOne, numberTwo, numberThree]
maxValueOfNumbers = max(numbers)

print("Maximum value is : " + str(maxValueOfNumbers))