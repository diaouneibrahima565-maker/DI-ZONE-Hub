import json 
import os


PROFILE_FILE = "profile.json"

DEFAULT_PROFILE = {
    "username": "Guest",
    "email": "",
    "school": "",
    "major": "",
    "theme": "dark"
}

def save_profile(profile):
    try:
        with open(PROFILE_FILE, 'w', encoding = 'utf-8') as file:
            json.dump(profile, file, indent = 4)
            return True

    except OSError:
        print('Profile could not be saved.')
        return False

def load_profile():
    if not os.path.exists(PROFILE_FILE):
        profile = DEFAULT_PROFILE.copy()
        save_profile(profile)
        return profile

    try:
        with open(PROFILE_FILE, 'r', encoding = 'utf-8') as file:
            saved_profile = json.load(file)

            profile = DEFAULT_PROFILE.copy()
            profile.update(saved_profile)

            return profile

    except json.JSONDecodeError:
        print("Profile file is invalid.")
        return DEFAULT_PROFILE.copy()

    except OSError:
        print("Could not load profile.")
        return DEFAULT_PROFILE.copy()

def update_profile(username, email, school, major):
    profile = load_profile()
    profile["username"] = username
    profile["email"] = email
    profile['school'] = school
    profile["major"] = major
    result = save_profile(profile)
    return result