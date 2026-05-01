from mysql.connector import pooling

'''
mysql db config
change it to your own mysql db config
if you don't have mysql db, create one first.
'''
mysql_config = {
    "user": "root",
    "password": "passw0rd",
    "host": "localhost",
    "database": "mysqldb",
    "port": "3306"
}



''''
create mysql db connection pool factory
connect mysql db based on db_config get_connection() function
and close it after ops.
'''


def mysql_pool_factory():
    return pooling.MySQLConnectionPool(
        pool_name='my_sql_pool',
        pool_size=5,
        **mysql_config)


def mysql_pool_factory(dbconfig: dict={}):
    return pooling.MySQLConnectionPool(
        pool_name='my_sql_pool',
        pool_size=5,
        **dbconfig)
