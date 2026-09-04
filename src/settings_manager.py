####################################################
# PSEUDOCODE — settings_manager.py
####################################################

# IMPORT json.
import json
# IMPORT os.
import os

# CREATE a constant named SETTINGS_FILE.
SETTINGS_FILE = "settings.json"        # Variable intended to be a constant.
# CREATE a dictionary named DEFAULT_SETTINGS.
DEFAULT_SETTINGS = {'appearance_mode': 'dark',
                    'language': 'English'}

####################################################
# PSEUDOCODE — save_settings
####################################################

# DEFINE a function named save_settings.
def save_settings(settings):
    try:
        with open(
            SETTINGS_FILE,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(settings, file, indent=4)

        return True

    except OSError as error:
        print(f"Could not save settings: {error}")
        return False

####################################################
# PSEUDOCODE — load_settings
####################################################

# DEFINE a function named load_settings.
def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        settings = DEFAULT_SETTINGS.copy()
        save_settings(settings)
        return settings

    try:
        with open(
            SETTINGS_FILE,
            "r",
            encoding = "utf-8"
        ) as file:
            saved_settings = json.load(file)
            return saved_settings
    except json.JSONDecodeError:
        print('settings file is invalid.')
        return DEFAULT_SETTINGS.copy()

    except OSError:
        print('Could not open settings file.')
        return DEFAULT_SETTINGS.copy()

####################################################
# PSEUDOCODE — save_appearance_mode
####################################################

# DEFINE a function named save_appearance_mode.
def save_appearance_mode(appearance_mode):

    settings = load_settings()
    
    settings["appearance_mode"] = appearance_mode

    return save_settings(settings)

