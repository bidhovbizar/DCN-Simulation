from Node import Node,Host,Edge,Agg,Core
from SystemParameters import SystemParameters

class Link:
    
        # Characterisation of Links
        #_type=0 -> hostEdgeLink
        #_type=1 -> edgeAggLink
        #_type=2 -> aggCoreLink
        #_type=3 -> coreAggLink
        #_type=4 -> aggEdgeLink
        #_type=5 -> edgeHostLink
    def __init__(self, _id, input, output, bandwidth, _type, bufferSize = 0, delay = 0 ):
        self._id                = _id
        self.input              = input
        self.output             = output
        self.bandwidth          = bandwidth
        self._type              = _type
        self.bufferSize         = bufferSize
        self.delay              = delay

        self.bandwidthUtilized  = 0
        self.flowList           = []
        
    def addFlow(self, flow):
        self.flowList.append(flow)
        self.bandwidthUtilized += flow.bandwidth 
        
    def removeFlow(self, flow):
        self.flowList.remove(flow)
        self.bandwidthUtilized -= flow.bandwidth
        
    def __repr__(self):
        if(self._type == 0):
            return '<Links _id: %s,\n Host : %s, Edge: %s,\n\
 bufferSize: %s, delay: %s, bandwidth: %s, bandwidthUtilization: %s,\n\
 flowList: %s\n>' %(
                self._id, self.input._id, self.output._id,
self.bufferSize, self.delay, self.bandwidth, self.bandwidthUtilized,
self.flowList)
        
        elif(self._type == 1):
            return '<Links _id: %s,\n Edge : %s, Agg: %s,\n\
 bufferSize: %s, delay: %s, bandwidth: %s, bandwidthUtilization: %s,\n\
 flowList: %s\n>' %(
                self._id, self.input._id, self.output._id,
self.bufferSize, self.delay, self.bandwidth, self.bandwidthUtilized,
self.flowList)
 
        elif(self._type == 2):
             return '<Links _id: %s,\n Agg : %s, Core: %s,\n\
 bufferSize: %s, delay: %s, bandwidth: %s, bandwidthUtilization: %s,\n\
 flowList: %s\n>' %(
                self._id, self.input._id, self.output._id,
self.bufferSize, self.delay, self.bandwidth, self.bandwidthUtilized,
self.flowList)
 
        elif(self._type == 3):
            return '<Links _id: %s,\n Core : %s, Agg: %s,\n\
 bufferSize: %s, delay: %s, bandwidth: %s, bandwidthUtilization: %s,\n\
 flowList: %s\n>' %(
                self._id, self.input._id, self.output._id,
self.bufferSize, self.delay, self.bandwidth, self.bandwidthUtilized,
self.flowList)
 
        elif(self._type == 4):
            return '<Links _id: %s,\n Agg : %s, Edge: %s,\n\
 bufferSize: %s, delay: %s, bandwidth: %s, bandwidthUtilization: %s,\n\
 flowList: %s\n>' %(
                self._id, self.input._id, self.output._id,
self.bufferSize, self.delay, self.bandwidth, self.bandwidthUtilized,
self.flowList)
 
        elif(self._type == 5):
            return '<Links _id: %s,\n Edge : %s, Host: %s,\n\
 bufferSize: %s, delay: %s, bandwidth: %s, bandwidthUtilization: %s,\n\
 flowList: %s\n>' %(
                self._id, self.input._id, self.output._id,
self.bufferSize, self.delay, self.bandwidth, self.bandwidthUtilized,
self.flowList)
 
 