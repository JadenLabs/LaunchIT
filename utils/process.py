import os

class Process:
    def __init__(self, name: str, directory_path: str, start_cmd: str, auto_start: bool = True) -> None:
        self.name = name
        self.directory_path = directory_path
        self.start_cmd = start_cmd
        
        if auto_start:
            self.start()

    def start(self):
        command = f"start cmd.exe /K {self.start_cmd}"
        os.chdir(self.directory_path)
        self.process = os.system(command)

