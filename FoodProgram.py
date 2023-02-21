import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0

# customer = fc.Customer(570,"Danni Sellyar","97 Mitchell Way Hewitt Texas 76712","dsellyarft@gmpg.org","254-555-9362",False)

customer = fc.Customer(
    569,
    "Aubree Himsworth",
    "1172 Moulton Hill Waco Texas 76710",
    "1172 Moulton Hill Waco Texas 76710",
    "254-555-2273",
    True,
)

print(f"Customer Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")

for x, y in dict.items():
    transaction = fc.Transaction(y[0], y[1], y[2], y[3])
    if customer.get_customerid() == transaction.get_customerid():
        print(
            f"Order Item: {transaction.get_item_name()} Price: ${format(transaction.get_cost(), '.2f')}"
        )
        order_total += transaction.get_cost()


print(f"Total cost: ${format(order_total, '.2f')}")


member_discount = order_total * 0.2
if customer.get_member_status() == True:
    print(f"Member Discount: ${format(member_discount, '.2f')}")
    print(f"Total Cost After Discount: ${format(order_total - member_discount, '.2f')}")
    print()
else:
    print()
