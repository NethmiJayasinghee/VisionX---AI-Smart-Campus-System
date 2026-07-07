import customtkinter as ctk


class Dashboard:


    def __init__(self, app, role):

        self.app = app
        self.role = role


        # Clear current window
        for widget in self.app.winfo_children():
            widget.destroy()


        self.create_sidebar()
        self.create_dashboard()



    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self.app,
            width=220,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )


        logo = ctk.CTkLabel(
            self.sidebar,
            text="VisionX",
            font=("Arial",32,"bold")
        )

        logo.pack(
            pady=30
        )


        buttons = [

            "🏠 Dashboard",
            "👨‍🎓 Students",
            "📷 Attendance",
            "🛡 Security",
            "🎤 Voice Assistant",
            "✋ Gesture Control",
            "📄 Reports",
            "⚙ Settings"

        ]


        for item in buttons:


            btn = ctk.CTkButton(
                self.sidebar,
                text=item,
                width=180,
                height=40
            )

            btn.pack(
                pady=8
            )



        logout = ctk.CTkButton(
            self.sidebar,
            text="Logout",
            fg_color="red"
        )

        logout.pack(
            side="bottom",
            pady=20
        )




    def create_dashboard(self):


        self.main_area = ctk.CTkFrame(
            self.app
        )


        self.main_area.pack(
            expand=True,
            fill="both",
            padx=20,
            pady=20
        )


        title = ctk.CTkLabel(
            self.main_area,
            text=f"Welcome {self.role}",
            font=("Arial",35,"bold")
        )


        title.pack(
            pady=30
        )



        cards_frame = ctk.CTkFrame(
            self.main_area
        )

        cards_frame.pack(
            pady=20
        )



        cards = [

            ("Students","0"),
            ("Attendance","0%"),
            ("Security Alerts","0"),
            ("Visitors","0")

        ]


        for name,value in cards:


            card = ctk.CTkFrame(
                cards_frame,
                width=180,
                height=120
            )

            card.pack(
                side="left",
                padx=15
            )


            label1 = ctk.CTkLabel(
                card,
                text=name,
                font=("Arial",18)
            )

            label1.pack(
                pady=15
            )


            label2 = ctk.CTkLabel(
                card,
                text=value,
                font=("Arial",30,"bold")
            )

            label2.pack()