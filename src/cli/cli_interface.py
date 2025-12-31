"""
CLI interface for the Todo application.

This module contains the TodoCLI class which provides a menu-based interface
for users to interact with the task management system.
"""

from typing import Optional
from src.services.task_service import TaskService


class TodoCLI:
    """
    Command-line interface for the Todo application.
    """

    def __init__(self, task_service: TaskService):
        """
        Initialize the CLI with a task service.

        Args:
            task_service (TaskService): The service to handle task operations
        """
        self.task_service = task_service

    def display_menu(self) -> None:
        """
        Display the main menu options to the user.
        """
        print("\n--- Todo Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete")
        print("6. Mark Task Incomplete")
        print("7. Exit")
        print("------------------------")

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            str: The user's menu choice
        """
        return input("Enter your choice (1-7): ").strip()

    def add_task(self) -> None:
        """
        Handle the add task functionality.
        """
        try:
            title = input("Enter task title: ").strip()
            
            if not title:
                print("Error: Task title cannot be empty.")
                return

            description_input = input("Enter task description (optional, press Enter to skip): ").strip()
            description = description_input if description_input else None

            task = self.task_service.add_task(title, description)
            print(f"Task '{task.title}' added successfully with ID {task.id}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_tasks(self) -> None:
        """
        Handle the view tasks functionality.
        """
        tasks = self.task_service.get_all_tasks()
        
        if not tasks:
            print("No tasks found.")
            return

        print("\n--- Task List ---")
        for task in tasks:
            status = "[x]" if task.completed else "[ ]"
            desc = f" - {task.description}" if task.description else ""
            print(f"{status} {task.id}. {task.title}{desc}")
        print("-----------------")

    def update_task(self) -> None:
        """
        Handle the update task functionality.
        """
        try:
            task_id_input = input("Enter task ID to update: ").strip()
            
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_input)
            
            # Check if task exists
            task = self.task_service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            print(f"Current task: {task}")
            
            new_title_input = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
            new_desc_input = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()
            
            # Use current values if no new values provided
            new_title = new_title_input if new_title_input else None
            new_description = new_desc_input if new_desc_input != "" else None
            
            updated_task = self.task_service.update_task(task_id, new_title, new_description)
            
            if updated_task:
                print(f"Task with ID {task_id} updated successfully.")
            else:
                print(f"Error: Failed to update task with ID {task_id}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_task(self) -> None:
        """
        Handle the delete task functionality.
        """
        try:
            task_id_input = input("Enter task ID to delete: ").strip()
            
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_input)
            
            # Check if task exists before asking for confirmation
            task = self.task_service.get_task_by_id(task_id)
            if not task:
                print(f"Error: Task with ID {task_id} not found.")
                return

            confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/N): ").strip().lower()
            
            if confirm in ['y', 'yes']:
                success = self.task_service.delete_task(task_id)
                
                if success:
                    print(f"Task with ID {task_id} deleted successfully.")
                else:
                    print(f"Error: Failed to delete task with ID {task_id}.")
            else:
                print("Deletion canceled.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def mark_task_complete(self) -> None:
        """
        Handle the mark task complete functionality.
        """
        try:
            task_id_input = input("Enter task ID to mark complete: ").strip()
            
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_input)
            
            task = self.task_service.mark_task_complete(task_id)
            
            if task:
                print(f"Task with ID {task_id} marked as complete.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def mark_task_incomplete(self) -> None:
        """
        Handle the mark task incomplete functionality.
        """
        try:
            task_id_input = input("Enter task ID to mark incomplete: ").strip()
            
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_input)
            
            task = self.task_service.mark_task_incomplete(task_id)
            
            if task:
                print(f"Task with ID {task_id} marked as incomplete.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def run(self) -> None:
        """
        Run the main CLI loop.
        """
        print("Welcome to the Todo CLI Application!")
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.mark_task_complete()
            elif choice == '6':
                self.mark_task_incomplete()
            elif choice == '7':
                print("Thank you for using the Todo CLI Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")