# ============================================================
# app_card.py
# Creates reusable application cards for DI-ZONE HUB
# ============================================================

import customtkinter
import launcher


def handle_open(app_data, update_status):
    """
    Handle the Open button for one application card.
    """

    app_name = app_data["name"]
    app_path = app_data.get("path")

    # The application does not exist yet.
    if not app_path:
        update_status(f"{app_name} is not available yet.")
        return

    # Tell the user that the launch process has started.
    update_status(f"Launching {app_name}...")

    # launcher.py should return:
    # success = True or False
    # message = text explaining the result
    success, message = launcher.launch_application(app_path)

    if success:
        update_status(f"{app_name} launched successfully.")
    else:
        update_status(message)


def create_app_card(
    parent,
    app_data,
    row,
    column,
    update_status
):
    """
    Create one reusable application card.

    parent:
        The frame where the card appears.

    app_data:
        Dictionary containing name, description,
        status, and path.

    row / column:
        Position of the card.

    update_status:
        Function used to change the dashboard status bar.
    """

    card_frame = customtkinter.CTkFrame(
        master=parent,
        corner_radius=12
    )
    card_frame.grid(
        row=row,
        column=column,
        padx=10,
        pady=10,
        sticky="nsew"
    )

    card_frame.grid_columnconfigure(0, weight=1)

    name_label = customtkinter.CTkLabel(
        master=card_frame,
        text=app_data["name"],
        font=("Arial", 18, "bold")
    )
    name_label.grid(
        row=0,
        column=0,
        padx=15,
        pady=(15, 5),
        sticky="w"
    )

    description_label = customtkinter.CTkLabel(
        master=card_frame,
        text=app_data["description"],
        wraplength=280,
        justify="left"
    )
    description_label.grid(
        row=1,
        column=0,
        padx=15,
        pady=5,
        sticky="w"
    )

    app_status_label = customtkinter.CTkLabel(
        master=card_frame,
        text=f'Status: {app_data["status"]}'
    )
    app_status_label.grid(
        row=2,
        column=0,
        padx=15,
        pady=5,
        sticky="w"
    )

    open_button = customtkinter.CTkButton(
        master=card_frame,
        text="Open",
        command=lambda: handle_open(
            app_data,
            update_status
        )
    )
    open_button.grid(
        row=3,
        column=0,
        padx=15,
        pady=(5, 15),
        sticky="ew"
    )