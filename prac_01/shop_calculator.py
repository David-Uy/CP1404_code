DISCOUNT_THRESHOLD = 100
DISCOUNT = 0.1

number_of_item = int(input("Number of items: "))
total_price = 0

while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of items: "))

for i in range(number_of_item):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > DISCOUNT_THRESHOLD:
    price_discounted = total_price * DISCOUNT
    total_price = total_price - price_discounted

print(f"Total price for {number_of_item} is ${total_price:.2f}")