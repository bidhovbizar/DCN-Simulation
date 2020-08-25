class Node:
    def __init__(self,_id):
        self._id = _id
        
    def __repr__(self):
        return 'ID: %s' %(self._id)


class Host(Node):
    
    def __init__(self, _id, edge = None):
        Node.__init__(self,_id)
        self.edge   = edge
        
    def __repr__(self):
        return '\n<%s, %s edge: %s>' %(
                Node.__repr__(self), 
                Host.__name__, self.edge._id)
                
    def setEdge(self, edge):
        self.edge = edge

class Switch(Node):
    def __init__(self, _id, bufferSize = 0):
        Node.__init__(self,_id)
        self.bufferSize = bufferSize
        
    def __repr__(self):
        return '\nID: %s, bufferSize: %s\n' %(self._id, self.bufferSize)
        
class Edge(Switch):
    def __init__(self,_id):
        Switch.__init__(self, _id)
        self.hostList       = []
        self.aggList= []
        
    def __repr__(self):
        return '%s <%s len(hostList): %s, len(aggList): %s>\n' %(
                Switch.__repr__(self),
                Edge.__name__, len(self.hostList),
                len(self.aggList))
    
    def setHost(self, host):
        self.hostList.append(host)
    
    def setAgg(self, agg):
        self.aggList.append(agg)
    
        
class Agg(Switch):
    def __init__(self,_id):
        Switch.__init__(self, _id)
        self.edgeList       = []
        self.coreList       = []
        
    def __repr__(self):
        return '%s <%s len(edgeList): %s, len(coreList): %s>\n' %(
                Switch.__repr__(self),
                Agg.__name__, len(self.edgeList),
                len(self.coreList))
    
    def setEdge(self, edge):
        self.edgeList.append(edge)
        
    def setCore(self, core):
        self.coreList.append(core)
        
class Core(Switch):
    def __init__(self,_id):
        Switch.__init__(self, _id)
        self.aggList= []
        
    def __repr__(self):
        return '%s <%s len(aggList): %s>\n' %(
                Switch.__repr__(self),
                Core.__name__, len(self.aggList))

    def setAgg(self, agg):
        self.aggList.append(agg)