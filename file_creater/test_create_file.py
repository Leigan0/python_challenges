import unittest
import unittest.mock
from create_file import CreateFile

class CreateFileTest(unittest.TestCase):
    def setUp(self):
        file_path = '/Users/leighann.gant/Projects/code_challenge'
        file_name = 'fun_test.txt'
        self.createFile = CreateFile(file_path, file_name)
    
    def test_it_has_directory_path_and_file_name(self):
        self.assertEqual(self.createFile.file_path, "/Users/leighann.gant/Projects/code_challenge")
        self.assertEqual(self.createFile.file_name, 'fun_test.txt')

    @unittest.mock.patch('os.path.exists')
    def test_it_checks_if_path_exists(self, mock_os):
        self.createFile.create_file()
        self.assertTrue(mock_os.called)

    @unittest.mock.patch('os.makedirs')
    @unittest.mock.patch('os.path.exists', return_value = False)
    def test_if_path_does_not_exist_dir_created(self, mock_os, mock_create_dir):
        self.createFile.create_file()
        self.assertTrue(mock_create_dir.called)
    
    @unittest.mock.patch('os.makedirs')
    @unittest.mock.patch('os.path.exists', return_value = True)
    def test_if_path_does_exist_dir_not_created(self, mock_os, mock_create_dir):
        self.createFile.create_file()
        self.assertFalse(mock_create_dir.called)
    
    @unittest.mock.patch('os.path.exists', return_value = False)
    @unittest.mock.patch('open')
    def test_if_path_does_exist_new_file_created(self, mock_os, mock_open):
        self.createFile.create_file()
        self.assertTrue(mock_open.called)

