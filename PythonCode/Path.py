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
        if(self.edgeAggLink == None and self.aggEdgeLink == None and self.aggCoreLink == None and self.coreAggLink == None):
            return '\n<Path sourceDestinationID: %s, pathID: %s \n\
sourceEdgeLink: %s,\n\
edgeAggLink: %s,\n\
aggCoreLink: %s,\n\
coreAggLink: %s,\n\
aggEdgeLink: %s,\n\
edgeDestinationLink: %s>\n' %(
                self.sourceDestinationID, self.pathID,
                self.sourceEdgeLink._id, self.edgeAggLink, self.aggCoreLink,
                self.coreAggLink, self.aggEdgeLink, self.edgeDestinationLink._id)

        elif(self.coreAggLink == None and self.aggCoreLink == None):
            return '\n<Path sourceDestinationID: %s, pathID: %s \n\
sourceEdgeLink: %s,\n\
edgeAggLink: %s,\n\
aggCoreLink: %s,\n\
coreAggLink: %s,\n\
aggEdgeLink: %s,\n\
edgeDestinationLink: %s>\n' %(
                self.sourceDestinationID, self.pathID,
                self.sourceEdgeLink._id, self.edgeAggLink._id, self.aggCoreLink,
                self.coreAggLink, self.aggEdgeLink._id, self.edgeDestinationLink._id)

        elif(self.edgeAggLink != None and self.aggEdgeLink != None
             and self.aggCoreLink != None and self.coreAggLink != None
             and self.sourceEdgeLink != None and self.edgeDestinationLink != None):
            return '\n<Path sourceDestinationID: %s, pathID: %s \n\
sourceEdgeLink: %s,\n\
edgeAggLink: %s,\n\
aggCoreLink: %s,\n\
coreAggLink: %s,\n\
aggEdgeLink: %s,\n\
edgeDestinationLink: %s>\n' %(
                self.sourceDestinationID, self.pathID,
                self.sourceEdgeLink._id, self.edgeAggLink._id, self.aggCoreLink._id,
                self.coreAggLink._id, self.aggEdgeLink._id, self.edgeDestinationLink._id)

        else:
            return '\n<Path sourceDestinationID: %s, pathID: %s \n\
sourceEdgeLink: %s,\n\
edgeAggLink: %s,\n\
aggCoreLink: %s,\n\
coreAggLink: %s,\n\
aggEdgeLink: %s,\n\
edgeDestinationLink: %s>\n' %(
                self.sourceDestinationID, self.pathID,
                self.sourceEdgeLink, self.edgeAggLink, self.aggCoreLink,
                self.coreAggLink, self.aggEdgeLink, self.edgeDestinationLink)