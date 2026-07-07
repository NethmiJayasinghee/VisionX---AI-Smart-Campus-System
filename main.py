import customtkinter as ctk

from database.database import (
    create_tables,
    insert_default_users
)

from ui.login import LoginPage



create_tables()

insert_default_users()



app = ctk.CTk()


app.title(
    "VisionX AI Smart Campus System"
)


app.geometry(
    "900x600"
)


login = LoginPage(app)



app.mainloop()