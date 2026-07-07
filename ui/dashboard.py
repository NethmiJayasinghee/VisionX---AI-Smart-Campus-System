import customtkinter as ctk
from datetime import datetime

from ui.students import StudentsPage



class Dashboard:


    def __init__(self, app, role):

        self.app = app
        self.role = role


        # Remove login page
        for widget in self.app.winfo_children():
            widget.destroy()


        self.create_layout()

        self.show_dashboard()



    # MAIN LAYOUT

    def create_layout(self):


        self.sidebar = ctk.CTkFrame(
            self.app,
            width=230,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )


        self.content = ctk.CTkFrame(
            self.app
        )

        self.content.pack(
            side="right",
            expand=True,
            fill="both",
            padx=20,
            pady=20
        )


        self.create_sidebar()



    # SIDEBAR

    def create_sidebar(self):


        logo = ctk.CTkLabel(
            self.sidebar,
            text="VisionX",
            font=("Arial",35,"bold")
        )

        logo.pack(
            pady=30
        )


        subtitle = ctk.CTkLabel(
            self.sidebar,
            text="AI Campus System"
        )

        subtitle.pack()



        menu_items = [

            ("🏠 Dashboard", self.show_dashboard),

            ("👨‍🎓 Students", self.open_students),

            ("📷 Attendance", None),

            ("🛡 Security", None),

            ("🎤 Voice Assistant", None),

            ("✋ Gesture Control", None),

            ("📊 Reports", None),

            ("⚙ Settings", None)

        ]


        for name, command in menu_items:


            btn = ctk.CTkButton(

                self.sidebar,

                text=name,

                width=190,

                height=40,

                command=command

            )


            btn.pack(
                pady=8
            )



        user = ctk.CTkLabel(
            self.sidebar,
            text=f"Logged as\n{self.role}",
            font=("Arial",15)
        )


        user.pack(
            side="bottom",
            pady=20
        )



    # CLEAR CONTENT

    def clear_content(self):

        for widget in self.content.winfo_children():

            widget.destroy()



    # DASHBOARD HOME

    def show_dashboard(self):


        self.clear_content()


        title = ctk.CTkLabel(

            self.content,

            text=f"Welcome {self.role}",

            font=("Arial",32,"bold")

        )

        title.pack(
            pady=20
        )


        time = ctk.CTkLabel(

            self.content,

            text=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            font=("Arial",18)

        )


        time.pack()



        cards_frame = ctk.CTkFrame(
            self.content
        )

        cards_frame.pack(
            pady=40
        )


        cards = [

            ("👨‍🎓 Students","125"),

            ("📷 Attendance","96%"),

            ("🛡 Alerts","3"),

            ("👥 Visitors","20")

        ]



        for title,value in cards:


            card = ctk.CTkFrame(

                cards_frame,

                width=180,

                height=120

            )


            card.pack(
                side="left",
                padx=15
            )


            card.pack_propagate(False)



            ctk.CTkLabel(
                card,
                text=title,
                font=("Arial",18)
            ).pack(
                pady=15
            )



            ctk.CTkLabel(
                card,
                text=value,
                font=("Arial",30,"bold")
            ).pack()



        status = ctk.CTkLabel(

            self.content,

            text="System Status : ONLINE ✅",

            font=("Arial",20)

        )


        status.pack(
            pady=30
        )



    # STUDENT PAGE

    def open_students(self):

        self.clear_content()

        StudentsPage(
            self.content
        )
