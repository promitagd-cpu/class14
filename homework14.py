def greet_cutomer():
    print("Welcome to the art supply store!")
    print("Get your colours and brushes here!")
price_per_item = float(input("Enter the price per item in dollars:  "))
item_sold = int(input("Enter number of items sold:  "))
def calculate_total (price, items):
    total = price * items
    return total
total_cost = calculate_total(price_per_item, item_sold)
rounded_total = round(total_cost, 2)
print("total_cost:  ", rounded_total)
amount_paid = float(input("Enter amount paid by customer:  "))
def calculate_change (paid, total):
    change = paid - total
    return change
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)
def thank_customer():
    print("Thank you for shopping with us!")
    print("Your change is:  ", rounded_change)
    