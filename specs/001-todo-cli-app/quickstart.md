# Quickstart Guide: Todo CLI Application

## Setup

1. Ensure you have Python 3.13+ installed on your system
2. Install UV package manager if not already installed:
   ```bash
   pip install uv
   ```
3. Clone or download the project repository
4. Navigate to the project root directory

## Installation

1. Create a virtual environment using UV:
   ```bash
   uv venv
   ```
2. Activate the virtual environment:
   ```bash
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```
3. The application uses only Python standard library, so no additional dependencies need to be installed.

## Running the Application

1. Navigate to the project root directory
2. Run the application:
   ```bash
   python src/main.py
   ```
3. The menu interface will appear, allowing you to perform the following operations:
   - 1. Add Task
   - 2. View Tasks
   - 3. Update Task
   - 4. Delete Task
   - 5. Mark Task Complete
   - 6. Mark Task Incomplete
   - 7. Exit

## Basic Usage

### Adding a Task
1. Select option 1 "Add Task" from the menu
2. Enter the task title when prompted
3. Optionally enter a task description when prompted
4. The task will be added with a unique ID and incomplete status

### Viewing Tasks
1. Select option 2 "View Tasks" from the menu
2. All tasks will be displayed with their ID, status indicator ([ ] or [x]), title, and truncated description

### Updating a Task
1. Select option 3 "Update Task" from the menu
2. Enter the task ID when prompted
3. Enter the new title and/or description when prompted
4. The task will be updated with the new information

### Deleting a Task
1. Select option 4 "Delete Task" from the menu
2. Enter the task ID when prompted
3. Confirm the deletion if prompted
4. The task will be removed from the list

### Marking a Task Complete/Incomplete
1. Select option 5 "Mark Task Complete" or option 6 "Mark Task Incomplete" from the menu
2. Enter the task ID when prompted
3. The task status will be updated accordingly

## Error Handling

- If you enter an invalid command, the application will display an error message and show the available options
- If you enter an invalid task ID, the application will display an error message indicating that the task was not found
- If you try to add a task with an empty title, the application will display an error message requiring a title