# Python Assignments Repository

## Overview
This repository contains three Python scripts that solve practical programming and DevOps-related tasks. Each script is designed to demonstrate essential concepts, from password validation to system monitoring and file backup.

---

## Table of Contents
1. [Assignment 1: Password Strength Checker](#assignment-1-password-strength-checker)
2. [Assignment 2: CPU Health Monitor](#assignment-2-cpu-health-monitor)
3. [Assignment 3: Directory Backup](#assignment-3-directory-backup)
4. [How to Use](#how-to-use)
5. [Contributing](#contributing)
6. [License](#license)

---

## Assignment 1: Password Strength Checker

### Description
This script implements a Python function `check_password_strength` that evaluates the strength of a password based on the following criteria:
- **Minimum length**: At least 8 characters.
- **Character types**: Includes uppercase, lowercase, numbers, and special characters.

The script prompts the user for a password, validates its strength, and provides feedback.

### How to Run
1. Navigate to the script's directory.
2. Run the script using Python:
   ```bash
   python password_checker.py
Follow the prompt to input a password and receive feedback on its strength.

## Assignment 2: CPU Health Monitor

### Description
This script continuously monitors the CPU usage of the local machine and raises an alert if the usage exceeds a predefined threshold (e.g., 80%). It runs indefinitely until interrupted and includes robust error handling.

### Features
- Continuously monitors CPU usage using the `psutil` library.
- Displays an alert message when CPU usage exceeds a specified threshold.
- Includes error handling to manage exceptions that may occur.

### Prerequisites
- Python 3.x installed on your system.
- The `psutil` library. Install it using:
   ```bash
   pip install psutil

### How to Run
1. Navigate to the script's directory.
2. Run the script using Python:
   ```bash
   python CPU_monitor.py
Monitor CPU usage in real-time and observe alert messages when thresholds are exceeded.


## Assignment 3: Directory Backup

### Description
This script, `backup.py`, automates the process of backing up files from a source directory to a destination directory. It ensures that file names in the destination directory remain unique by appending timestamps to duplicates.

### Features
- Copies all files from the source directory to the destination directory.
- Appends a timestamp to the file name in case of duplicates to ensure uniqueness.
- Handles errors such as missing directories or permission issues gracefully.

### How to Run
1. Navigate to the script's directory.
2. Run the script with the source and destination directory paths as arguments:
   ```bash
   python backup.py /path/to/source /path/to/destination

  Replace /path/to/source with your source directory path and /path/to/destination with your destination directory path.
   Example
    ```bash
    python backup.py ./source_dir ./backup_dir

  Notes
  Ensure the source and destination directories exist before running the script.
  Backup files will have unique names if a conflict arises.

### How to use
Clone this repository:
  ```bash
  git clone https://github.com/reshmanavale/Assignments.git

Navigate to the repository:
    ```bash
    cd Assignments

Execute the scripts based on the instructions provided for each assignment.
Contributing
Contributions are welcome! If you'd like to enhance or add features:

Fork this repository.
Create a new branch:
    ```bash
    git checkout -b feature-name
Commit and push your changes.
Open a pull request for review.
License
This repository is open for educational and personal use. Feel free to use, modify, and share, but please provide attribution where applicable.


