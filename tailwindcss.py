import os
import subprocess

# Function to display a message with a typing effect
def display_typing_message(message):
    for char in message:
        print(char, end='', flush=True)
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
def create_project(project_name):
    display_typing_message("Creating your project folder...")
    os.makedirs(project_name)
    os.chdir(project_name)

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
    YOUR_FANCY_NAME = "YOUR_NAME_IN_BIG_LETTERS"  # Replace with your name
    display_typing_message(f"Hello, {YOUR_FANCY_NAME}!")

    # Ask for project name
    display_typing_message("What is the name of your project?")
    PROJECT_NAME = input().strip()

    # Check that npm and node are installed
    check_command("npm")
    check_command("node")

    # Create the project
    create_project(PROJECT_NAME)
