class Node:
    def __init__(self,_id):
        self._id = _id
        
    def __repr__(self):
        return '<Node _id: %s\n>' %(self._id)


class Host(Node):
    def __init__(self, _id, edge):
        Node.__init__(self,_id)
        self.edge   = edge
        
    def __repr__(self):
        return '%s \n\
                <%s edge: %s\n>' %(
                Node.__repr__(self), 
                Host.__name__, self.edge)

class Switch(Node):
    def __init__(self, _id, bufferSize = 0):
        Node.__init__(self,_id)
        self.bufferSize = bufferSize
        
    def __repr__(self):
        return '<Node _id: %s, bufferSize: %s\n>' %(self._id, self.bufferSize)
        
class Edge(Switch):
    def __init__(self,_id):
        Switch.__init__(self,_id)
        self.hostList       = []
        self.aggregationList= []
        
    def __repr__(self):
        return '%s \n\
                <%s hostList: %s,\n\
                aggregationList: %s\n>' %(
                Switch.__repr__(self),
                Edge.__class__, self.hostList,
                self.aggregationList)
        
class Aggregation(Switch):
    def __init__(self,_id):
        Switch.__init__(self,_id)
        self.edgeList       = []
        self.coreList       = []
        
    def __repr__(self):
        return '%s \n\
                <%s edgeList: %s,\n\
                coreList: %s\n>' %(
                Switch.__repr__(self),
                Aggregation.__class__, self.edgeList,
                self.coreList)
       
class Core(Switch):
    def __init__(self,_id):
        Switch.__init__(self,_id)
        self.aggregationList= []
        
    def __repr__(self):
        return '%s \n\
                <%s aggregationList: %s\n>' %(
                Switch.__repr__(self),
                Core.__class__, self.aggregationList)
               
 