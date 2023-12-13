
from node import Node

class FileSystem:
    def __init__(self):
        self.root = Node('/')
        self.current_dir = self.root
