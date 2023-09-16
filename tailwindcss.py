import os
import subprocess
import time

# Function to display a message with a typing effect and cyber-blue color
def display_typing_message(message):
    CYBER_BLUE = '\033[96m'  # ANSI escape code for cyber blue color
    RESET = '\033[0m'  # ANSI escape code to reset text color
    for char in message:
        print(f'{CYBER_BLUE}{char}{RESET}', end='', flush=True)
        time.sleep(0.03)  # Adjust the sleep duration for the typing speed
    print()

# Function to check if a command is installed
def check_command(command):
    try:
        subprocess.check_call([command, '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        display_typing_message(f"{command} is not installed. Please install {command} before running this script.")
        exit(1)

# Function to create a file with content
def create_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# Function to create project structure
def create_project(project_name, project_path):
    project_directory = os.path.join(project_path, project_name)
    display_typing_message(f"Creating your project folder '{project_name}' in '{project_path}'...")
    os.makedirs(project_directory, exist_ok=True)
    os.chdir(project_directory)

    display_typing_message("Initializing npm and setting up Tailwind CSS...")
    subprocess.run(['npm', 'init', '-y'])
    subprocess.run(['npm', 'install', '-D', 'tailwindcss'])
    subprocess.run(['npx', 'tailwindcss', 'init'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    display_typing_message("Creating Tailwind CSS configuration...")
    with open('tailwind.config.js', 'w') as config_file:
        config_file.write('module.exports = {\n  extend: {}\n};\n')

    display_typing_message("Creating input.css...")
    create_file('input.css', '@tailwind base;\n@tailwind components;\n@tailwind utilities;')

    display_typing_message("Creating index.html...")
    create_file('index.html', '''<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="/style.css" rel="stylesheet">
</head>
<body>
  <h1 class="text-3xl font-bold underline">
    Hello, {}!
  </h1>
</body>
</html>
'''.format(project_name))

    display_typing_message("Building Tailwind CSS...")
    subprocess.run(['npx', 'tailwindcss', '-i', './input.css', '-o', './style.css', '--watch'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    display_typing_message("Your project is set up. Happy coding!")

if __name__ == "__main__":
    # Display your fancy name with typing effect
    YOUR_FANCY_NAME = """  __  __            _       ____            _             _             
 |  \/  |          | |     |  _ \          | |           (_)            
 | \  / | ___  __ _| |__   | |_) | __ _  __| | ___  _ __  _ _   _  __ _ 
 | |\/| |/ _ \/ _` | '_ \  |  _ < / _` |/ _` |/ _ \| '_ \| | | | |/ _` |
 | |  | |  __/ (_| | | | | | |_) | (_| | (_| | (_) | | | | | |_| | (_| |
 |_|  |_|\___|\__, |_| |_| |____/ \__,_|\__,_|\___/|_| |_|_|\__, |\__,_|
               __/ |                                         __/ |      
              |___/                                         |___/       """
    display_typing_message(YOUR_FANCY_NAME)

    # Ask for project name
    display_typing_message("What is the name of your project?")
    PROJECT_NAME = input().strip()

    # Ask for the project path or use the current directory
    display_typing_message("Where do you want to create the project? (Press Enter for current directory)")
    PROJECT_PATH = input().strip()
    if not PROJECT_PATH:
        PROJECT_PATH = os.getcwd()

    # Check that npm and node are installed
    check_command("npm")
    check_command("node")

    # Create the project
    create_project(PROJECT_NAME, PROJECT_PATH)
