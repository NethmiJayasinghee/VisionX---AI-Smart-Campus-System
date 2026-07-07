import customtkinter as ctk


# Application window
app = ctk.CTk()

app.title("VisionX - AI Smart Campus System")

app.geometry("900x600")


# Main title
title = ctk.CTkLabel(
    app,
    text="VisionX AI Smart Campus System",
    font=("Arial", 30)
)

title.pack(pady=50)


# Start button
button = ctk.CTkButton(
    app,
    text="Start System"
)

button.pack(pady=20)


# Run application
app.mainloop()