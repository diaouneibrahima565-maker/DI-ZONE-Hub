##################################################
# dashboard.py
# Builds the DI-ZONE HUB interface
##################################################

import customtkinter
import navigation
import settings_manager
import profile_manager

def build_dashboard(app):
    # --------------------------------------------------
    # MAIN DASHBOARD FRAME
    # --------------------------------------------------

    dashboard_frame = customtkinter.CTkFrame(master=app)
    dashboard_frame.grid(
        row=0,
        column=0,
        padx=20,
        pady=20,
        sticky="nsew"
    )

    dashboard_frame.grid_rowconfigure(0, weight=0)
    dashboard_frame.grid_rowconfigure(1, weight=1)
    dashboard_frame.grid_rowconfigure(2, weight=0)

    dashboard_frame.grid_columnconfigure(0, weight=0)
    dashboard_frame.grid_columnconfigure(1, weight=1)

    # --------------------------------------------------
    # HEADER FRAME
    # --------------------------------------------------

    header_frame = customtkinter.CTkFrame(
        master=dashboard_frame,
        height=70
    )
    header_frame.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="ew"
    )

    header_frame.grid_columnconfigure(0, weight=0)
    header_frame.grid_columnconfigure(1, weight=1)
    header_frame.grid_columnconfigure(2, weight=0)

    # --------------------------------------------------
    # SIDEBAR FRAME
    # --------------------------------------------------

    sidebar_frame = customtkinter.CTkFrame(
        master=dashboard_frame,
        width=220
    )
    sidebar_frame.grid(
        row=1,
        column=0,
        padx=8,
        pady=8,
        sticky="ns"
    )

    sidebar_frame.grid_columnconfigure(0, weight=1)

    # --------------------------------------------------
    # CONTENT FRAME
    # --------------------------------------------------

    content_frame = customtkinter.CTkFrame(
        master=dashboard_frame
    )
    content_frame.grid(
        row=1,
        column=1,
        sticky="nsew"
    )

    content_frame.grid_rowconfigure(1, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # --------------------------------------------------
    # STATUS BAR FRAME
    # --------------------------------------------------

    status_bar_frame = customtkinter.CTkFrame(
        master=dashboard_frame
    )
    status_bar_frame.grid(
        row=2,
        column=0,
        columnspan=2,
        sticky="ew"
    )

    status_bar_frame.grid_columnconfigure(0, weight=1)
    status_bar_frame.grid_columnconfigure(1, weight=0)

    status_label = customtkinter.CTkLabel(
        master=status_bar_frame,
        text="Status: Ready",
        fg_color="transparent"
    )
    status_label.grid(
        row=0,
        column=0,
        padx=10,
        pady=5,
        sticky="w"
    )

    def update_status(message):
        status_label.configure(text=message)


    def change_theme(appearance_mode):
        customtkinter.set_appearance_mode(appearance_mode)

        saved = settings_manager.save_appearance_mode(appearance_mode)

        if saved:
            update_status(f"Theme changed to {appearance_mode} and saved.")
        else:
            update_status(f"Theme changed to {appearance_mode} but could not be saved.")


    version_label = customtkinter.CTkLabel(
        master=status_bar_frame,
        text="Version 0.1.0",
        fg_color="transparent"
    )
    version_label.grid(
        row=0,
        column=1,
        padx=10,
        pady=5,
        sticky="e"
    )

    # --------------------------------------------------
    # HEADER WIDGETS
    # --------------------------------------------------

    hub_label = customtkinter.CTkLabel(
        master=header_frame,
        text="DI-ZONE HUB",
        fg_color="transparent"
    )
    hub_label.grid(
        row=0,
        column=0,
        padx=15,
        pady=10,
        sticky="w"
    )

    search_entry = customtkinter.CTkEntry(
        master=header_frame,
        placeholder_text="Search"
    )
    search_entry.grid(
        row=0,
        column=1,
        padx=20,
        pady=10,
        sticky="ew"
    )

    search_entry.bind(
        "<KeyRelease>",
        lambda event: navigation.search_apps(
            content_frame,
            search_entry.get(),
            update_status
        )
    )

    profile = profile_manager.load_profile()

    profile_button = customtkinter.CTkButton(master = header_frame, text = profile["username"], command = lambda: navigation.show_profile(
        content_frame,
        update_status,
        refresh_profile_header
        )
        )
    profile_button.grid(row = 0, column = 2, padx = 15, pady = 10, sticky = 'e')

    def refresh_profile_header(username):
        profile_button.configure(text = username)

    # --------------------------------------------------
    # SIDEBAR BUTTONS
    # --------------------------------------------------

    home_button = customtkinter.CTkButton(
        master=sidebar_frame,
        text="Home",
        command=lambda: navigation.show_home(
            content_frame,
            update_status
        )
    )
    home_button.grid(
        row=0,
        column=0,
        padx=10,
        pady=5,
        sticky="ew"
    )

    arena_button = customtkinter.CTkButton(
        master=sidebar_frame,
        text="Vanguard",
        command=lambda: navigation.show_arena(content_frame)
    )
    arena_button.grid(
        row=1,
        column=0,
        padx=10,
        pady=5,
        sticky="ew"
    )

    finance_button = customtkinter.CTkButton(
        master=sidebar_frame,
        text="Axiom",
        command=lambda: navigation.show_finance(content_frame)
    )
    finance_button.grid(
        row=2,
        column=0,
        padx=10,
        pady=5,
        sticky="ew"
    )

    social_button = customtkinter.CTkButton(
        master=sidebar_frame,
        text="Synchro",
        command=lambda: navigation.show_social(content_frame)
    )
    social_button.grid(
        row=3,
        column=0,
        padx=10,
        pady=5,
        sticky="ew"
    )

    student_button = customtkinter.CTkButton(
        master=sidebar_frame,
        text="Student",
        command=lambda: navigation.show_student(content_frame)
    )
    student_button.grid(
        row=4,
        column=0,
        padx=10,
        pady=5,
        sticky="ew"
    )

    assistant_button = customtkinter.CTkButton(
        master=sidebar_frame,
        text="Orion",
        command=lambda: navigation.show_assistant(content_frame)
    )
    assistant_button.grid(
        row=5,
        column=0,
        padx=10,
        pady=5,
        sticky="ew"
    )

    settings_button = customtkinter.CTkButton(
        master=sidebar_frame,
        text="Settings",
        command = lambda: navigation.show_settings(content_frame, change_theme)
    )
    settings_button.grid(
        row=6,
        column=0,
        padx=10,
        pady=5,
        sticky="ew"
    )

    # Display Home when the Hub opens.
    navigation.show_home(content_frame, update_status)
