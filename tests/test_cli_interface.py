"""
Unit tests for the CLI interface.

This module contains unit tests for the TodoCLI class to ensure it functions
correctly according to the specifications.
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from src.services.task_service import TaskService
from src.cli.cli_interface import TodoCLI


class TestCLIInterface(unittest.TestCase):
    """
    Test cases for the TodoCLI class.
    """

    def setUp(self):
        """
        Set up a fresh TodoCLI instance for each test.
        """
        self.task_service = TaskService()
        self.cli = TodoCLI(self.task_service)

    def test_add_task(self):
        """
        Test the add task functionality.
        """
        with patch('builtins.input', side_effect=['Test Task', 'Test Description']):
            with patch('builtins.print') as mock_print:
                self.cli.add_task()
        
        # Verify the task was added
        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test Task")
        self.assertEqual(tasks[0].description, "Test Description")
        self.assertEqual(tasks[0].completed, False)

    def test_add_task_without_description(self):
        """
        Test the add task functionality without description.
        """
        with patch('builtins.input', side_effect=['Test Task', '']):
            with patch('builtins.print') as mock_print:
                self.cli.add_task()
        
        # Verify the task was added
        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].title, "Test Task")
        self.assertIsNone(tasks[0].description)

    def test_add_task_empty_title(self):
        """
        Test the add task functionality with empty title.
        """
        with patch('builtins.input', side_effect=['', 'Test Description']):
            with patch('builtins.print') as mock_print:
                self.cli.add_task()
        
        # Verify the task was not added
        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 0)
        
        # Verify error message was printed
        mock_print.assert_called_with("Error: Task title cannot be empty.")

    def test_view_tasks_empty(self):
        """
        Test the view tasks functionality when no tasks exist.
        """
        with patch('builtins.print') as mock_print:
            self.cli.view_tasks()
        
        # Verify appropriate message was printed
        mock_print.assert_called_with("No tasks found.")

    def test_view_tasks_with_tasks(self):
        """
        Test the view tasks functionality with existing tasks.
        """
        # Add some tasks
        self.task_service.add_task("Task 1", "Description 1")
        task2 = self.task_service.add_task("Task 2", "Description 2")
        # Mark the second task as complete
        self.task_service.mark_task_complete(task2.id)

        with patch('builtins.print') as mock_print:
            self.cli.view_tasks()

        # Verify the method was called with appropriate content
        self.assertTrue(any("Task 1" in str(call) for call in mock_print.call_args_list))
        self.assertTrue(any("Task 2" in str(call) for call in mock_print.call_args_list))

    def test_update_task(self):
        """
        Test the update task functionality.
        """
        # Add a task first
        task = self.task_service.add_task("Original Task", "Original Description")
        
        with patch('builtins.input', side_effect=[str(task.id), "Updated Task", "Updated Description"]):
            with patch('builtins.print') as mock_print:
                self.cli.update_task()
        
        # Verify the task was updated
        updated_task = self.task_service.get_task_by_id(task.id)
        self.assertEqual(updated_task.title, "Updated Task")
        self.assertEqual(updated_task.description, "Updated Description")

    def test_update_task_not_found(self):
        """
        Test the update task functionality with non-existent task ID.
        """
        with patch('builtins.input', side_effect=['999', "Updated Task", "Updated Description"]):
            with patch('builtins.print') as mock_print:
                self.cli.update_task()
        
        # Verify error message was printed
        mock_print.assert_called_with("Error: Task with ID 999 not found.")

    def test_delete_task(self):
        """
        Test the delete task functionality.
        """
        # Add a task first
        task = self.task_service.add_task("Task to Delete", "Description")
        
        with patch('builtins.input', side_effect=[str(task.id), 'y']):
            with patch('builtins.print') as mock_print:
                self.cli.delete_task()
        
        # Verify the task was deleted
        remaining_tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(remaining_tasks), 0)

    def test_delete_task_cancelled(self):
        """
        Test the delete task functionality when deletion is cancelled.
        """
        # Add a task first
        task = self.task_service.add_task("Task to Delete", "Description")
        
        with patch('builtins.input', side_effect=[str(task.id), 'n']):
            with patch('builtins.print') as mock_print:
                self.cli.delete_task()
        
        # Verify the task was not deleted
        remaining_tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(remaining_tasks), 1)

    def test_delete_task_not_found(self):
        """
        Test the delete task functionality with non-existent task ID.
        """
        with patch('builtins.input', side_effect=['999', 'y']):
            with patch('builtins.print') as mock_print:
                self.cli.delete_task()
        
        # Verify error message was printed
        mock_print.assert_called_with("Error: Task with ID 999 not found.")

    def test_mark_task_complete(self):
        """
        Test the mark task complete functionality.
        """
        # Add a task first
        task = self.task_service.add_task("Test Task", "Description")
        self.assertFalse(task.completed)
        
        with patch('builtins.input', side_effect=[str(task.id)]):
            with patch('builtins.print') as mock_print:
                self.cli.mark_task_complete()
        
        # Verify the task was marked complete
        updated_task = self.task_service.get_task_by_id(task.id)
        self.assertTrue(updated_task.completed)

    def test_mark_task_complete_not_found(self):
        """
        Test the mark task complete functionality with non-existent task ID.
        """
        with patch('builtins.input', side_effect=['999']):
            with patch('builtins.print') as mock_print:
                self.cli.mark_task_complete()
        
        # Verify error message was printed
        mock_print.assert_called_with("Error: Task with ID 999 not found.")

    def test_mark_task_incomplete(self):
        """
        Test the mark task incomplete functionality.
        """
        # Add a task first and mark it complete
        task = self.task_service.add_task("Test Task", "Description")
        self.task_service.mark_task_complete(task.id)
        self.assertTrue(task.completed)
        
        with patch('builtins.input', side_effect=[str(task.id)]):
            with patch('builtins.print') as mock_print:
                self.cli.mark_task_incomplete()
        
        # Verify the task was marked incomplete
        updated_task = self.task_service.get_task_by_id(task.id)
        self.assertFalse(updated_task.completed)

    def test_mark_task_incomplete_not_found(self):
        """
        Test the mark task incomplete functionality with non-existent task ID.
        """
        with patch('builtins.input', side_effect=['999']):
            with patch('builtins.print') as mock_print:
                self.cli.mark_task_incomplete()
        
        # Verify error message was printed
        mock_print.assert_called_with("Error: Task with ID 999 not found.")


if __name__ == "__main__":
    unittest.main()