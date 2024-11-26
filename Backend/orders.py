from datetime import datetime
from sql import get_sql

def insert_order(connection, order):
    cursor = connection.cursor()

    order_query = ("INSERT INTO Orders "
                   "(customer_name, total, datetime)"
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_details_query = ("INSERT INTO Order_Details "
                           "(order_id, product_id, quantity, total_price)"
                           "VALUES (%s, %s, %s, %s)")
    
    order_details_data = []
    for order_detail_record in order['Order_Details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()

    return order_id

def get_order_details(connection, order_id):
    cursor = connection.cursor()

    query = "SELECT * FROM Order_Details WHERE order_id = %s"

    query = "SELECT Order_Details.order_id, Order_Details.quantity, Order_Details.total_price, "\
            "Products.name, Products.price_per_unit FROM Order_Details LEFT JOIN Products ON "\
            "Order_Details.product_id = Products.product_id WHERE Order_Details.order_id = %s"
    
    data = (order_id, )

    cursor.execute(query, data)

    records = []
    for (order_id, quantity, total_price, product_name, price_per_unit) in cursor:
        records.append({
            'order_id': order_id,
            'quantity': quantity,
            'total_price': total_price,
            'product_name': product_name,
            'price_per_unit': price_per_unit,
        })

    cursor.close()

    return records

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM Orders")
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt,
        })

    cursor.close()

    # Append order details in each order
    for record in response:
        record['Order_Details'] = get_order_details(connection, record['order_id'])

    return response

if __name__ == '__main__':
    connection = get_sql()
    print(get_all_orders(connection))