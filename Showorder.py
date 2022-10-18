import sqlite3

class ShowOrder():
    def __init__(self,id ):
     self.id=id

    def show_order(self,id):
       try:
            conn = sqlite3.connect('orders.db')
        # create a cursor
            c = conn.cursor()
            sql = "SELECT t1.order_id,t1.order_status,t1.item_count,t2.product_name,t2.product_quantity,t2.order_detail_status from" \
                 " orderheader t1  join orderdetail t2 on t1.order_id = t2.order_detail_id where order_id =?"""
            c.execute(sql,(id,))
            data = c.fetchall()
            order_no = 0
            for row in data:
                if (order_no != row[0]):
                    print('       ')
                    print(f'Order {row[0]},{row[1]},{row[2]}')
                    order_no = row[0]
                if (order_no == row[0]):
                    print(row[3], row[4], row[5])
       except sqlite3.Error as error:
            print("Sql statement failed", error)
       finally:
            conn.commit()
            conn.close()

