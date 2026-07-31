import customtkinter as ctk
import pyautogui
import keyboard
import threading
import time


# ==============================
# AUTO CLICKER CUSTOM SETTINGS
# ==============================

APP_NAME = "My Auto Clicker"
VERSION = "1.0"

THEME = "dark"        # dark / light / system
COLOR = "blue"        # blue / green / dark-blue

START_KEY = "f6"
EXIT_KEY = "esc"


# ==============================
# CLICKER SYSTEM
# ==============================

running = False


def click_engine():
    global running

    while running:
        try:
            delay = float(speed_entry.get())
        except:
            delay = 0.05

        button = click_type.get().lower()

        pyautogui.click(
            button=button
        )

        time.sleep(delay)



def toggle_clicker():

    global running

    if running:
        running = False
        start_button.configure(
            text="START"
        )

    else:
        running = True

        start_button.configure(
            text="STOP"
        )

        threading.Thread(
            target=click_engine,
            daemon=True
        ).start()



def close_app():
    global running

    running = False
    app.destroy()



# ==============================
# GUI AREA
# ==============================

ctk.set_appearance_mode(THEME)
ctk.set_default_color_theme(COLOR)


app = ctk.CTk()

app.title(
    f"{APP_NAME} v{VERSION}"
)

app.geometry(
    "450x550"
)

app.resizable(
    False,
    False
)



# Logo / Title
title = ctk.CTkLabel(
    app,
    text=APP_NAME,
    font=(
        "Arial",
        30,
        "bold"
    )
)

title.pack(
    pady=30
)



# Settings Card
settings = ctk.CTkFrame(
    app,
    corner_radius=20
)

settings.pack(
    padx=25,
    pady=10,
    fill="both"
)



# Speed
ctk.CTkLabel(
    settings,
    text="Click Delay"
).pack(
    pady=(20,5)
)


speed_entry = ctk.CTkEntry(
    settings,
    width=250
)

speed_entry.insert(
    0,
    "0.01"
)

speed_entry.pack()



# Button Type
ctk.CTkLabel(
    settings,
    text="Mouse Button"
).pack(
    pady=(20,5)
)


click_type = ctk.CTkComboBox(
    settings,
    values=[
        "LEFT",
        "RIGHT",
        "MIDDLE"
    ],
    width=250
)

click_type.set(
    "LEFT"
)

click_type.pack()



# Main Button

start_button = ctk.CTkButton(
    app,
    text="START",
    width=250,
    height=50,
    corner_radius=15,
    command=toggle_clicker
)

start_button.pack(
    pady=35
)



# Info

info = ctk.CTkLabel(
    app,
    text=f"""
Hotkey:
{START_KEY.upper()} = Start/Stop
{EXIT_KEY.upper()} = Exit

Made with Python
"""
)

info.pack()



# Hotkeys

keyboard.add_hotkey(
    START_KEY,
    toggle_clicker
)

keyboard.add_hotkey(
    EXIT_KEY,
    close_app
)


app.protocol(
    "WM_DELETE_WINDOW",
    close_app
)


app.mainloop()