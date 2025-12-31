"""
Task model representing a single todo item.

This module contains the Task class which represents a single todo item
with an ID, title, description, and completion status.
"""

from typing import Optional


class Task:
    """
    Represents a single todo item with the following attributes:
    - ID: Unique auto-incrementing identifier (starting from 1)
    - Title: String representing the task name (required)
    - Description: String providing additional details (optional)
    - Completed: Boolean indicating completion status (default: false)
    """

    def __init__(self, task_id: int, title: str, description: Optional[str] = None, completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            title (str): Task title (required, non-empty)
            description (Optional[str]): Task description (optional)
            completed (bool): Completion status (default: False)
        """
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title must be a non-empty string")
        
        if description is not None and not isinstance(description, str):
            raise ValueError("Task description must be a string or None")
        
        if not isinstance(completed, bool):
            raise ValueError("Task completion status must be a boolean")
        
        self._id = task_id
        self._title = title.strip()
        self._description = description
        self._completed = completed

    @property
    def id(self) -> int:
        """Get the task ID."""
        return self._id

    @property
    def title(self) -> str:
        """Get the task title."""
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        """Set the task title."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Task title must be a non-empty string")
        self._title = value.strip()

    @property
    def description(self) -> Optional[str]:
        """Get the task description."""
        return self._description

    @description.setter
    def description(self, value: Optional[str]) -> None:
        """Set the task description."""
        if value is not None and not isinstance(value, str):
            raise ValueError("Task description must be a string or None")
        self._description = value

    @property
    def completed(self) -> bool:
        """Get the task completion status."""
        return self._completed

    @completed.setter
    def completed(self, value: bool) -> None:
        """Set the task completion status."""
        if not isinstance(value, bool):
            raise ValueError("Task completion status must be a boolean")
        self._completed = value

    def __str__(self) -> str:
        """Return a string representation of the task."""
        status = "[x]" if self.completed else "[ ]"
        desc = f" - {self.description}" if self.description else ""
        return f"{status} {self.id}. {self.title}{desc}"

    def to_dict(self) -> dict:
        """
        Convert the task to a dictionary representation.

        Returns:
            dict: Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }