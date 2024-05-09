print("This programe calculate the discount of a given price")
price = float(input("Enter price: "))
discount_percent = float(input("Enter discount: "))
def calculate_discount(price, discount_percent) :
    if discount_percent >= 20 :
        total = price - (price * discount_percent / 100)
        print(total)
    else :
        print(price)

calculate_discount(price, discount_percent)