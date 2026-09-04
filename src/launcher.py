########################################################
# launcher.py
# Launches Python files and executable applications
########################################################

import os
import subprocess
import sys


def launch_application(app_path):
    """
    Launch a Python file or executable.

    Returns:
        success: True or False
        message: Description of the result
    """

    # No path was provided.
    if not app_path:
        return False, "No application path was provided."

    # The file does not exist.
    if not os.path.exists(app_path):
        return False, f"Application not found: {app_path}"

    try:
        # Launch Python files with the current Python interpreter.
        if app_path.lower().endswith(".py"):
            subprocess.Popen(
                [sys.executable, app_path],
                cwd=os.path.dirname(app_path)
            )

        # Launch executable files directly.
        else:
            subprocess.Popen(
                [app_path],
                cwd=os.path.dirname(app_path)
            )

        return True, "Application launched successfully."

    except OSError as error:
        return False, f"Could not launch application: {error}"