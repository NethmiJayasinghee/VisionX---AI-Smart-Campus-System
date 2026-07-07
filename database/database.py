import sqlite3


DATABASE_NAME = "campus.db"


def create_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection



def create_tables():

    conn = create_connection()
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL

    )
    """)


    conn.commit()
    conn.close()



def insert_default_users():

    conn = create_connection()
    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM users"
    )


    if cursor.fetchone() is None:


        users = [

            ("admin", "admin123", "Admin"),

            ("student", "student123", "Student"),

            ("security", "security123", "Security")

        ]


        cursor.executemany(
            """
            INSERT INTO users
            (username,password,role)

            VALUES(?,?,?)
            """,
            users
        )


    conn.commit()
    conn.close()



def check_login(username, password):

    conn = create_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT role FROM users
        WHERE username=? AND password=?
        """,
        (username,password)
    )


    result = cursor.fetchone()

    conn.close()


    return result