#Kullanıcıdan alınan sayının asal çarpanlarını bulma islemi
number = int(input("Please enter a number :"))

divisorOfNumber = []
notPrimeDivisorOfNumber = []

#Sayının pozitif tam bölenlerini bulma (1 hariç) ve diziye ekleme islemi
for i in range(2, number+1):
    kalan = number % i
    if kalan == 0:
        divisorOfNumber.append(i)

print(f"Positive divisors of a number : {divisorOfNumber}")

#Sayının bölenleri arasından asal olmayanları bulma ve diziye ekleme islemi
for i in divisorOfNumber:
    for n in range(2, i):
        if i % n == 0:
            notPrimeDivisorOfNumber.append(i)
            break

#Asal olmayan bölenler dizisini bölenler dizisinden cıkarma islemi (sadece asal olan bölenleri bulmak icin)
for j in notPrimeDivisorOfNumber:
    divisorOfNumber.remove(j)

print(f"Prime factors of a number: {divisorOfNumber}")