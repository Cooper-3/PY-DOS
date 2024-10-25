import os
import subprocess
import time as t
import psutil

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
FILE_WARDEN = os.path.join(PROJECT_FOLDER, 'file-warden.txt')

# ASCII Art
print(
    """.·:''''''''''''''''''''''''''':·.
: :                           : :
: :  ________  ________       : :
: : |\   ____\|\   ____\      : :
: : \ \  \___|\ \  \___|_     : :
: :  \ \  \    \ \_____  \    : :
: :   \ \  \____\|____|\  \   : :
: :    \ \_______\____\_\  \  : :
: :     \|_______|\_________\ : :
: :              \|_________| : :
: :                           : :
'·:...........................:·'"""
)
t.sleep(3)

# Loading Animation
for _ in range(12):
    print()
    t.sleep(0.02)

print(" *******   **    **        *******     *******    ********")
t.sleep(0.2)
print("/**////** //**  **        /**////**   **/////**  **////// ")
t.sleep(0.2)
print("/**   /**  //****         /**    /** **     //**/**       ")
t.sleep(0.2)
print("/*******    //**    ***** /**    /**/**      /**/*********")
t.sleep(0.2)
print("/**////      /**   /////  /**    /**/**      /**////////**")
t.sleep(0.2)
print("/**          /**          /**    ** //**     **        /**")
t.sleep(0.2)
print("/**          /**          /*******   //*******   ******** ")
t.sleep(0.2)
print("//           //           ///////     ///////   ////////  ")
print("")
print("version: 1'1 PRE-ALPHA")
t.sleep(1.5)
print("*Loading*(Need any help? Join our Discord at: https://discord.gg/Vz7QGCPd)")

def load_file_list():
    """Load the list of files from file-warden.txt."""
    if not os.path.exists(FILE_WARDEN):
        return set()
    with open(FILE_WARDEN, 'r') as f:
        return set(line.strip() for line in f)

def save_file_list(file_list):
    """Save the list of files to file-warden.txt."""
    with open(FILE_WARDEN, 'w') as f:
        for file_name in file_list:
            f.write(f"{file_name}\n")

def add_files(file_names):
    """Add new files with content and update file-warden.txt."""
    file_list = load_file_list()
    for file_name in file_names:
        file_path = os.path.join(PROJECT_FOLDER, file_name)
        if file_name not in file_list:
            content = input(f"Enter content for {file_name} (press Enter for empty file): ")
            with open(file_path, 'w') as f:  # Create the file and write content
                f.write(content)
            file_list.add(file_name)
            print(f"File added: {file_name}")
        else:
            print(f"File already exists: {file_name}")
    save_file_list(file_list)

def delete_files(file_names):
    """Delete files and update file-warden.txt."""
    file_list = load_file_list()
    for file_name in file_names:
        file_path = os.path.join(PROJECT_FOLDER, file_name)
        if file_name in file_list:
            try:
                os.remove(file_path)
                file_list.remove(file_name)
                print(f"File deleted: {file_name}")
            except FileNotFoundError:
                print(f"File not found: {file_name}")
        else:
            print(f"File not listed: {file_name}")
    save_file_list(file_list)

def display_file(file_name):
    """Display the contents of a file."""
    file_path = os.path.join(PROJECT_FOLDER, file_name)
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        print(f"Contents of {file_name}:\n{contents}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")

def edit_file(file_name):
    """Display, edit, and save a file."""
    file_path = os.path.join(PROJECT_FOLDER, file_name)
    try:
        # Display contents first
        with open(file_path, 'r') as file:
            contents = file.read()
        print(f"Current contents of {file_name}:\n{contents}")

        # Get new content from user
        new_content = input("Enter new content for the file (existing content will be replaced):\n")

        # Write new content to file
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"{file_name} has been updated.")
    except FileNotFoundError:
        print(f"File not found: {file_name}")

def monitor_system():
    """Monitor system usage."""
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)        
    # RAM usage
    memory_info = psutil.virtual_memory()
    total_ram = memory_info.total / (1024 ** 3)
    available_ram = memory_info.available / (1024 ** 3)
    used_ram = memory_info.used / (1024 ** 3)
    ram_percent = memory_info.percent

    # Print system information
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Total RAM: {total_ram:.2f} GB")
    print(f"Available RAM: {available_ram:.2f} GB")
    print(f"Used RAM: {used_ram:.2f} GB")
    print(f"RAM Usage: {ram_percent}%")
    print("-" * 30)

def run_cmd():
    """Launch a command prompt interface."""
    print("Cmd launched. You can start typing commands. Type 'exit' to quit.")
    while True:
        user_input = input("cmd> ")
        
        if user_input.lower() == "exit":
            break

        # Execute the command and capture output
        process = subprocess.run(
            user_input,
            shell=True,
            capture_output=True,
            text=True
        )

        # Print the output and errors
        if process.stdout:
            print(f"Output: {process.stdout.strip()}")
        if process.stderr:
            print(f"Error: {process.stderr.strip()}")

def progress_bar(total, step, speed):
    """Display a progress bar."""
    for i in range(0, total + 1, step):
        percent = (i / total) * 100
        bar = '=' * int(percent // 2) + ' ' * (50 - int(percent // 2))
        print(f'\r[{bar}] {percent:.2f}%', end='')
        t.sleep(speed)
    print()  # Move to the next line after completion

def file_management():
    """Manage files: add, delete, display, or edit."""
    while True:
        action = input("File Management: 1 to add files, 2 to delete files, 3 to list files, 4 to display a file, 5 to edit a file, 6 to exit to main menu: ")
        if action == '1':
            files = input("Enter filenames to add (comma-separated): ").split(',')
            add_files(file.strip() for file in files)
        elif action == '2':
            files = input("Enter filenames to delete (comma-separated): ").split(',')
            delete_files(file.strip() for file in files)
        elif action == '3':
            print("Files in file-warden:")
            with open(FILE_WARDEN, 'r') as f:
                print(f.read())
        elif action == '4':
            file_name = input("Enter filename to display: ").strip()
            display_file(file_name)
        elif action == '5':
            file_name = input("Enter filename to edit: ").strip()
            edit_file(file_name)
        elif action == '6':
            break
        else:
            print("Invalid option. Please choose again.")

# Main Program
progress_bar(total=100, step=1, speed=0.050)
print("Loading Done!")

while True:
    user_select = input("1 to open files, 2 to open MS Edge, 3 to open cmd interface, 4 to open calculator, 5 to open RDL menu (Repair.Diagnostics.Links): ")
    if (int(user_select)) == 1:
        file_management()
    elif (int(user_select)) == 2:
        print("2. Accepted")
        os.system("start msedge")
    elif (int(user_select)) == 3:
        print("3. Accepted")
        cmd_control = (int(input("Press 1 to start a new window, 2 to use the cmd CLI pipe: ")))
        if cmd_control == 1:
            os.system("start cmd")
        elif cmd_control == 2:
            run_cmd()
    elif (int(user_select)) == 4:
        print("4. Accepted")
        os.system("start calc")
    elif (int(user_select)) == 5:
        print("5. Accepted")
        RDL_control = input("Do you want to [(R)epair not working], open (D)iagnostics or open (L)inks?:  ")
        if RDL_control == "D":
            monitor_system()
        elif RDL_control == 'L' :
            print("""
            https://discord.com/channels/1285700545331593216/1285700545331593218
            """)
        elif RDL_control == 'R':
            print("I told you it isn't working!")
    else:
        print("Invalid option. Please choose again.")

    ite = input("Do you want to keep running? (no=no):  ")
    if ite == 'no':
        break
for _ in range(20):
    print()