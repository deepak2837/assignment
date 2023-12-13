# mv_command.py
class MvCommand:
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

        moved_node = source_node.children[source_name]
        moved_node.name = destination_name
        destination_node.children[destination_name] = moved_node
        del source_node.children[source_name]
