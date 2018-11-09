import os 

class CreateFile():
    def __init__(self, file_path, file_name):
        self.file_path = file_path
        self.file_name = file_name
    
    def create_file(self):
        if os.path.exists(self.file_path): 
            open(self.file_path + "/" + self.file_name, "wb")
        else: 
            os.makedirs(self.file_path)