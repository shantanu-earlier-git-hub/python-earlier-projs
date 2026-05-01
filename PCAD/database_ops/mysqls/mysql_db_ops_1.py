from database_ops.mysqls import mysql_pool_factory

mysql_testdb_config = {
    "user": "dbuser",
    "password": "passw0rd",
    "host": "localhost",
    "database": "test",
    "port": "3306"
}


def fetch_data():
    connection = None
    try:
        connection = mysql_pool_factory(dbconfig= mysql_testdb_config).get_connection()
        query_str = "select * from employees"
        with connection.cursor() as cursor:
            cursor.execute(query_str)
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print(e)
    finally:
        if connection:
            connection.close()


if __name__ == '__main__':
    try:
        fetch_data()
    except Exception as e:
        print(e)
