#
from create_order import *
from product_order import *
from showorders import *
from Showorder import *


def print_order_function():

    print('The following commands are available : ')
    print('Enter CREATE_ORDER to create an order : ')
    print('Enter ADD_PRODUCT_ORDER: to add product(s) to an order')
    print('Enter SHOW_ORDER [order_id] to display one order,with the id : ')
    print('Enter SHOW_ORDERS to show  all one orders : ')


if __name__ == '__main__':
    print_order_function()
    command = input()
    new_order = Order('DRAFT', 0)

if command == 'CREATE_ORDER':
    new_order.create_order('DRAFT', 0)
elif command == 'ADD_PRODUCT_ORDER':
    order_id = input('Enter id ')
    product = input('Enter product ')
    quantity = input('Enter quantity ')
    p_order = ProductOrder(order_id, 'product', quantity)
    p_order.create_product_order(order_id, product, quantity)
elif command == 'SHOW_ORDERS':
    s = ShowOrders()
    s.show_orders()
elif command[0:10] == 'SHOW_ORDER':
    x = command.find('[')
    y = command.find(']')
    if x != -1 & y != -1:
        order_id = command[x+1:y]
        s = ShowOrder(order_id)
        s.show_order(order_id)
    elif x == -1 | y == -1:
        print('INVALID COMMAND entered')
else:
    print('INVALID COMMAND entered')


