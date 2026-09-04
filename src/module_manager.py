####################################################
# PSEUDOCODE — module_manager.py
####################################################

# CREATE a variable named APPLICATIONS.

APPLICATIONS = [
    {
        "name": "DI-ZONE Arena",
        "description": "A futuristic tactical game.",
        "status": "Coming Soon",
        "path": None
    },
    {
        "name": "DI-ZONE Finance",
        "description": "A personal finance management application.",
        "status": "Coming Soon",
        "path": None
    },
    {
        "name": "DI-ZONE Social",
        "description": "A community and messaging platform.",
        "status": "Coming Soon",
        "path": None
    },
    {
        "name": "DI-ZONE Student",
        "description": "A college planning and academic management application.",
        "status": "Planned",
        "path": None
    },
    {
        "name": "D-Assistant",
        "description": "A desktop assistant for the DI-ZONE ecosystem.",
        "status": "Coming Soon",
        "path": None
    }
]

# DEFINE a function named get_all_applications.
def get_all_applications():
    return APPLICATIONS

