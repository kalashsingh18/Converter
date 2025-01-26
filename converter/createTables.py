def create_table(connection, table_name, columns):
        """
        Create a table in the database.

        :param table_name: Name of the table to create
        :param columns: Dictionary with column names as keys and column types as values
        """
        if not connection:
            raise Exception("No database connection established.")

        try:
            column_definitions = []
            for column_name, column_type in columns.items():
                column_definitions.append(f"{column_name} {column_type}")
            
            column_definitions_str = ", ".join(column_definitions)
            create_table_query = f"CREATE TABLE {table_name} ({column_definitions_str});"
            
            cursor = connection.cursor()
            cursor.execute(create_table_query)
            connection.commit()

            print(f"Table '{table_name}' created successfully!")
        
        except Exception as e:
            print(f"Error creating table: {e}")
            connection.rollback()
