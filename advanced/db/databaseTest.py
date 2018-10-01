import sqlite3

def Main():
    try:
        connection = sqlite3.connect('Company.db')
        cursor = connection.cursor()
        cursor.execute('SELECT SQLITE_VERSION()')
        data = cursor.fetchone()
        print "SQLite version: " + str(data)

        cursor.executescript("""
            DROP TABLE IF EXISTS Staff;
            CREATE TABLE Staff(
                                Id INT PRIMARY KEY,
                                Name Text NOT NULL,
                                Age INT  NOT NULL,
                                Address CHAR(50),Salary REAL
                                );

            INSERT INTO Staff (Id, Name, Age, Address, Salary) VALUES (1, "Paul", 32, "California", 20000.00 );

                            """)
        staffs = (
            (2, "Allen", 25, "Texas", 15000.00),
            (3, "Teddy", 23, "Norway", 20000.00),
            (4, "Mark", 25, "Rich-Mond", 65000.00),
            (5, "David", 27, "Texas", 85000.00),
            (6, "Kim", 22, "South-Hall", 45000.00 )
        )

        cursor.executemany("INSERT INTO Staff VALUES(?, ?, ?, ?, ?)", staffs)

        connection.commit()

        cursor.execute('SELECT * FROM Staff')

        data = cursor.fetchall()

        print "Staff Info: "

        for row in data:
            print row

    except sqlite3.Error, e:
        if connection:
            connection.rollback()
            print "There was a problem with the sql"
            print  e

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    Main()
