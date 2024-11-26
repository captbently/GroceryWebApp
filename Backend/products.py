from sql import get_sql

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT Products.product_id, Products.name, Products.units_id, Products.price_per_unit, Units.units_name FROM Products INNER JOIN Units ON Products.unit_id=Units.units_id")
    cursor.execute(query)
    response = []
    for(product_id, name, units_id, price_per_unit, units_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'units_id': units_id,
            'price_per_unit': price_per_unit,
            'units_name': units_name,
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO Products "
             "(name, units_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['units_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM Products WHERE product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql()
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'units_id': '1',
        'price_per_unit': 10,
    }))