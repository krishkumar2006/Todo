"""
Unit tests for viewing tasks functionality in TaskService.

This module contains unit tests for the viewing tasks functionality in the TaskService.
"""

import unittest
from src.services.task_service import TaskService


class TestViewTasks(unittest.TestCase):
    """
    Test cases for viewing tasks functionality.
    """

    def setUp(self):
        """
        Set up a fresh TaskService instance for each test.
        """
        self.service = TaskService()

    def test_get_all_tasks_empty(self):
        """
        Test getting all tasks when there are no tasks.
        """
        tasks = self.service.get_all_tasks()
        self.assertEqual(len(tasks), 0)
        self.assertIsInstance(tasks, list)

    def test_get_all_tasks_single_task(self):
        """
        Test getting all tasks when there is one task.
        """
        task = self.service.add_task("Test Task", "Test Description")
        tasks = self.service.get_all_tasks()
        
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, task.id)
        self.assertEqual(tasks[0].title, task.title)
        self.assertEqual(tasks[0].description, task.description)
        self.assertEqual(tasks[0].completed, task.completed)

    def test_get_all_tasks_multiple_tasks(self):
        """
        Test getting all tasks when there are multiple tasks.
        """
        task1 = self.service.add_task("Task 1", "Description 1")
        task2 = self.service.add_task("Task 2", "Description 2")
        task3 = self.service.add_task("Task 3", "Description 3")
        
        tasks = self.service.get_all_tasks()
        
        self.assertEqual(len(tasks), 3)
        self.assertEqual(tasks[0].id, task1.id)
        self.assertEqual(tasks[1].id, task2.id)
        self.assertEqual(tasks[2].id, task3.id)

    def test_get_all_tasks_after_deletion(self):
        """
        Test getting all tasks after one has been deleted.
        """
        task1 = self.service.add_task("Task 1", "Description 1")
        task2 = self.service.add_task("Task 2", "Description 2")
        
        # Delete the first task
        self.service.delete_task(task1.id)
        
        tasks = self.service.get_all_tasks()
        
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, task2.id)

    def test_get_all_tasks_returns_copy(self):
        """
        Test that get_all_tasks returns a copy of the internal list.
        """
        task1 = self.service.add_task("Task 1", "Description 1")
        task2 = self.service.add_task("Task 2", "Description 2")
        
        tasks = self.service.get_all_tasks()
        
        # Modify the returned list
        tasks.clear()
        
        # Internal list should remain unchanged
        internal_tasks = self.service.get_all_tasks()
        self.assertEqual(len(internal_tasks), 2)
        self.assertEqual(internal_tasks[0].id, task1.id)
        self.assertEqual(internal_tasks[1].id, task2.id)


if __name__ == "__main__":
    unittest.main()