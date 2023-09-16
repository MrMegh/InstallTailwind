#!/bin/bash

# Function to display a message with a typing effect and color
display_typing_message() {
  local message="$1"
  local color="$2"
  for ((i=0; i<${#message}; i++)); do
    echo -n "${color}${message:$i:1}"
    sleep 0.03  # Adjust the sleep duration for the typing speed
  done
  echo
}

# Function to check if a command is installed
check_command() {
  if ! command -v $1 > /dev/null 2>&1; then
    display_typing_message "$1 is not installed. Please install $1 before running this script." "$RED"
    exit 1
  fi
}

# Function to create a file with content
create_file() {
  echo "$2" > "$1"
}

# Function to create project structure
create_project() {
  display_typing_message "Creating your project folder..." "$GREEN"
  mkdir "$1"
  cd "$1"

  display_typing_message "Initializing npm and setting up Tailwind CSS..." "$GREEN"
  npm init -y
  npm install -D tailwindcss
  npx tailwindcss init > /dev/null 2>&1

  display_typing_message "Creating Tailwind CSS configuration..." "$GREEN"
  sed -i 's/extend: {}/extend: \{\}/g' tailwind.config.js

  display_typing_message "Creating input.css..." "$GREEN"
  create_file "input.css" "@tailwind base;\n@tailwind components;\n@tailwind utilities;"

  display_typing_message "Creating index.html..." "$GREEN"
  create_file "index.html" "<!doctype html>\n<html>\n<head>\n  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <link href=\"/style.css\" rel=\"stylesheet\">\n</head>\n<body>\n  <h1 class=\"text-3xl font-bold underline\">\n    Hello, $1!\n  </h1>\n</body>\n</html>"

  display_typing_message "Building Tailwind CSS..." "$GREEN"
  npx tailwindcss -i ./input.css -o ./style.css --watch > /dev/null 2>&1

  display_typing_message "Your project is set up. Happy coding!" "$GREEN"
}

# Define ANSI color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
RESET='\033[0m' # Reset color

# Main script starts here

# Display your fancy name with typing effect
YOUR_FANCY_NAME="MEGH BADONIYA"  # Replace with your name
display_typing_message "Hello, $YOUR_FANCY_NAME!" "$CYAN"

# Ask for project name
display_typing_message "What is the name of your project?" "$CYAN"
read -p "" PROJECT_NAME

# Check that npm and node are installed
check_command "npm"
check_command "node"

# Create the project
create_project "$PROJECT_NAME"
