from typing import Optional
from Vertex import *

class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source, destination, weight: Optional[float]) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight