# cat_command.py
class CatCommand:
    @staticmethod
    def execute(fs, path):
        parts = path.split('/')
        current = fs.root
        for part in parts[:-1]:
            if part not in current.children:
                print(f"File '{path}' not found.")
                return
            current = current.children[part]
        print(current.content)
