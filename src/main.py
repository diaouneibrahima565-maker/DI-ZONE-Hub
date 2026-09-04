####################################################
# PSEUDOCODE — main.py
####################################################

import customtkinter
import dashboard
import settings_manager
import profile_manager

settings = settings_manager.load_settings()
profile = profile_manager.load_profile()
if not isinstance(settings, dict):
    settings = settings_manager.DEFAULT_SETTINGS.copy()

if not isinstance(profile, dict):
    profile = profile_manager.DEFAULT_PROFILE.copy()


customtkinter.set_appearance_mode(settings["appearance_mode"])

app = customtkinter.CTk()
    
app.geometry('1200x700')
app.title("DI-ZONE HUB")

app.grid_rowconfigure(0, weight = 1)
app.grid_columnconfigure(0, weight = 1)

dashboard.build_dashboard(app)

app.mainloop()