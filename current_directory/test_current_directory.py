import unittest
import sys
import unittest.mock
from io import StringIO
from current_directory import CurrentDirPrinter

class CurrentDirTest(unittest.TestCase):
        @unittest.mock.patch('os.getcwd', return_value='/home/leigh-ann')
        def test_can_print_dir(self, mock_os):
            cwdPrinter = CurrentDirPrinter()
            out = StringIO()
            sys.stdout = out
            cwdPrinter.printDir()
            output = out.getvalue().strip()
            self.assertEqual(output,"/home/leigh-ann")