import pymysql
from datetime import datetime

def insert_execution_time():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            database="appdb",
            unix_socket="/var/run/mysqld/mysqld.sock"
        )
        cursor = conn.cursor()
        now = datetime.now()
        cursor.execute("INSERT INTO executions (executed_at) VALUES (%s)", (now,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Hola world")
    except pymysql.MySQLError as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    insert_execution_time()
