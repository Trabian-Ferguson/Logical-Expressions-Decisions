# Program Name: Lab2.py
# Course: IT1114/Section 01
# Student Name: Trabian Ferguson
# Assignment Number: Lab2
# Due Date: 9/3/2023
# Purpose: This program determines the food costs for the KSU CCSE Hackathon

import math

#number of pizzas and salads ordered
npo = int(input("Number of pizza orders"))
nso = int(input("Number of salad orders"))



#pizza total
pizzatotal = float(15.99 * math.ceil(npo*3/12))
#salad total
saladtotal = float(7.99 * nso)

#total order w/o discount
totalorder = float(pizzatotal + saladtotal)

#defining variables
pizzadis = 0
saladdis = 0

saladtax = 0
pizzatax = 0

if math.ceil(npo * 3/12) > 10:
    #calculation for pizza discount
    pizzatax = float (pizzatotal * 0.15)
    #pizza discount
pizzadis = (pizzatotal - pizzatax)
    

if nso > 10:
    #calculation for salad discount
    saladtax = float(saladtotal * 0.15)
    #saladdiscount
saladdis = (saladtotal - saladtax)
    



#pizzaandsalad_totaldiscount
totalwdiscount = float(pizzadis+saladdis)
totaldis = saladtax+pizzatax




deliverytax = 0


deliverytax = (pizzatotal+saladtotal)*0.07

if deliverytax < 20:

    deliverytax = 20

    


print("Pizzas ordered:", math.ceil(npo*3/12))
print("Pizza Cost $", pizzatotal)
print("Salad Cost $", saladtotal)
print("Total $", totalorder)
print("Discount $", totaldis)
print("Delivery fee $", deliverytax)
print("Total amount due $", totalwdiscount+deliverytax)



