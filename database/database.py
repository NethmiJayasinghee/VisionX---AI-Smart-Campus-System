import sqlite3

from datetime import datetime


DATABASE_NAME = "campus.db"



def create_connection():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    return connection

def get_total_students():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM students"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count



def get_today_attendance():

    conn = create_connection()
    cursor = conn.cursor()


    today = datetime.now().strftime("%Y-%m-%d")


    cursor.execute(
        """
        SELECT COUNT(*)
        FROM attendance
        WHERE date=?
        """,
        (today,)
    )


    count = cursor.fetchone()[0]


    conn.close()

    return count

def create_tables():

    conn = create_connection()
    cursor = conn.cursor()

    # ---------------- Students ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id TEXT,

        name TEXT,

        email TEXT,

        course TEXT,

        photo TEXT,

        face_encoding TEXT

    )
    """)

    # ---------------- Attendance ----------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id TEXT,

        student_name TEXT,

        date TEXT,

        time TEXT,

        status TEXT

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        password TEXT,

        role TEXT

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

        photo TEXT,

        face_encoding TEXT

    )
    """)


    conn.commit()
    conn.close()


def add_student(student_id, name, email, course, photo, face_encoding):

    conn = create_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO students
        (student_id,name,email,course,photo,face_encoding)

        VALUES(?,?,?,?,?,?)
        """,

        (
            student_id,
            name,
            email,
            course,
            photo,
            face_encoding
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

    print(data)   # add this

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

def create_attendance_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id TEXT,

        student_name TEXT,

        date TEXT,

        time TEXT,

        status TEXT

    )
    """)

    conn.commit()
    conn.close()

    


# def mark_attendance(student_id, student_name):

#     conn = create_connection()
#     cursor = conn.cursor()

#     now = datetime.now()

#     today = now.strftime("%Y-%m-%d")
#     current_time = now.strftime("%H:%M:%S")

#     cursor.execute(
#         """
#         INSERT INTO attendance
#         (student_id, student_name, date, time, status)

#         VALUES(?,?,?,?,?)
#         """,
#         (
#             student_id,
#             student_name,
#             today,
#             current_time,
#             "Present"
#         )
#     )

#     conn.commit()
#     conn.close()

def get_attendance():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM attendance
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data

def mark_attendance(student_id, student_name):

    conn = create_connection()
    cursor = conn.cursor()

    now = datetime.now()

    today = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    # Prevent duplicate attendance for the same day
    cursor.execute("""
        SELECT id
        FROM attendance
        WHERE student_id = ?
        AND date = ?
    """, (student_id, today))

    if cursor.fetchone():
        conn.close()
        return

    cursor.execute("""
        INSERT INTO attendance
        (
            student_id,
            student_name,
            date,
            time,
            status
        )
        VALUES (?,?,?,?,?)
    """,
    (
        student_id,
        student_name,
        today,
        current_time,
        "Present"
    ))

    conn.commit()
    conn.close()