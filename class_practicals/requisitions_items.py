amount = int(input("how many items you want to purchase? "))
# inputs stored into these lists
item_name = []
price = []
# using for loop for lists
for i in range(amount):
    n = input(f"enter the name of the item:{i + 1} ")
    item_name.append(n) #append will add to the list
    p = float(input(f"enter the price:{i + 1} "))
    price.append(p)
for i in range(amount):
    print(item_name[i], ":", price[i])
total = 0
for prices in price:
    total = prices + total
# displaying the receipt/output to user
print(f"total:{total}")