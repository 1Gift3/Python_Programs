# I Struggled with - naming, which led to conflict
# Learned that python uses a mechanism called importing to bring external lib and modules into my program. So now when i import a module, python looks for it in various locations, including built in standard lib's and my current directory.
# - So getpass is a built in module that helps secure take input like passwords without the text on screen.
# - Now in my original code i named my script getpass.py, so when i did import getpass python tried to import my own getpass.py file instead of the standard lib getpass module. That resulted in error

# I then renamed my script to get_pass.py avoiding the conflict witht the built in getpass.

# Take-away
# Naming my script the same as a built-in Python module (like getpass.py) causes Python to treat your script as that module, which can lead to issues because my script does not have the same functionality as the actual module.


# HOW
# When you want to securely take input from the user without showing char's as they type

# WHY
# It id useful when you're collecting sensitive info like passwords or pins.

# WHAT
# The getpass module hides the input as the user types it (wont be visible on the terminal)
# getpass.getpass() will prompt the user for input but will not display entered characters which then ensures the password is hidden while typing.

