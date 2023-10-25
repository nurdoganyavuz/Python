#Dairenin alanını ve çevresini hesaplama işlemi

strRadius = input("Please enter the radius value: ")
radius = int(strRadius)
pi = 3

#alan
areaOfTheCircle = pi * (radius*radius)

#çevre
circumference = 2*pi*radius

print("Area of the circle is : " + str(areaOfTheCircle))
print("Circumference of the circle is : " + str(circumference))
