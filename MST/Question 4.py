stock = {
    'mb': 6,
    'cpu': 5,
    'ram': 32,
    'chassis+power supply': 0,
    'dvd drive': 5,
    'harddisk': 155
}

price = {
    'mb': 225,
    'cpu': 155,
    'ram': 120,
    'chassis+power supply': 230,
    'dvd drive': 25,
    'harddisk': 55
}

#add ssd
stock['ssd'] = 15
price['ssd'] = 60

#delete dvd drive
del stock['dvd drive']
del price['dvd drive']

shopping_cart = ['mb', 'cpu', 'ram', 'chassis+power supply', 'ssd', 'harddisk']

#computing bill
def compute_bill(components):
    total = 0
    for key in stock:
        # print(i)
        if stock[key] == 0:
            print(f"Warning, no stock for {key}: ${price[key]}")
        else:
            stock[key] -= 1
            # print(f"{key} {stock[key]}")
            total += price[key]
    print(f"Total: ${total:.2f}")
    
#Call a function to compute the bill
# compute_bill(shopping_cart)
#Print the total
# print(stock)
# print(len(shopping_cart))

for no in range(len(shopping_cart)):
    if no == len(shopping_cart)-1:
        print(shopping_cart[no])
    else:
        print(shopping_cart[no], end=', ')
