# cp_command.py
from node import Node

class CpCommand:
    @staticmethod
    def execute(fs, source, destination):
        source_node, source_name = fs._parse_path(source)
        destination_node, destination_name = fs._parse_path(destination)

        if source_name not in source_node.children:
            print(f"Error: Source '{source}' does not exist")
            return

        if destination_name in destination_node.children:
            print(f"Error: Destination '{destination}' already exists")
            return

        source_data = source_node.children[source_name].content
        destination_node.children[destination_name] = Node(destination_name, True, source_data)
