#Dimitri Aistov Pizza calculator

import time

#Menu
smallAmount = int(input("Hoeveel small pizzas voor 5.99 wilt u? "))
mediumAmount = int(input("Hoeveel medium pizzas voor 7.99 wilt u? "))
largeAmount = int(input("Hoeveel large pizzas voor 11.99 wilt u? "))

time.sleep(1)

#Prijzen
smallPrice = 5.99
mediumPrice = 7.99
largePrice = 11.99

#Totaal
totalPrice = smallAmount * smallPrice + mediumAmount * mediumPrice + largeAmount * largePrice
round(totalPrice, 2)

print("Uw totaalbedrag is " + str("%.2f" % totalPrice))