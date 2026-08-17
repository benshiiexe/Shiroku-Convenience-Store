#Program created by: Benedict Emmanuel D. Rivera
#Date created: Aug 3, 2026
#Program title: Hands-on Activity 2
print("=======================================================")
print("=========Welcome to Shiroku Convenience Store==========")
print("=======================================================")
print("Menu:")
print("1. Icelandic Water (PREMIUM LIMITED EDITION$$$$) - $3")
print("2. Doritos Nacho Cheese (Naoto Shirogane Spit) - $2.50")
print("3. Onigiri (Salmon) - $2.75")
print("4. Pocky Chocolate - $2")
print("5. Ramune Soda - $3.50")
print("6. Instant Ramen - $2.25")
print("7. Coca-Cola (Kill Pepsi Support) - $2.00")
print("8. Spam Musubi - $3.75")
print("9. Hershey's Chocolate Bar - $1.75")
print("10. Lays Classic Chips - $2.25")
print("=======================================================")
customer_name = input("Enter your name: ")
item = input("Enter the item you want: ")

if item == "Icelandic Water" or item == "icelandic water" or item == "1" :
    price = 3
elif item == "Doritos Nacho Cheese" or item == "doritos nacho cheese" or item == "2" :
    price = 2.50
elif item == "Onigiri" or item == "onigiri" or item == "3" :
    price = 2.75
elif item == "Pocky Chocolate" or item == "pocky chocolate" or item == "4" :
    price = 2
elif item == "Ramune Soda" or item == "ramune soda" or item == "5" :
    price = 3.50
elif item == "Instant Ramen" or item == "instant ramen" or item == "6":
    price = 2.25
elif item == "Coca-Cola" or item == "coca-cola" or item == "7":
    price = 2
elif item == "Spam Musubi" or item == "spam musubi" or item == "8":
    price = 3.75
elif item == "Hershey's Chocolate Bar" or item == "hershey's chocolate bar" or item == "9":
    price = 1.75
elif item == "Lays Classic Chips" or item == "lays classic chips" or item == "10":
    price = 2.25
else:
    print("❌ Invalid Item. Please select a valid item from the list, then try again.")
    exit()

print(f"The price of {item} is ${price:,}")
quantity = int(input(f"Enter the quantity of {item}: "))
total_cost = price * quantity
payment = float(input("Enter your payment amount: ")) 
if payment < total_cost:
    print ("❌ Insufficient Payment Amount. Please pay the total cost, then try again.")
    exit()
else:
    change = payment - total_cost
print("========== OFFICIAL RECEIPT ==========")
print(f"Customer Name : {customer_name}")
print(f"Item Ordered   : {item}")
print(f"Quantity      : {quantity}")
print(f"Total Cost    : ${total_cost:,}")
print(f"Payment       : ${payment:,}")
print(f"Change        : ${change:,}")
print("======================================")
print("   Thank you for choosing Shiroku Convenience Store!   ")
print("======================================")
