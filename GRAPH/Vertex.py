from typing import Any

class Vertex:
    data: Any
    index: int

    def __init__(self, data, index = None):
        self.data = data
        self.index = index