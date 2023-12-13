# echo_command.py
from node import Node

class EchoCommand:
    @staticmethod
    def execute(fs, content, path):
        parts = path.split('/')
        current = fs.root
        for part in parts[:-1]:
            if part not in current.children:
                current.children[part] = Node(part)
            current = current.children[part]
        current.children[parts[-1]] = Node(parts[-1], True, content)
        print(f"Content written to '{path}'.")
