def delete_table(connection, table_name):
        """
        Drop a table in the database.
  
        """
        if not connection:
            raise Exception("No database connection established.")

        try:
            create_table_query = f"DROP TABLE {table_name};"         
            cursor = connection.cursor()
            cursor.execute(create_table_query)
            connection.commit()
            print(f"DROP TABLE  '{table_name}' DROPED successfully!")

        except Exception as e:
            print(f"Error creating table: {e}")
            connection.rollback()
