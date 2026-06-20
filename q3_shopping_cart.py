
# Part A - Spot the Bug
def add_item(item, cart=[]):
    cart.append(item)
    return cart

print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']
# Bug:
# cart=[] is a mutable default argument.
# The same list is reused across function calls.

# Part B - Fix It
def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart

print("\nFixed Version:")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))

# Part C - Shopping Cart Program
# Create a new cart
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Add item to cart
def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({
        "name": name,
        "price": price,
        "qty": qty
    })


# Demonstrate tuple immutability
def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print("\nTuple Error:", e)


# Calculate total after discount
def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    total -= total * (cart["discount"] / 100)

    return total


# Customer 1
cart1 = create_cart("Aarav", 10)

add_to_cart(cart1, "Book", 500, 2)
add_to_cart(cart1, "Pen", 20, 5)

# Customer 2
cart2 = create_cart("Priya", 5)

add_to_cart(cart2, "Notebook", 100, 3)

# Show carts
print("\nCustomer 1 Cart:")
print(cart1)

print("\nCustomer 2 Cart:")
print(cart2)

# Totals
print("\nCustomer 1 Total:", calculate_total(cart1))
print("Customer 2 Total:", calculate_total(cart2))

# Tuple example
price_info = (100, "Book")
update_price(price_info, 200)


