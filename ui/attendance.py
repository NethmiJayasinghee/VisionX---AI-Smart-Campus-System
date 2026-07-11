import customtkinter as ctk

from ai.face_recognition import start_face_recognition
from database.database import get_attendance


class AttendancePage:

    def __init__(self, parent):

        self.parent = parent

        self.build_ui()


    def build_ui(self):

        title = ctk.CTkLabel(
            self.parent,
            text="Face Attendance",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)


        scan_btn = ctk.CTkButton(
            self.parent,
            text="📷 Start Face Recognition",
            width=250,
            height=45,
            command=self.start_scan
        )

        scan_btn.pack(pady=20)


        self.listbox = ctk.CTkTextbox(
            self.parent,
            width=700,
            height=350
        )

        self.listbox.pack(pady=20)


        self.load_attendance()


    def start_scan(self):

        start_face_recognition()

        self.load_attendance()


    def load_attendance(self):

        self.listbox.delete("1.0", "end")

        data = get_attendance()

        self.listbox.insert(
            "end",
            "Student ID\tName\tDate\tTime\tStatus\n"
        )

        self.listbox.insert(
            "end",
            "-" * 100 + "\n"
        )

        for row in data:

            self.listbox.insert(
                "end",
                f"{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\n"
            )