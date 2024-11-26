def get_units(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM Units")
    cursor.execute(query)
    response = []
    for (units_id, units_name) in cursor:
        response.append({
            'units_id': units_id,
            'units_name': units_name,
        })
    return response

if __name__ == "__main__":
    from sql import get_sql

    connection = get_sql()
    print(get_units(connection))