####################################################
# navigation.py
# Controls pages, searching, and application cards
####################################################

import customtkinter
from app_card import create_app_card
import module_manager
import profile_manager

# --------------------------------------------------
# CLEAR CURRENT PAGE
# --------------------------------------------------

def clear_content(content_frame):
    """Destroy every widget currently inside the content area."""

    for child in content_frame.winfo_children():
        child.destroy()


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

def show_home(content_frame, update_status, applications=None):
    """Display application cards on the Home page."""

    clear_content(content_frame)

    if applications is None:
        applications = module_manager.get_all_applications()

    content_frame.grid_rowconfigure(0, weight=0)
    content_frame.grid_rowconfigure(1, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    page_title = customtkinter.CTkLabel(
        master=content_frame,
        text="DI-ZONE Applications",
        font=("Arial", 24, "bold")
    )
    page_title.grid(
        row=0,
        column=0,
        padx=20,
        pady=(20, 10),
        sticky="w"
    )

    applications_frame = customtkinter.CTkScrollableFrame(
        master=content_frame,
        fg_color="transparent",
        corner_radius=0
    )
    applications_frame.grid(
        row=1,
        column=0,
        padx=10,
        pady=(0, 10),
        sticky="nsew"
    )

    applications_frame.grid_columnconfigure(0, weight=1)
    applications_frame.grid_columnconfigure(1, weight=1)

    if not applications:
        no_results_label = customtkinter.CTkLabel(
            master=applications_frame,
            text="No applications found.",
            font=("Arial", 18)
        )
        no_results_label.grid(
            row=0,
            column=0,
            columnspan=2,
            padx=20,
            pady=40
        )
        return

    row = 0
    column = 0

    for app_data in applications:
        create_app_card(
            parent=applications_frame,
            app_data=app_data,
            row=row,
            column=column,
            update_status=update_status
        )

        column += 1

        if column == 2:
            column = 0
            row += 1


# --------------------------------------------------
# SEARCH
# --------------------------------------------------

def search_apps(content_frame, search_text, update_status):
    """Filter application cards using the search text."""

    search_text = search_text.strip().lower()

    if search_text == "":
        show_home(
            content_frame,
            update_status
        )
        return

    matching_apps = []

    for app_data in module_manager.get_all_applications():
        app_name = app_data["name"].lower()
        description = app_data["description"].lower()

        if search_text in app_name or search_text in description:
            matching_apps.append(app_data)

    show_home(
        content_frame,
        update_status,
        matching_apps
    )


# --------------------------------------------------
# OTHER PAGES
# --------------------------------------------------
def show_student(content_frame):
    clear_content(content_frame)

    page_title_label = customtkinter.CTkLabel(
        content_frame,
        text="DI-ZONE Student"
    )
    page_title_label.pack(pady=(30, 10))

    temporary_message = customtkinter.CTkLabel(
        content_frame,
        text="Student module coming soon..."
    )
    temporary_message.pack()

    
def show_arena(content_frame):
    clear_content(content_frame)

    page_title_label = customtkinter.CTkLabel(
        content_frame,
        text="DI-ZONE Arena"
    )
    page_title_label.pack(pady=(30, 10))

    temporary_message = customtkinter.CTkLabel(
        content_frame,
        text="Arena module coming soon..."
    )
    temporary_message.pack()


def show_finance(content_frame):
    clear_content(content_frame)

    page_title_label = customtkinter.CTkLabel(
        content_frame,
        text="DI-ZONE Finance"
    )
    page_title_label.pack(pady=(30, 10))

    temporary_message = customtkinter.CTkLabel(
        content_frame,
        text="Finance module coming soon..."
    )
    temporary_message.pack()


def show_social(content_frame):
    clear_content(content_frame)

    page_title_label = customtkinter.CTkLabel(
        content_frame,
        text="DI-ZONE Social"
    )
    page_title_label.pack(pady=(30, 10))

    temporary_message = customtkinter.CTkLabel(
        content_frame,
        text="Social module coming soon..."
    )
    temporary_message.pack()


def show_assistant(content_frame):
    clear_content(content_frame)

    page_title_label = customtkinter.CTkLabel(
        content_frame,
        text="DI-ZONE AI Assistant"
    )
    page_title_label.pack(pady=(30, 10))

    temporary_message = customtkinter.CTkLabel(
        content_frame,
        text="AI module coming soon..."
    )
    temporary_message.pack()


def show_settings(content_frame, change_theme):
    # Clear whatever page is currently open.
    clear_content(content_frame)

    # Allow the page to expand.
    content_frame.grid_rowconfigure(0, weight=0)
    content_frame.grid_rowconfigure(1, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)

    # Page title.
    page_title = customtkinter.CTkLabel(
        master=content_frame,
        text="Settings",
        font=("Arial", 24, "bold")
    )
    page_title.grid(
        row=0,
        column=0,
        padx=20,
        pady=(20, 10),
        sticky="w"
    )

    # Main settings container.
    settings_frame = customtkinter.CTkFrame(
        master=content_frame
    )
    settings_frame.grid(
        row=1,
        column=0,
        padx=20,
        pady=20,
        sticky="nsew"
    )

    settings_frame.grid_columnconfigure(0, weight=1)

    # Appearance section.
    appearance_label = customtkinter.CTkLabel(
        master=settings_frame,
        text="Appearance",
        font=("Arial", 18, "bold")
    )
    appearance_label.grid(
        row=0,
        column=0,
        padx=15,
        pady=(15, 10),
        sticky="w"
    )

    # Theme buttons (commands will be added later).
    dark_button = customtkinter.CTkButton(
        master=settings_frame,
        text="Dark Theme", command = lambda: change_theme('dark')
    )
    dark_button.grid(
        row=1,
        column=0,
        padx=15,
        pady=5,
        sticky="ew"
    )

    light_button = customtkinter.CTkButton(
        master=settings_frame,
        text="Light Theme", command = lambda: change_theme('light')
    )
    light_button.grid(
        row=2,
        column=0,
        padx=15,
        pady=5,
        sticky="ew"
    )

    system_button = customtkinter.CTkButton(
        master=settings_frame,
        text="System Theme", command = lambda: change_theme('system')
    )
    system_button.grid(
        row=3,
        column=0,
        padx=15,
        pady=(5, 15),
        sticky="ew"
    )

    page_title_label = customtkinter.CTkLabel(
        content_frame,
        text="Settings"
    )
    page_title_label.grid(row = 0, column = 0, padx = 10, pady = (30,10), sticky = 'w')

def show_profile(content_frame, update_status, refresh_profile_header):

    clear_content(content_frame)

    profile = profile_manager.load_profile()

    profile_page_title = customtkinter.CTkLabel(content_frame, text = "Profile")
    profile_page_title.grid(row = 0, column = 0, sticky = 'w', padx = 5, pady = 5)

    profile_form_frame = customtkinter.CTkFrame(content_frame)
    profile_form_frame.grid(row = 1, column = 0, sticky = 'ew', padx = 8, pady = 8)
    profile_form_frame.grid_columnconfigure(0,weight = 0)
    profile_form_frame.grid_columnconfigure(1, weight = 1)

    username_label = customtkinter.CTkLabel(profile_form_frame, text = 'Username')
    username_label.grid(row = 0, column = 0)

    username_entry = customtkinter.CTkEntry(profile_form_frame)
    username_entry.grid(row = 0, column = 1, sticky = 'ew')
    username_entry.insert(0, profile["username"])

    email_label = customtkinter.CTkLabel(profile_form_frame, text = 'Email')
    email_label.grid(row = 1, column = 0)

    email_entry = customtkinter.CTkEntry(profile_form_frame)
    email_entry.grid(row = 1, column = 1, sticky = 'ew')
    email_entry.insert(1, profile['email'])

    school_label = customtkinter.CTkLabel(profile_form_frame, text = 'School')
    school_label.grid(row = 2, column = 0)

    school_entry = customtkinter.CTkEntry(profile_form_frame)
    school_entry.grid(row = 2, column = 1, sticky = 'ew')
    school_entry.insert(2, profile['school'])

    major_label = customtkinter.CTkLabel(profile_form_frame, text = 'Major')
    major_label.grid(row = 3, column = 0)

    major_entry = customtkinter.CTkEntry(profile_form_frame)
    major_entry.grid(row = 3, column = 1, sticky ='ew')
    major_entry.insert(3, profile['major'])

    def save_changes():
        username = username_entry.get()
        email = email_entry.get()
        school = school_entry.get()
        major = major_entry.get()

        success = profile_manager.update_profile(
            username,
            email,
            school,
            major
        )

        if success:
            update_status("Profile saved successfully.")
            print("Profile saved successfully.")
            refresh_profile_header(username)

        else:
            update_status("Could not save profile.")
            print("Could not save profile.")

    save_profile_button = customtkinter.CTkButton(profile_form_frame, text="Save profile",
                                                        command = save_changes)
    save_profile_button.grid(row = 5, column = 1, sticky = 'e', padx = 5, pady = 15)




