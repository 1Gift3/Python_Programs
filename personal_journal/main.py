# it all works but i see to cant edit properly or delete entries meaning it might needa few tweaks here and there for it to functionally work nicely for me
#cater it to fit your needs 

import os 
from datetime import datetime

# create a directort for th e journal if it doesnt already exist
if not os.path.exists("MyJournal"):
    os.makedirs("MyJournal")
print("Project directory created.")    

def create_entry():
    # Get the journal entry text from the user
    entry_text = input("WHats on your mind today? ")
    
    #generate a file name based of the current dat and time
    filename = f"MyJournal/{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # save the entry 
    with open(filename, "w") as file: 
        file.write(entry_text)
    print(f"Entry saved as {filename}!")       


def view_entries():
    entries = os.listdir("MyJournal")
    if entries:
        for entry in entries:
            print(entry)
    else: 
        print("No entries found. ")

                
def read_entry(enter_name):
    filepath = f"MyJournal/{enter_name}"
    try:
        with open(filepath, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Entry not found.")                      

def update_entry(entry_name):
    filepath = f"MyJournal/{entry_name}"
    try: 
        with open(filepath, "a") as file:
            new_text = input("What's new on your mind? ")
            file.write("\n" + new_text)
        print(f"Entry {entry_name} updated.")
    except FileNotFoundError:
        print("Entry not found.")

# Sample usage to try out the functions
print("Welcome to your Personal Journal!")
create_entry()
view_entries()
read_entry(input("Which entry would you like to read?"))
update_entry(input("Which entry would you like to edit?"))
                