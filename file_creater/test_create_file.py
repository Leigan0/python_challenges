import unittest
from create_file import CreateFile

class CreateFileTest(unittest.TestCase):
    def setUp(self):
        file_path = '/Users/leighann.gant/Projects/code_challenge'
        file_name = 'fun_test.txt'
        self.createFile = CreateFile(file_path, file_name)

    def test_it_has_directory_path_and_file_name(self):
        self.assertEqual(self.createFile.file_path, "/Users/leighann.gant/Projects/code_challenge")
        self.assertEqual(self.createFile.file_name, 'fun_test.txt')
