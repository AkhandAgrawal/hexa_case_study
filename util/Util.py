import pyodbc # type: ignore

class DBConnUtil:
    @staticmethod
    def create_db_connection():
        """Establish a database connection."""
        try:
            connection_string = (
                "Driver={ODBC Driver 18 for SQL Server};"
                "Server=AKHAND\\SQLEXPRESS;"
                "Database=Car_Rental_System;"
                "TrustServerCertificate=yes;"
                "Trusted_Connection=yes;"
            )
            conn = pyodbc.connect(connection_string)
            print("Database connection established successfully.")
            return conn
        except pyodbc.Error as e:
            print(f"Error while connecting to the DB: {e}")
            return None  # Return None if the connection fails


# Usage example
if __name__ == "__main__":
    conn = DBConnUtil.create_db_connection()

    if conn:
        conn.close()
