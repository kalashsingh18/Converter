def insert_data(connection, table_name, columns, values):
    """
    Insert data into the specified table.
    
    :param connection: Database connection instance
    :param table_name: Name of the table where data will be inserted
    :param columns: A tuple or list of column names to insert data into
    :param values: A tuple or list of values corresponding to the columns
    :return: None
    """
    if not connection:
        raise Exception("No database connection established.")
    
    try:
        # Construct the INSERT INTO query
        columns_str = ", ".join(columns)
        placeholders = ", ".join(["%s"] * len(values))  # Create placeholders for values
        insert_query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders});"
        
        # Create a cursor object and execute the query
        cursor = connection.cursor()
        cursor.execute(insert_query, values)
        
        # Commit the transaction
        connection.commit()
        
        print(f"Data inserted successfully into '{table_name}'!")
    
    except Exception as e:
        print(f"Error inserting data: {e}")
        connection.rollback()
