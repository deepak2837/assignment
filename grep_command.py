# grep_command.py
class GrepCommand:
    @staticmethod
    def execute(fs, pattern, path='/'):
        target_file = fs._get_node(path)

        if not target_file.is_file or not target_file.content:
            print(f"Error: '{path}' is not a file or has no content.")
        elif pattern in target_file.content:
            print(f"Found '{pattern}' in '{target_file.name}'")
        else:
            print(f"Pattern '{pattern}' not found in '{target_file.name}'")
