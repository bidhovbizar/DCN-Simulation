import numpy as np
import random
from Topology import Topology,FatTreeTopology
from Flow import MiceFlow,ElephantFlow 
from Path import Path
from SourceDestination import SourceDestination
from SystemParameters import SystemParameters
from Arrival import Arrival, ExponentialArrival

class System:

    def __init__(self, flowArrivalRate, probElephantFlow,
				 elephantBandwidth, elephantServiceShift, elephantServiceMean, elephantServiceType,
                 miceBandwidth, miceServiceShift, miceServiceMean, miceServiceType,
                 hostEdgeBandwidth, edgeAggBandwidth, aggCoreBandwidth, coreAggBandwidth, aggEdgeBandwidth, edgeHostBandwidth,
				 numPorts):
        
        self.systemParameters = SystemParameters(flowArrivalRate, probElephantFlow,
				 elephantBandwidth, elephantServiceShift, elephantServiceMean, elephantServiceType,
                 miceBandwidth, miceServiceShift, miceServiceMean, miceServiceType,
                 hostEdgeBandwidth, edgeAggBandwidth, aggCoreBandwidth, coreAggBandwidth, aggEdgeBandwidth, edgeHostBandwidth)
        
        self.topology = FatTreeTopology(self.systemParameters, numPorts = 4)

        self.eventTime          = 0
        self.activeFlowList     = []
        self.numFlows           = 0
        self.lastPathList       = []
        
        self.arrival            = Arrival(systemParameters.flowArrivalRate)
        self.elephantParameters = systemParameters.elephant
        self.miceParameters     = systemParameters.mice

        self.nextArrivalTime    = 0
        self.nextDepatureTime   = 'inf' # this would depend on type of the flow so let this be default
        
        if self.nextArrivalTime < self.nextDepatureTime:
            self.updateAtArrival()
        else:
            self.updateAtDeparture()

    def __repr__(self):

        return '%s,\n\
                %s,\n\
                <System # Flow in activeFlowList: %s,\n\
                lastPathList: %s,\n\
                nextArrivalTime: %s, nextDepartureTime: %s\n>' %(
                self.systemParameters,
                self.topology,
                len(self.activeFlowList),
                self.lastPathList,
                self.nextArrivalTime, self.nextDepatureTime)

    # Check whether to shift to State
    def updateAtArrival(self):
        newFlowId       = self.numFlows

        srcDestDict     = random.choice(self.topology.sourceDestinationDictionary)
        
        srcDestId       =  self.topology.sourceDestinationList[self.topology.findSourceDestination(_typeSourceDestination = 0)].index()
        
        #_typePath decides how is the next path assigned for the sourceDestination Pair
        # We can assign _typePath in 3 ways
        # 0 Random : use indexOfPath
        # 1 Round Robin
        # 2 Load Aware
        pathID                   = random.choice(srceDest.pathList)
        path                     = Path
        

        if random.random() <= probElephantFlow:
            newFlow     = ElephantFlow(newFlowId, srcDestId, self.nextArrivalTime, path, self.elephantParameters)
        else:
            newFlow     = MiceFlow(newFlowId,srcDestId, self.nextArrivalTime, path, self.miceParameters)
        #checking sample elephant or mice flow
#        if (np.random.binomial(size=1, n=1, p= self.SystemParameters.probElephantFlow) == 1):
#            #isMice = False
#            newFlow                    = ElephantFlow(_id, sourceDestinationID, self.nextArrivalTime, self.Topology.sourceDestinationDictionary[sourceDestinationID].pathList[pathID], self.SystemParameters)
#        
#        else:
#            #isMice = True
#            newFlow                 = MiceFlow(_id, sourceDestinationID, self.nextArrivalTime, self.Topology.sourceDestinationDictionary[sourceDestinationID].pathList[pathID], self.SystemParameters)
        
        self.activeFlowList.append(newflow)
        self.numFlows       += 1
        self.nextArrivalTime+= self.arrival.getDuation()

    # Check whether to shift to State
    def updateAtDeparture(self):
        # update the state of the varibles at the departure of an old flow
        
    def arrivalNewFlow(self, _typePath = 0, _typeSourceDestination = 0):

        
        
    def findSourceDestination(self, _typeSourceDestination = 0, source = 0, destination = 0)
        # Fetch the the source and destination pair and return the path or finds the sourceDestination Object corresponding to source and destination and return it
        if (_typeSourceDestination = 0):
            return random.sample(range(self.numSourceDestinationPair),1)
        
	def assignPath(self, sourceDestination, _typePath):
            # By default the _typePath is set to 0 i.e. Random
            pathID                             = self.Topology.findPathID(_typePath)
            self.lastPathList                  = self.updateLastPath(sourceDestination, pathID)
            return pathID

    def updateLastPath(self,sourceDestination, pathID):
        # Receives the last path and goes to self.lastPathList and update the last path chosen for round robin

        
    def findLastFlowLeft(self,activeFlowList):
        #find the time when the last flow leave the system or time when we stop observing
    
    def plotCountPackets(t1,t2):
        #counts the number of packets between time t1 and t2 while sampling
    
    def plotMicroBurst():
        #Plot CDF vs Microburst
