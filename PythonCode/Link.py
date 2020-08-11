from Node import Node
from Host import Host
from Edge import Edge
from Aggregation import Aggregation
from Core import Core

class Link:
    def __init__(self, _id, egress, ingress, bandwidth, bufferSize = 0, delay = 0 ):
        self._id                = _id
        self.egress             = egress
        self.ingress            = ingress
        
        self.bufferSize         = bufferSize
        self.delay              = delay
        self.bandwidth          = bandwidth
        self.bandwidthUtilized  = 0 
        self.flowList           = []
        
    def __repr__(self):
        return '<Links _id: %s, egress: %s, ingress: %s,\n\
                 bufferSize: %s, delay: %s, bandwidth: %s, flowList: %s\n>' %(
                 self._id, self.egress, self.ingress,
                 self.bufferSize, self.delay, self.bandwidth, self.flowList)

class HostEdgeLink(Link):
    
    def __init__(self, _id, egress, ingress, bandwidth, flowList = []):
        Link.__init__(self, _id, egress, ingress, bandwidth, flowList)

    def __repr__(self):
        return '<%s>\n %s' %(HostEdgeLink.__name__, Link.__repr__(self))
        

class EdgeHostLink(Link):
     def __init__(self, _id, egress, ingress, bandwidth, flowList = []):
        Link.__init__(self, _id, egress, ingress, bandwidth, flowList)
       
    def __repr__(self):
        return '<%s>\n %s' %(EdgeHostLink.__name__, Link.__repr__(self))
        
class EdgeAggregationLink(Link):
    
    def __init__(self, _id, egress, ingress, bandwidth, flowList = []):
        Link.__init__(self, _id, egress, ingress, bandwidth, flowList)

    def __repr__(self):
        return '<%s>\n %s' %(EdgeAggregationLink.__name__, Link.__repr__(self))
    
class AggregationEdgeLink(Link):
    
    def __init__(self, _id, egress, ingress, bandwidth, flowList = []):
        Link.__init__(self, _id, egress, ingress, bandwidth, flowList)

    def __repr__(self):
        return '<%s>\n %s' %(AggregationEdgeLink.__name__, Link.__repr__(self))
    
class AggregationCoreLink(Link):
    
    def __init__(self, _id, egress, ingress, bandwidth, flowList = []):
        Link.__init__(self, _id, egress, ingress, bandwidth, flowList)

    def __repr__(self):
        return '<%s>\n %s' %(AggregationCoreLink.__name__, Link.__repr__(self))

class CoreAggregationLink(Link):
    
    def __init__(self, _id, egress, ingress, bandwidth, flowList = []):
        Link.__init__(self, _id, egress, ingress, bandwidth, flowList)

     def __repr__(self):
        return '<%s>\n %s' %(CoreAggregationLink.__name__, Link.__repr__(self))




