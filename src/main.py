"""
Main entry point for the Todo CLI Application.

This module initializes the application components and starts the CLI interface.
"""

from src.services.task_service import TaskService
from src.cli.cli_interface import TodoCLI


def main() -> None:
    """
    Main function to run the Todo CLI Application.
    """
    # Initialize the task service
    task_service = TaskService()
    
    # Initialize the CLI interface with the task service
    cli = TodoCLI(task_service)
    
    # Run the CLI interface
    cli.run()


if __name__ == "__main__":
    main()