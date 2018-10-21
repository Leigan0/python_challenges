import unittest
import sys
import unittest.mock
from io import StringIO
from current_directory import CurrentDirPrinter

class CurrentDirTest(unittest.TestCase):
        @unittest.mock.patch('os.getcwd', return_value='/home/leigh-ann')
        def test_can_print_dir(self, mock_os):
            out = StringIO()
            sys.stdout = out
            CurrentDirPrinter.printDir()
            output = out.getvalue().strip()
            self.assertEqual(output,"/home/leigh-ann")

        @unittest.mock.patch('os.getcwd')
        def test_os_getcwd_is_called(self, mock_os):
            CurrentDirPrinter.printDir()
            self.assertTrue(mock_os.called)
