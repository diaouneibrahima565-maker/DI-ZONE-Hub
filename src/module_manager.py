####################################################
# PSEUDOCODE — module_manager.py
####################################################

# CREATE a variable named APPLICATIONS.

APPLICATIONS = [
    {
        "name": "Vanguard",
        "description": "A futuristic tactical game.",
        "status": "Coming Soon",
        "path": None
    },
    {
        "name": "Axiom",
        "description": "A personal finance management application.",
        "status": "Coming Soon",
        "path": None
    },
    {
        "name": "Synchro",
        "description": "A community and messaging platform.",
        "status": "Coming Soon",
        "path": None
    },
    {
        "name": "Student",
        "description": "A college planning and academic management application.",
        "status": "Planned",
        "path": None
    },
    {
        "name": "Orion",
        "description": "A desktop assistant for the DI-ZONE ecosystem.",
        "status": "Coming Soon",
        "path": None
    }
]

# DEFINE a function named get_all_applications.
def get_all_applications():
    return APPLICATIONS

