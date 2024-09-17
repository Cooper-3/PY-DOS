import os
import time as t

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
print()
print()
print()

# Progress Bar Function
def progress_bar(total, step, speed):
    for i in range(0, total + 1, step):
        percent = (i / total) * 100
        bar = '=' * int(percent // 2) + ' ' * (50 - int(percent // 2))
        print(f'\r[{bar}] {percent:.2f}%', end='')
        t.sleep(speed)
    print()  # Move to the next line after completion

progress_bar(total=100, step=1, speed=0.025)
print("Loading Done!")

# Print Multiple Times Function
def pmt(text, times):
    try:
        times = int(times)
        for _ in range(times):
            print(text)
    except ValueError:
        print("Invalid input for times. Please enter a valid integer.")

pmt(text=" ", times=20)

# Function to add a file name to FileDict.txt
def file_search_dictionary(file_name):
    try:
        print(f"Attempting to add {file_name} to FileDict.txt")  # Debugging statement
        with open('FileDict.txt', 'a') as file:
            file.write(file_name + '\n')
            print(f"Added {file_name} to FileDict.txt")  # Debugging statement
    except Exception as e:
        print(f"Error writing to FileDict.txt: {e}")

# Main Program
ite = 1
while int(ite) == 1:
    user_input = input("Enter 1 to enter file writer, 2 to enter the file search: ")
    print(f"User input: {user_input}")  # Debugging statement
    try:
        user_input = int(user_input)
        if user_input == 1:
            directory = r'C:\Users\coope\Desktop\Code\Python Stuff\Console Python Game\project Files'
            file_name = input("Enter the file name: ")
            file_path = f'{directory}\\{file_name}'
            print(f"File path: {file_path}")  # Debugging statement

            try:
                with open(file_path, 'r') as file:
                    existing_content = file.read()
                    if existing_content:
                        print("The file already has content:")
                        print(existing_content)
                    else:
                        print("The file is empty.")
            except FileNotFoundError:
                print("The file does not exist. It will be created.")
                print(f"Calling file_search_dictionary for {file_name}")  # Debugging statement
                file_search_dictionary(file_name)

            action = input("Do you want to append to or overwrite the file? (append/overwrite): ").strip().lower()
            print(f"Action: {action}")  # Debugging statement
            if action in ['append', 'overwrite']:
                new_content = input("Enter the new content: ")
                mode = 'a' if action == 'append' else 'w'
                with open(file_path, mode) as file:
                    file.write(new_content + ('\n' if action == 'append' else ''))
                print(f"The file has been {'appended to' if action == 'append' else 'overwritten'}.")
                print(f"Adding {file_name} to FileDict.txt")  # Debugging statement
                file_search_dictionary(file_name)  # Ensure the file is added to FileDict.txt
            else:
                print("Invalid option. Please enter 'append' or 'overwrite'.")
        elif user_input == 2:
            try:
                with open("FileDict.txt", "r") as file:
                    content = file.read()
                    print("Current FileDict.txt content:")
                    print(content)
                    # Verify if files exist
                    lines = content.splitlines()
                    for line in lines:
                        file_path = f'{directory}\\{line.strip()}'
                        if not os.path.exists(file_path):
                            print(f"Warning: {line.strip()} does not exist in the directory.")
            except FileNotFoundError:
                print("FileDict.txt does not exist.")
    except ValueError as e:
        print(f"Invalid input. Please enter a valid number. Error: {e}")
