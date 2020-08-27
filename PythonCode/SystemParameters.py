from LifeTime import LifeTime, ShiftedExponentialLifeTime, ShiftedParetoLifeTime

class Elephant:
    
    def __init__(self, bandwidth, serviceMean, serviceShift):
        self.bandwidth      = bandwidth
        self.serviceType    = 1
        self.lifeTime       = ShiftedParetoLifeTime(serviceMean, serviceShift)

    def __repr__(self):
        return '< Elephant bandwidth: %s,serviceType: %s >\n%s' %(
                 self.bandwidth, self.serviceType, self.lifeTime)

class Mice:
    
    def __init__(self, bandwidth, serviceMean, serviceShift):
        self.bandwidth          = bandwidth
        self.serviceType        = 0
        self.lifeTime           = ShiftedExponentialLifeTime(serviceMean, serviceShift)
    
    def __repr__(self):
        return '< Mice  bandwidth: %s, serviceType: %s >\n%s' %(
                self.bandwidth, self.serviceType, self.lifeTime)
        
class LinkBandwidth:
    
    def __init__(self, hostEdge, edgeAgg, aggCore, coreAgg, aggEdge, edgeHost):
        self.hostEdge         = hostEdge
        self.edgeAgg          = edgeAgg
        self.aggCore          = aggCore
        self.coreAgg          = coreAgg
        self.aggEdge          = aggEdge
        self.edgeHost         = edgeHost
    
    def __repr__(self):
        return'< LinkBandwidth hostEdge: %s, edgeAgg: %s, aggCore: %s, coreAgg: %s, aggEdge: %s, edgeHost: %s >'%(
                self.hostEdge, self.edgeAgg, self.aggCore, self.coreAgg, self.aggEdge, self.edgeHost)

class SystemParameters:

    def __init__(self, flowArrivalRate, probElephantFlow,
				 elephantBandwidth, elephantServiceShift, elephantServiceMean, elephantServiceType,
                 miceBandwidth, miceServiceShift, miceServiceMean, miceServiceType,
                 hostEdgeBandwidth, edgeAggBandwidth, aggCoreBandwidth, coreAggBandwidth, aggEdgeBandwidth, edgeHostBandwidth):

        self.flowArrivalRate    = flowArrivalRate
        self.probElephantFlow   = probElephantFlow
        
        # Push  global Variable
        self.numFlows           = 0
    
        self.elephant           = Elephant(elephantBandwidth, elephantServiceMean, elephantServiceShift)
        self.mice               = Mice(miceBandwidth, miceServiceMean, miceServiceShift)
        self.linkBandwidth      = LinkBandwidth(hostEdgeBandwidth, edgeAggBandwidth, aggCoreBandwidth, coreAggBandwidth, aggEdgeBandwidth, edgeHostBandwidth)
        
    def __repr__(self):
        return  '< SystemParameters flowArrivalRate: %s, \n\
numFlows: %s, \n\
probElephantFlow: %s\n\
%s\n\
%s\n\
%s\n>' %(
        self.flowArrivalRate,
        self.numFlows,
        self.probElephantFlow,
        self.elephant,
        self.mice,
        self.linkBandwidth)

