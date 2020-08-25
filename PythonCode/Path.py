class Path:
    
    def __init__(self, sourceDestinationID, pathID, 
                 sourceEdgeLink, edgeAggLink, aggCoreLink,
                 coreAggLink, aggEdgeLink, edgeDestinationLink):
                 
            self.sourceDestinationID    = sourceDestinationID
            self.pathID                 = pathID
            
            self.sourceEdgeLink         = sourceEdgeLink
            self.edgeAggLink    = edgeAggLink
            self.aggCoreLink    = aggCoreLink
            self.coreAggLink    = coreAggLink
            self.aggEdgeLink    = aggEdgeLink
            self.edgeDestinationLink    = edgeDestinationLink
            
            
    def __repr__(self):
        return '<Path sourceDestinationID: %s,pathID: %s \
                sourceEdgeLink: %s, edgeAggLink: %s, aggCoreLink: %s,\n\
                coreAggLink: %s, aggEdgeLink: %s, edgeDestinationLink: %s\n>' %(
                self.sourceDestinationID, self.pathID,
                self.sourceEdgeLink, self.edgeAggLink, self.aggCoreLink,
                self. coreAggLink, self.aggEdgeLink, self.edgeDestinationLink)