import customtkinter as ctk

from database.database import (
    add_student,
    get_students,
    search_students,
    delete_student
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



        # ---------------- FORM ----------------


        self.student_id = ctk.CTkEntry(
            self.parent,
            placeholder_text="Student ID",
            width=300
        )

        self.student_id.pack(
            pady=5
        )



        self.name = ctk.CTkEntry(
            self.parent,
            placeholder_text="Student Name",
            width=300
        )

        self.name.pack(
            pady=5
        )



        self.email = ctk.CTkEntry(
            self.parent,
            placeholder_text="Email",
            width=300
        )

        self.email.pack(
            pady=5
        )



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
            command=self.add_student
        )

        add_btn.pack(
            pady=10
        )



        # ---------------- SEARCH ----------------


        self.search_box = ctk.CTkEntry(
            self.parent,
            placeholder_text="Search by ID or Name",
            width=300
        )

        self.search_box.pack(
            pady=5
        )



        search_btn = ctk.CTkButton(
            self.parent,
            text="Search",
            command=self.search
        )

        search_btn.pack(
            pady=5
        )



        # ---------------- DELETE ----------------


        delete_btn = ctk.CTkButton(
            self.parent,
            text="Delete Student",
            fg_color="red",
            command=self.delete
        )

        delete_btn.pack(
            pady=5
        )



        # ---------------- DISPLAY ----------------


        self.listbox = ctk.CTkTextbox(

            self.parent,

            width=700,

            height=250

        )

        self.listbox.pack(
            pady=20
        )



        refresh_btn = ctk.CTkButton(

            self.parent,

            text="Refresh",

            command=self.load_students

        )

        refresh_btn.pack()



        self.load_students()



    # ---------------- ADD ----------------


    def add_student(self):


        add_student(

            self.student_id.get(),

            self.name.get(),

            self.email.get(),

            self.course.get(),

            ""

        )


        self.clear()

        self.load_students()



    # ---------------- LOAD ----------------


    def load_students(self):


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



    # ---------------- SEARCH ----------------


    def search(self):


        keyword = self.search_box.get()


        self.listbox.delete(
            "0.0",
            "end"
        )


        students = search_students(keyword)



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



    # ---------------- DELETE ----------------


    def delete(self):


        student_id = self.student_id.get()


        delete_student(student_id)


        self.load_students()



    # ---------------- CLEAR ----------------


    def clear(self):


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