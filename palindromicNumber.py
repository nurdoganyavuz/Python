#Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulma işlemi

strNumber = input("Please enter a number : ")

strReverseNumber = strNumber[::-1]

#dönüşümler 
number = int(strNumber)
reverseNumber = int(strReverseNumber)

if number == reverseNumber : print("The number is a palindromic number..")
else :  print("The number is not a palindromic number..")