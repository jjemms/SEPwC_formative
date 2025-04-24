import os
import unittest
from unittest.mock import patch
from todo import add_task, list_tasks, remove_task, TASK_FILE

class TestTodoFunctions(unittest.TestCase):

    def setUp(self):
        """Ensure an empty task file before each test."""
        if os.path.exists(TASK_FILE):
            os.remove(TASK_FILE)

    def tearDown(self):
        """Clean up the task file after each test."""
        if os.path.exists(TASK_FILE):
            os.remove(TASK_FILE)

    def test_add_task(self):
        """Test that a task is added correctly."""
        add_task("First")
        self.assertTrue(os.path.exists(TASK_FILE)) # Check if the file exists

        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()

        self.assertEqual(len(tasks), 1) # This checks that the numbers of tasks added is 1 (as only added one)
        self.assertEqual(tasks[0].strip(), "First") # This checks that the task added is the same as the one that was added

    def test_list_tasks(self):
        """Test printing all the tasks."""
        add_task("First")
        add_task("Second")

        tasks = list_tasks()

        self.assertIn("1. First", tasks) # Check if the first task is in the list
        self.assertIn("2. Second", tasks) # Check if the second task is in the list

    def test_remove_task(self):
        """Test removing a task in the middle of the list."""
        add_task("First")
        add_task("Second")
        add_task("Third")

        remove_task(2) 

        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[1].strip(), "Third") # Check that the second task is now the third task because the middle task was removed

    def test_remove_task_invalid_index(self):
        """Test removing a task with an invalid index."""
        add_task("First")
        with patch("builtins.print") as mock_print:
            remove_task(5)  # Invalid index out of range
            mock_print.assert_called_with("Invalid task number. Please choose between 1 and 1.") 

        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].strip(), "First")

if __name__ == "__main__":
    unittest.main()
