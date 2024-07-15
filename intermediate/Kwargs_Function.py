# def person(**Kwargs):
#     print(Kwargs)
#     print(type(Kwargs))

#     if 'age' in Kwargs:
#         print("Your age is", Kwargs.get("age"))


# person(name="Jacob", age=27, brain="Huge")    

def order_pizza(name, address, **toppings):
    print(f"Order is for {name}")
    print(f"Ship it to {address}")
    price = 18.00
    for key, value in toppings.items():
        price = price + 6.00
        print(f"The total price is {price}")
        return price
    
total_price = order_pizza("Amanda", "Canada", jalapenos=True, extra_cheese=True, ham=True)    