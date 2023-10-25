#Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksinin hesaplanması işlemi 
#Formül : (VKİ = ağırlık/(boy*boy)) 

weight = input("Please enter the value of your weight: ")
height = input("Please enter the value of your height: ")

#dönüşümler
intWeight = float(weight)
intHeight = float(height)

#hesaplama
calculate = intWeight/(intHeight*intHeight)

bmi = str(calculate)

print("Your body mass index is = " + bmi)