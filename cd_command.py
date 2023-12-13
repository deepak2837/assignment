# cd_command.py
class CdCommand:
    @staticmethod
    def execute(fs, path):
        if path == '..':
            if fs.current_dir.name != '/':
                fs.current_dir = fs.current_dir.parent
            else:
                print("Already at root directory.")
        elif path == '/':
            fs.current_dir = fs.root
        elif path.startswith('/'):
            parts = path[1:].split('/')
            current = fs.root
            for part in parts:
                if part not in current.children:
                    print(f"Directory '{path}' not found.")
                    return
                current = current.children[part]
            fs.current_dir = current
        else:
            if path not in fs.current_dir.children:
                print(f"Directory '{path}' not found in the current directory.")
            else:
                fs.current_dir = fs.current_dir.children[path]
