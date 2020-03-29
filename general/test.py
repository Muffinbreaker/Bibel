prices = ["2"]
new_prices =[]


for price in prices:
    if int(price) <= 20:
        price = int(price)*0.8

print(price)


