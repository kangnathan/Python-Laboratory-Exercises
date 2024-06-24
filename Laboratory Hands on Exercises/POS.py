print("WELCOME TO THE 100 STORE")

price = 100
stock = 100
critical_level = stock * 0.5

product_name = input("Enter Product: ")
quantity = int(input("Enter Quantity: "))

if quantity <= stock:
    print(f"""
Product Order: {product_name}
Quantity: {quantity}
Amount: {price}

--------------------------------

Total Amount: {quantity * price}
Order Complete 
Please Proceed to Payment

--------------------------------
""")

    payment = int(input("Enter Payment: "))
    total_amount = quantity * price
    change = payment - total_amount
    stock_remain = stock - quantity

    print(f"""
Total Amount: {quantity * price}
Amount Paid: {payment}
""")

    if payment >= total_amount:
        print(f"""
Change: {change}
Payment Complete\nThank you, Come again

--------------------------------

Inventory Report
Stock Remain: {stock_remain}
            """)
        if stock_remain > critical_level:
            print("This item is available")
        elif critical_level > stock_remain > 1:
            print("This item is at Critical Level")
        else:
            print("This item is at Out of Stock")
    else:
        print(f"""
Insufficient Funds

--------------------------------

Inventory Report
Stock Remain: {stock}
This item is available
""")
else:
    print("Sorry we are short of that item")
