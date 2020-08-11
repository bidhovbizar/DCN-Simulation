from SourceDestination import SourceDestination

class Path:
    
    def __init__(self, sourceDestinationID, pathID, 
                 sourceEdgeLink, edgeAggregationLink, aggregationCoreLink,
                 coreAggregationLink, aggregationEdgeLink, edgeDestinationLink):
                 
            self.sourceDestinationID    = sourceDestinationID
            self.pathID                 = pathID
            
            self.sourceEdgeLink         = sourceEdgeLink
            self.edgeAggregationLink    = edgeAggregationLink
            self.aggregationCoreLink    = aggregationCoreLink
            self.coreAggregationLink    = coreAggregationLink
            self.aggregationEdgeLink    = aggregationEdgeLink
            self.edgeDestinationLink    = edgeDestinationLink
            
            
    def __repr__(self):
        return '<Path sourceDestinationID: %s,pathID: %s \
                sourceEdgeLink: %s, edgeAggregationLink: %s, aggregationCoreLink: %s,\n\
                coreAggregationLink: %s, aggregationEdgeLink: %s, edgeDestinationLink: %s\n>' %(
                self.sourceDestinationID, self.pathID,
                self.sourceEdgeLink, self.edgeAggregationLink, self.aggregationCoreLink,
                self. coreAggregationLink, self.aggregationEdgeLink, self.edgeDestinationLink)