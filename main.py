# main.py
from filesystems import FileSystem
from mkdir_command import MkdirCommand
from cd_command import CdCommand
from ls_command import LsCommand
from grep_command import GrepCommand
from cat_command import CatCommand
from touch_command import TouchCommand
from echo_command import EchoCommand
from mv_command import MvCommand
from cp_command import CpCommand
from rm_command import RmCommand

def main():
    fs = FileSystem()
    while True:
        try:
            command = input('> ').strip()

            # Handle quotes and split arguments
            parts = []
            in_quotes = False
            current_part = ''
            for char in command:
                if char == "'":
                    in_quotes = not in_quotes
                elif char == ' ' and not in_quotes:
                    if current_part:
                        parts.append(current_part)
                        current_part = ''
                    continue
                current_part += char

            if current_part:
                parts.append(current_part)

            if not parts:
                continue

            action = parts[0]
            args = parts[1:]

            # Use a dictionary to map commands to their respective classes
            command_classes = {
                'mkdir': MkdirCommand,
                'cd': CdCommand,
                'ls': LsCommand,
                'grep': GrepCommand,
                'cat': CatCommand,
                'touch': TouchCommand,
                'echo': EchoCommand,
                'mv': MvCommand,
                'cp': CpCommand,
                'rm': RmCommand,
            }

            if action in command_classes:
                command_classes[action].execute(fs, *args)
            else:
                print(f"Invalid command: '{action}'")

        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
