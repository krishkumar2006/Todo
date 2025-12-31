"""
Task service for managing todo tasks.

This module contains the TaskService class which handles all business logic
for task operations including adding, updating, deleting, and viewing tasks.
The implementation uses in-memory storage only as specified in the requirements.
"""

from typing import List, Optional
from src.models.task import Task


class TaskService:
    """
    Service class for handling task operations with in-memory storage.
    """

    def __init__(self):
        """
        Initialize the TaskService with an empty list of tasks and ID counter.
        """
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task with a unique auto-incrementing ID.

        Args:
            title (str): Task title (required, non-empty)
            description (Optional[str]): Task description (optional)

        Returns:
            Task: The newly created Task object

        Raises:
            ValueError: If title is empty or invalid
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title must be a non-empty string")

        # Create a new task with the next available ID
        task = Task(self._next_id, title, description, completed=False)
        self._tasks.append(task)
        
        # Increment the ID counter for the next task
        self._next_id += 1
        
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks.

        Returns:
            List[Task]: List of all tasks
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, new_title: Optional[str] = None, 
                    new_description: Optional[str] = None) -> Optional[Task]:
        """
        Update an existing task's title and/or description.

        Args:
            task_id (int): The ID of the task to update
            new_title (Optional[str]): New title (if provided)
            new_description (Optional[str]): New description (if provided)

        Returns:
            Optional[Task]: The updated task if found, None otherwise

        Raises:
            ValueError: If new_title is empty
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if new_title is not None and (not isinstance(new_title, str) or not new_title.strip()):
            raise ValueError("Task title must be a non-empty string if provided")

        task = self.get_task_by_id(task_id)
        if task:
            if new_title is not None:
                task.title = new_title
            if new_description is not None:
                task.description = new_description
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if not found
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self.get_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False

    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as complete.

        Args:
            task_id (int): The ID of the task to mark complete

        Returns:
            Optional[Task]: The updated task if found, None otherwise
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            return task
        return None

    def mark_task_incomplete(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as incomplete.

        Args:
            task_id (int): The ID of the task to mark incomplete

        Returns:
            Optional[Task]: The updated task if found, None otherwise
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")

        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return task
        return None

    def get_next_id(self) -> int:
        """
        Get the next available task ID.

        Returns:
            int: The next available task ID
        """
        return self._next_id