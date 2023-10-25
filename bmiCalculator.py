#Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksinin hesaplanması işlemi 
#Formül : (VKİ = ağırlık/(boy*boy)) 

strWeight = input("Please enter the value of your weight: ")
strHeight = input("Please enter the value of your height: ")

#dönüşümler
weight = float(strWeight)
height = float(strHeight)

#hesaplama
calculate = weight/(height*height)

bmi = str(calculate)

print("Your body mass index is = " + bmi)