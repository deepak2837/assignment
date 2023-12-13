# touch_command.py
from node import Node

class TouchCommand:
    @staticmethod
    def execute(fs, path):
        parts = path.split('/')
        current = fs.current_dir
        for part in parts[:-1]:
            if part not in current.children:
                current.children[part] = Node(part)
            current = current.children[part]
        current.children[parts[-1]] = Node(parts[-1], True)
        print(f"File '{path}' created successfully.")
