import customtkinter as ctk

import os
import shutil
import json

from tkinter import filedialog
from tkinter import messagebox


from database.database import (
    add_student,
    get_students,
    search_students,
    delete_student
)


from ai.face_encoding import create_face_embedding



class StudentsPage:


    def __init__(self, parent):

        self.parent = parent

        self.selected_image = None

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



        # -------- FORM --------


        self.student_id = ctk.CTkEntry(
            self.parent,
            placeholder_text="Student ID",
            width=300
        )

        self.student_id.pack(pady=5)



        self.name = ctk.CTkEntry(
            self.parent,
            placeholder_text="Student Name",
            width=300
        )

        self.name.pack(pady=5)



        self.email = ctk.CTkEntry(
            self.parent,
            placeholder_text="Email",
            width=300
        )

        self.email.pack(pady=5)



        self.course = ctk.CTkEntry(
            self.parent,
            placeholder_text="Course",
            width=300
        )

        self.course.pack(pady=5)



        # -------- PHOTO UPLOAD --------


        self.photo_btn = ctk.CTkButton(

            self.parent,

            text="Choose Student Photo",

            command=self.choose_photo

        )

        self.photo_btn.pack(
            pady=10
        )



        self.photo_label = ctk.CTkLabel(

            self.parent,

            text="No image selected"

        )

        self.photo_label.pack()



        # -------- ADD BUTTON --------


        add_btn = ctk.CTkButton(

            self.parent,

            text="Add Student",

            command=self.add_student

        )

        add_btn.pack(
            pady=10
        )



        # -------- SEARCH --------


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



        # -------- DELETE --------


        delete_btn = ctk.CTkButton(

            self.parent,

            text="Delete Student",

            fg_color="red",

            command=self.delete

        )


        delete_btn.pack(
            pady=5
        )



        # -------- DISPLAY --------


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





    # ================= PHOTO SELECT =================


    def choose_photo(self):


        file = filedialog.askopenfilename(

            filetypes=[

                ("Image Files","*.jpg *.jpeg *.png")

            ]

        )


        if file:


            self.selected_image = file


            self.photo_label.configure(

                text=os.path.basename(file)

            )





    # ================= ADD STUDENT =================


    def add_student(self):

    # Validate required fields
        if (
            self.student_id.get() == "" or
            self.name.get() == "" or
            self.email.get() == "" or
            self.course.get() == ""
        ):

            messagebox.showwarning(
                "Missing Information",
                "Please fill in all student details."
            )
            return


        # Validate photo
        if not self.selected_image:

            messagebox.showwarning(
                "Photo Required",
                "Please select a student photo."
            )
            return


        photo_path = ""
        face_encoding = ""


        folder = "images/students"

        os.makedirs(
            folder,
            exist_ok=True
        )


        filename = os.path.basename(
            self.selected_image
        )


        photo_path = os.path.join(
            folder,
            filename
        )


        shutil.copy(
            self.selected_image,
            photo_path
        )


        messagebox.showinfo(
            "Please Wait",
            "Generating face encoding..."
        )


        encoding = create_face_embedding(
            photo_path
        )


        if encoding:

            face_encoding = json.dumps(
                encoding
            )

        else:

            messagebox.showerror(
                "Face Detection Failed",
                "No face detected in the selected image.\nPlease choose another clear photo."
            )
            return


        add_student(

            self.student_id.get(),

            self.name.get(),

            self.email.get(),

            self.course.get(),

            photo_path,

            face_encoding

        )


        messagebox.showinfo(
            "Success",
            "Student added successfully!"
        )


        self.clear()

        self.load_students()




    # ================= LOAD =================


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
Photo      : {student[5]}

----------------------------

"""

            )





    # ================= SEARCH =================


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





    # ================= DELETE =================


    def delete(self):


        student_id = self.student_id.get()



        delete_student(

            student_id

        )


        self.load_students()





    # ================= CLEAR =================


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


        self.selected_image = None


        self.photo_label.configure(

            text="No image selected"

        )