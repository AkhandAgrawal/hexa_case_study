import pyodbc

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            try:
                connection_string = (
                    "Driver={ODBC Driver 18 for SQL Server};"
                    "Server=AKHAND\\SQLEXPRESS;"
                    "Database=CaseStudyCRS;"
                    "TrustServerCertificate=yes;"
                    "Trusted_Connection=yes;" 
                )
                DBConnection.connection = pyodbc.connect(connection_string)
                print("Connection successful")
            except pyodbc.Error as e:
                print(f"Error connecting to the database: {e}")
        else:
            print("Connection already established")

        return DBConnection.connection



try:
    conn = DBConnection.getConnection()
finally:
    if conn:
        conn.close()
        print("Connection closed")
