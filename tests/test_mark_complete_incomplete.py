"""
Unit tests for marking tasks complete/incomplete functionality in TaskService.

This module contains unit tests for the marking tasks complete/incomplete functionality in the TaskService.
"""

import unittest
from src.services.task_service import TaskService


class TestMarkTaskCompleteIncomplete(unittest.TestCase):
    """
    Test cases for marking tasks complete/incomplete functionality.
    """

    def setUp(self):
        """
        Set up a fresh TaskService instance for each test.
        """
        self.service = TaskService()

    def test_mark_task_complete_found(self):
        """
        Test marking a task as complete when it exists.
        """
        task = self.service.add_task("Test Task", "Test Description")
        self.assertFalse(task.completed)
        
        marked_task = self.service.mark_task_complete(task.id)
        self.assertIsNotNone(marked_task)
        self.assertTrue(marked_task.completed)

    def test_mark_task_complete_not_found(self):
        """
        Test marking a task as complete when it doesn't exist.
        """
        result = self.service.mark_task_complete(999)
        self.assertIsNone(result)

    def test_mark_task_complete_id_validation(self):
        """
        Test that marking a task complete validates the task ID.
        """
        with self.assertRaises(ValueError):
            self.service.mark_task_complete(0)
        
        with self.assertRaises(ValueError):
            self.service.mark_task_complete(-1)

    def test_mark_task_incomplete_found(self):
        """
        Test marking a task as incomplete when it exists.
        """
        task = self.service.add_task("Test Task", "Test Description")
        # Mark as complete first
        self.service.mark_task_complete(task.id)
        self.assertTrue(task.completed)
        
        marked_task = self.service.mark_task_incomplete(task.id)
        self.assertIsNotNone(marked_task)
        self.assertFalse(marked_task.completed)

    def test_mark_task_incomplete_not_found(self):
        """
        Test marking a task as incomplete when it doesn't exist.
        """
        result = self.service.mark_task_incomplete(999)
        self.assertIsNone(result)

    def test_mark_task_incomplete_id_validation(self):
        """
        Test that marking a task incomplete validates the task ID.
        """
        with self.assertRaises(ValueError):
            self.service.mark_task_incomplete(0)
        
        with self.assertRaises(ValueError):
            self.service.mark_task_incomplete(-1)

    def test_mark_task_complete_then_incomplete(self):
        """
        Test marking a task complete then incomplete.
        """
        task = self.service.add_task("Test Task", "Test Description")
        self.assertFalse(task.completed)
        
        # Mark complete
        self.service.mark_task_complete(task.id)
        task = self.service.get_task_by_id(task.id)
        self.assertTrue(task.completed)
        
        # Mark incomplete
        self.service.mark_task_incomplete(task.id)
        task = self.service.get_task_by_id(task.id)
        self.assertFalse(task.completed)


if __name__ == "__main__":
    unittest.main()