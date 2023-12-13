# node.py
class Node:
    def __init__(self, name, is_file=False, content=None):
        self.name = name
        self.is_file = is_file
        self.content = content
        self.children = {}
