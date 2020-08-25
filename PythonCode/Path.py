class Path:
    
    def __init__(self, sourceDestinationID, pathID, 
                 sourceEdgeLink, edgeAggLink, aggCoreLink,
                 coreAggLink, aggEdgeLink, edgeDestinationLink):
                 
            self.sourceDestinationID    = sourceDestinationID
            self.pathID                 = pathID
            
            self.sourceEdgeLink         = sourceEdgeLink
            self.edgeAggLink            = edgeAggLink
            self.aggCoreLink            = aggCoreLink
            self.coreAggLink            = coreAggLink
            self.aggEdgeLink            = aggEdgeLink
            self.edgeDestinationLink    = edgeDestinationLink
            
            
    def __repr__(self):
        return '\n<Path sourceDestinationID: %s, pathID: %s \n\
sourceEdgeLink: %s,\n\
edgeAggLink: %s,\n\
aggCoreLink: %s,\n\
coreAggLink: %s,\n\
aggEdgeLink: %s,\n\
edgeDestinationLink: %s>\n' %(
                self.sourceDestinationID, self.pathID,
                self.sourceEdgeLink, self.edgeAggLink, self.aggCoreLink,
                self. coreAggLink, self.aggEdgeLink, self.edgeDestinationLink)