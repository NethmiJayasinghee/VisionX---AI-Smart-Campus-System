import customtkinter as ctk

from database.database import (
    add_student,
    get_students
)



class StudentsPage:


    def __init__(self, parent):

        self.parent = parent

        self.create_ui()



    def create_ui(self):


        title = ctk.CTkLabel(
            self.parent,
            text="Student Management",
            font=("Arial",30,"bold")
        )

        title.pack(
            pady=20
        )



        # Student ID

        self.student_id = ctk.CTkEntry(
            self.parent,
            placeholder_text="Student ID",
            width=300
        )

        self.student_id.pack(
            pady=5
        )



        # Name

        self.name = ctk.CTkEntry(
            self.parent,
            placeholder_text="Student Name",
            width=300
        )

        self.name.pack(
            pady=5
        )



        # Email

        self.email = ctk.CTkEntry(
            self.parent,
            placeholder_text="Email",
            width=300
        )

        self.email.pack(
            pady=5
        )



        # Course

        self.course = ctk.CTkEntry(
            self.parent,
            placeholder_text="Course",
            width=300
        )

        self.course.pack(
            pady=5
        )



        add_btn = ctk.CTkButton(
            self.parent,
            text="Add Student",
            command=self.add
        )

        add_btn.pack(
            pady=10
        )



        # Student List

        self.listbox = ctk.CTkTextbox(
            self.parent,
            width=700,
            height=250
        )

        self.listbox.pack(
            pady=20
        )



        view_btn = ctk.CTkButton(
            self.parent,
            text="Refresh Students",
            command=self.view
        )

        view_btn.pack()



        self.view()



    # Add Student

    def add(self):


        add_student(

            self.student_id.get(),

            self.name.get(),

            self.email.get(),

            self.course.get(),

            ""

        )


        self.clear_fields()

        self.view()



    # Display Students

    def view(self):


        self.listbox.delete(
            "0.0",
            "end"
        )


        students = get_students()


        for student in students:


            self.listbox.insert(

                "end",

                f"""
Student ID : {student[1]}
Name       : {student[2]}
Email      : {student[3]}
Course     : {student[4]}


----------------------------

"""

            )



    def clear_fields(self):

        self.student_id.delete(
            0,
            "end"
        )

        self.name.delete(
            0,
            "end"
        )

        self.email.delete(
            0,
            "end"
        )

        self.course.delete(
            0,
            "end"
        )