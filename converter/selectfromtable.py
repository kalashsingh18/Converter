def select_data(connection, table_name, columns="*"):
    """
    Execute a SELECT query to fetch data from a specified table.
    
    :param connection: Database connection instance
    :param table_name: Name of the table from which to fetch data
    :param columns: Columns to select, defaults to '*' (all columns)
    :return: List of rows from the query result
    """
    if not connection:
        raise Exception("No database connection established.")
    
    try:
        select_query = f"SELECT {columns} FROM {table_name};"
        
        cursor = connection.cursor()
        cursor.execute(select_query)
        
        rows = cursor.fetchall()

        print(f"Data fetched successfully from '{table_name}'")

        return rows
    
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
