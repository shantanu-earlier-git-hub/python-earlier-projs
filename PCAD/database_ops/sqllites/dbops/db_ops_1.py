import sqlite3

con = sqlite3.connect("movies_db.db")
cur = con.cursor()


def create_table():
    global cur
    cur.execute("DROP TABLE IF EXISTS movie")
    print("Table dropped successfully")

    create_table_str = ('CREATE TABLE if not exists '
                        'movie(movie_id Serial PRIMARY KEY,'
                        'title VARCHAR(255), '
                        'year INT, '
                        'score FLOAT)')

    cur.execute(create_table_str)
    con.commit()
    print("Table created successfully")


def insert_data():
    global cur
    cur.execute("""
                INSERT INTO movie
                VALUES (1, 'Monty Python and the Holy Grail', 1975, 8.2),
                       (2, 'And Now for Something Completely Different', 1971, 7.5),
                       (3, 'movie3', 2000, 3.4),
                       (4, 'movie4', 2001, 4.2),
                       (5, 'movie5', 1890, 3.4),
                       (6, 'movie6', 2002, 5.4),
                       (7, 'movie7', 1998, 2.4),
                       (8, 'movie8', 1999, 2),
                       (9, 'movie9', 2005, 4.8),
                       (10, 'movie10', 2000, 3.4)
                """)
    con.commit()
    print("Data inserted successfully")


def fetch_all():
    global cur
    res = cur.execute("SELECT * FROM movie")
    if res:
        records = res.fetchall()
        print(" movie_id, title, year, score ", end="\n")
        for record in records:
            print(f"{record[0]}, {record[1]}, {record[2]}, {record[3]}")
    else:
        print("No record found")
    print("", end="\n")


def fetch_by_id(id):
    global cur
    # query_str = f"SELECT * FROM movie WHERE movie_id = :id "
    # params = {'id': id}
    # res = cur.execute(query_str, params)

    query_str = f"SELECT * FROM movie WHERE movie_id = ?"
    res = cur.execute(query_str, (id,))

    if res:
        record = res.fetchone()
        print(f"{record[0]}, {record[1]}, {record[2]}, {record[3]}")


if __name__ == '__main__':
    create_table()
    insert_data()
    fetch_all()
    fetch_by_id(2)
