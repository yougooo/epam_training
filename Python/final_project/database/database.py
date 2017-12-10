
# python 3

import psycopg2


connection_row = "dbname=library user=alex password=95qaz26plm"


with psycopg2.connect(connection_row) as connect:
    with connect.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS books_list")
        cursor.execute("DROP TABLE IF EXISTS authors")
        cursor.execute("DROP TABLE IF EXISTS genre")
        cursor.execute("DROP TABLE IF EXISTS books")

        # Create authors table for e-library app
        cursor.execute("CREATE TABLE authors(" +
                       "id SERIAL PRIMARY KEY," +
                       "first_name VARCHAR(25) NOT NULL," +
                       "last_name VARCHAR(25) NOT NULL," +
                       "born_date DATE NOT NULL," +
                       "country VARCHAR(30)," +
                       "UNIQUE(first_name, last_name, born_date))")

        print('Table authors. OK')

        cursor.execute("CREATE TABLE genre(" +
                        "id SERIAL PRIMARY KEY," +
                        "genre VARCHAR(30) NOT NULL)")

        print('Table genre. OK')

        cursor.execute("CREATE TABLE books(" +
                       "id SERIAL PRIMARY KEY," +
                       "book_name VARCHAR(100) NOT NULL," +
                       "publication_date DATE NOT NULL," +
                       "description TEXT," +
                       "UNIQUE(book_name, publication_date))")

        print('Table books. OK')

        cursor.execute("CREATE TABLE books_list(" +
                       "author_id int4 REFERENCES authors (id) " +
                       "ON UPDATE CASCADE ON DELETE CASCADE," +
                       "book_id int4 REFERENCES books (id) " +
                       "ON UPDATE CASCADE ON DELETE CASCADE," +
                       "genre_id int4 REFERENCES genre (id) " +
                       "ON UPDATE CASCADE ON DELETE CASCADE," +
                       "CONSTRAINT list_id PRIMARY KEY (author_id, book_id))")

        print('Table books_list. OK')

        connect.commit()
        cursor.close()

    print('All changes were successfully saved.')

