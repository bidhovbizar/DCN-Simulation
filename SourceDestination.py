from Node import Node
from Link import Links
from Path import Path
from Arrival import Arrival

class SourceDestination:
    def __init__(self, _id, source, destination):
        self._id                = _id
        self.source             = source
        self.destination        = destination
        self.pathList           = []
        
    def __repr__(self):
        return '<SourceDestination _id: %s, source: %s, destination: %s\n\
                pathList: %s\n> %(
                self._id, self.source, self.destination,
                self.pathList)