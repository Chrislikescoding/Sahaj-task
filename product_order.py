import sqlite3


class CheckOrder:
    def check_order(self, order_id):
        order_is_valid = True
        try:
            conn = sqlite3.connect('orders.db')
            # create a cursor
            c = conn.cursor()
            sql = "SELECT order_id from orderheader where order_id =?"""
            c.execute(sql, (order_id,))
            data = c.fetchone()
            if data is not None:
                return order_is_valid
            else:
                print(f"Order {order_id} does not exist")
                order_is_valid = False
        except sqlite3.Error as error:
            print("", error)
        finally:
            conn.commit()
            conn.close()
            return order_is_valid


class CheckProduct:
    def check_product(self, product):
        product_is_valid = True
        try:
            conn = sqlite3.connect('orders.db')
            # create a cursor
            c = conn.cursor()
            sql = "SELECT product_name from products where product_name =?"""
            c.execute(sql, (product,))
            data = c.fetchone()
            if data is not None:
                return product_is_valid
            else:
                print(f"Product {product} does not exist")
                product_is_valid = False
        except sqlite3.Error as error:
            print("", error)
        finally:
            conn.commit()
            conn.close()
        return product_is_valid


class ProductOrder:

    def __init__(self, order_id, product, quantity):
        self.order_id = order_id,
        self.product = product
        self.quantity = quantity

    def create_product_order(self, order_id, product, quantity):
        order_check = CheckOrder()
        if not order_check.check_order(order_id):
            print(f"Order with id {order_id} does not exist")
        else:
            product_check = CheckProduct()
            if not product_check.check_product(product):
                print(f"Product {product} does not exist")
            else:
                product_order_created = False
                try:
                    conn = sqlite3.connect('orders.db')
                    # create a cursor
                    c = conn.cursor()
                    # insert into table
                    order_detail_status = 'DRAFT'
                    c.execute("INSERT INTO orderdetail VALUES ('{}','{}', {},'{}')".format(order_id, product, quantity, order_detail_status))
                    c.execute("UPDATE orderheader SET item_count=item_count + '{}' where order_id = '{}'".format(quantity, order_id))
                    print(f"{product} {quantity} added to order  {order_id}")
                    product_order_created = True
                except sqlite3.Error as error:
                    print("Failed to insert data to create the product order", error)
                finally:
                    conn.commit()
                    conn.close()
                return product_order_created
