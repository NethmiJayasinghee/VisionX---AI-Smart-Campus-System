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

def create_student_table():

    conn = create_connection()

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id TEXT,

        name TEXT,

        email TEXT,

        course TEXT,

        photo TEXT

    )
    """)


    conn.commit()

    conn.close()



def add_student(student_id, name, email, course, photo):

    conn = create_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO students
        (student_id,name,email,course,photo)

        VALUES(?,?,?,?,?)
        """,

        (
            student_id,
            name,
            email,
            course,
            photo
        )
    )


    conn.commit()

    conn.close()



def get_students():

    conn = create_connection()

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM students"
    )


    data = cursor.fetchall()


    conn.close()


    return data



def delete_student(student_id):

    conn = create_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM students
        WHERE student_id=?
        """,
        (student_id,)
    )


    conn.commit()

    conn.close()
    
def search_students(keyword):

    conn = create_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT * FROM students
        WHERE student_id LIKE ?
        OR name LIKE ?
        """,

        (
            "%" + keyword + "%",
            "%" + keyword + "%"
        )
    )


    result = cursor.fetchall()


    conn.close()


    return result