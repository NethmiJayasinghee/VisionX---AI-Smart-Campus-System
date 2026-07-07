import customtkinter as ctk

from database.database import check_login
from ui.dashboard import Dashboard



class LoginPage:


    def __init__(self, app):

        self.app = app


        self.frame = ctk.CTkFrame(
            app,
            width=400,
            height=400
        )

        self.frame.pack(
            pady=80
        )


        self.title = ctk.CTkLabel(
            self.frame,
            text="VisionX Login",
            font=("Arial", 30, "bold")
        )

        self.title.pack(
            pady=30
        )


        self.username = ctk.CTkEntry(
            self.frame,
            placeholder_text="Username",
            width=250
        )

        self.username.pack(
            pady=10
        )


        self.password = ctk.CTkEntry(
            self.frame,
            placeholder_text="Password",
            show="*",
            width=250
        )

        self.password.pack(
            pady=10
        )


        self.login_button = ctk.CTkButton(
            self.frame,
            text="LOGIN",
            width=250,
            command=self.login
        )

        self.login_button.pack(
            pady=20
        )


        self.message = ctk.CTkLabel(
            self.frame,
            text=""
        )

        self.message.pack()



    def login(self):

        username = self.username.get()

        password = self.password.get()


        result = check_login(
            username,
            password
        )


        if result:

            role = result[0]


            # Open Dashboard
            Dashboard(
                self.app,
                role
            )


        else:

            self.message.configure(
                text="Invalid Username or Password",
                text_color="red"
            )