# ls_command.py
class LsCommand:
    @staticmethod
    def execute(fs, path='/'):
        if path == '/':
            current = fs.root
        else:
            parts = path.split('/')
            current = fs.root
            for part in parts[:-1]:
                if part not in current.children:
                    print(f"Directory '{path}' not found.")
                    return
                current = current.children[part]
        if current.is_file:
            print(current.name)
        else:
            for child in current.children:
                print(child)
