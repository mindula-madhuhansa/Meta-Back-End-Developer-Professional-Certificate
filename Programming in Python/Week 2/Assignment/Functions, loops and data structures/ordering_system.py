menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee',
        "price": 2.50},
    3: {"name": 'cake',
        "price": 2.79},
    4: {"name": 'soup',
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}


# calculate order total and return
def calculate_subtotal(order):
    print('Calculating bill subtotal...')

    bill_tot = 0

    for item in order:
        bill_tot += item["price"]
    tot = round(bill_tot, 2)
    return tot


# calculate tax for subtotal and return
def calculate_tax(subtotal):
    print('Calculating tax from subtotal...')

    tax = subtotal * 0.15
    return round(tax, 2)


# return items names and final bill
def summarize_order(order):
    print_order(order)
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)

    tot = subtotal + tax
    total = round(tot, 2)

    names = []
    for item in order:
        names.append(item["name"])

    return names, total


# print the order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order


# print the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()


# take the order
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order is: " + str(tax))

    items, subtotal = summarize_order(order)


if __name__ == "__main__":
    main()
