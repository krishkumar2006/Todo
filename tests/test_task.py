"""
Unit tests for the Task model.

This module contains unit tests for the Task class to ensure it functions
correctly according to the specifications.
"""

import unittest
from src.models.task import Task


class TestTask(unittest.TestCase):
    """
    Test cases for the Task class.
    """

    def test_task_creation_valid(self):
        """
        Test creating a task with valid parameters.
        """
        task = Task(1, "Test Task", "Test Description", False)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.completed, False)

    def test_task_creation_defaults(self):
        """
        Test creating a task with default values.
        """
        task = Task(1, "Test Task")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertIsNone(task.description)
        self.assertEqual(task.completed, False)

    def test_task_creation_completed(self):
        """
        Test creating a task with completed status.
        """
        task = Task(1, "Test Task", "Test Description", True)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.completed, True)

    def test_task_id_validation(self):
        """
        Test that task ID must be a positive integer.
        """
        with self.assertRaises(ValueError):
            Task(0, "Test Task")
        
        with self.assertRaises(ValueError):
            Task(-1, "Test Task")

    def test_task_title_validation(self):
        """
        Test that task title must be a non-empty string.
        """
        with self.assertRaises(ValueError):
            Task(1, "")
        
        with self.assertRaises(ValueError):
            Task(1, "   ")
        
        with self.assertRaises(ValueError):
            Task(1, 123)

    def test_task_description_validation(self):
        """
        Test that task description must be a string or None.
        """
        # Valid case - None description
        task = Task(1, "Test Task", None)
        self.assertIsNone(task.description)
        
        # Valid case - string description
        task = Task(1, "Test Task", "Valid Description")
        self.assertEqual(task.description, "Valid Description")
        
        # Invalid case - non-string, non-None description
        with self.assertRaises(ValueError):
            Task(1, "Test Task", 123)

    def test_task_completed_validation(self):
        """
        Test that task completed status must be a boolean.
        """
        with self.assertRaises(ValueError):
            Task(1, "Test Task", "Description", "True")
        
        with self.assertRaises(ValueError):
            Task(1, "Test Task", "Description", 1)

    def test_task_title_setter(self):
        """
        Test setting the task title.
        """
        task = Task(1, "Test Task")
        task.title = "New Title"
        self.assertEqual(task.title, "New Title")

    def test_task_title_setter_validation(self):
        """
        Test that setting task title validates the input.
        """
        task = Task(1, "Test Task")
        
        with self.assertRaises(ValueError):
            task.title = ""
        
        with self.assertRaises(ValueError):
            task.title = "   "

    def test_task_description_setter(self):
        """
        Test setting the task description.
        """
        task = Task(1, "Test Task")
        task.description = "New Description"
        self.assertEqual(task.description, "New Description")
        
        task.description = None
        self.assertIsNone(task.description)

    def test_task_description_setter_validation(self):
        """
        Test that setting task description validates the input.
        """
        task = Task(1, "Test Task")
        
        with self.assertRaises(ValueError):
            task.description = 123

    def test_task_completed_setter(self):
        """
        Test setting the task completed status.
        """
        task = Task(1, "Test Task")
        task.completed = True
        self.assertTrue(task.completed)
        
        task.completed = False
        self.assertFalse(task.completed)

    def test_task_completed_setter_validation(self):
        """
        Test that setting task completed status validates the input.
        """
        task = Task(1, "Test Task")
        
        with self.assertRaises(ValueError):
            task.completed = "True"
        
        with self.assertRaises(ValueError):
            task.completed = 1

    def test_task_str_representation(self):
        """
        Test the string representation of a task.
        """
        task = Task(1, "Test Task", "Test Description", False)
        expected = "[ ] 1. Test Task - Test Description"
        self.assertEqual(str(task), expected)
        
        task = Task(2, "Completed Task", completed=True)
        expected = "[x] 2. Completed Task"
        self.assertEqual(str(task), expected)

    def test_task_to_dict(self):
        """
        Test converting a task to a dictionary.
        """
        task = Task(1, "Test Task", "Test Description", True)
        expected_dict = {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "completed": True
        }
        self.assertEqual(task.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()