import customtkinter as ctk


from database.database import (
    create_attendance_table,
    create_tables,
    insert_default_users,
    create_student_table
)


from ui.login import LoginPage



# ---------------- DATABASE INITIALIZATION ----------------

# Create users table
create_tables()


# Insert default users
insert_default_users()


# Create student table
create_student_table()

# Create attendance table
create_attendance_table()



# ---------------- APPLICATION WINDOW ----------------


app = ctk.CTk()


app.title(
    "VisionX AI Smart Campus System"
)


app.geometry(
    "1200x700"
)


# Dark mode
ctk.set_appearance_mode("dark")


# Theme color
ctk.set_default_color_theme("blue")



# Open Login Page

login = LoginPage(app)



# Run application

app.mainloop()