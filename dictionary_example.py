menu = {
    1: {
        "name": 'espresso',
        "price": 1.99
    },
    2: {
        "name": 'coffee', 
        "price": 2.50
    },
    3: {
        "name": 'cake', 
        "price": 2.79
    },
    4: {
        "name": 'soup', 
        "price": 4.50
    },
    5: {
        "name": 'sandwich',
        "price": 4.99
    }
}
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

def calculate_tax(subtotal):
      tax_rate = 0.15
      return round(subtotal*tax_rate,2)

def take_order():
    display_menu()
    order =[]
    count = 1
    for item in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order
def summarize_order(order):
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total_cost = round(subtotal + tax, 2)
    orders_name =[]
    for item in order:
        name = item["name"]
        orders_name.append(name)
    return orders_name,total_cost


def display_order_name(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items_name =[]
    for item in order:
      items = item["name"] 
      print(items)
      items_name.append(items)
    print(items_name)
    return order
def calculate_subtotal(order):
   total =0.0
   for item in order:
       total +=item["price"]
   return round(total,2)
       
def main():
    order =take_order()
    print(order)
    display_order_name(order)
    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is: $" + str(subtotal))
    tax = calculate_tax(subtotal)
    print("Tax for the order is: $" + str(tax))
    items, total = summarize_order(order)
    print("You have ordered:")
    for item in items:
        print(item)
    print("Total cost of the order is: $" + str(total))


if __name__ == "__main__":
    main()
