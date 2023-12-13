# rm_command.py
class RmCommand:
    @staticmethod
    def execute(fs, path):
        parts = path.split('/')
        current = fs.root
        for part in parts[:-1]:
            if part not in current.children:
                print(f"Path '{path}' not found.")
                return
            current = current.children[part]
        if path in current.children:
            del current.children[path]
            print(f"Path '{path}' removed successfully.")
        else:
            print(f"Path '{path}' not found ")
