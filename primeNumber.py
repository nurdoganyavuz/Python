#Kullanıcıdan alınan sayının asal sayı olup olmadığını kontrol etme islemi 

number = int(input("Please enter a number :"))

if number > 1:
    for i in range(2, number):
        mod = number % i
        if mod == 0:
            print("This number is not prime.")
            break
    else:           
        print("This number is prime.")

else:
    print("This number is not prime.")