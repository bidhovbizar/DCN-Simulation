import Path as Path
from Topology import Topology
from FatTreeTopology import FatTreeTopology

class Controller(FatTreeTopology):
    
    def __init__(self,numPort):
        FatTreeTopology.__init__(self, numPort)
        self.lastPathList = []
    
    def __repr__(self):
        return '%s \n\
                < Controller LastPathList: %s\n>' %(
                Topology.__repr__(self),
                self.lastPathList)
    
    def assignPath(self,sourceDestination, _typePath):
            # By default the _typePath is set to 0 i.e. Random
        pathID                             = Topology.findPathID(_typePath)
        self.lastPathList                  = self.updateLastPath(sourceDestination, pathID)
        return pathID

    def updateLastPath(self,sourceDestination, pathID):
        # Receives the last path and goes to self.lastPathList and update the last path chosen for round robin
