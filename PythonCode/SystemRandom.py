import random
from Topology import FatTreeTopology
from Flow import MiceFlow, ElephantFlow 
from SystemParameters import SystemParameters
from Arrival import ExponentialArrival

class SystemRandom:

    def __init__(self, flowArrivalRate, probElephantFlow,
				 elephantBandwidth, elephantServiceShift, elephantServiceMean, elephantServiceType,
                 miceBandwidth, miceServiceShift, miceServiceMean, miceServiceType,
                 hostEdgeBandwidth, edgeAggBandwidth, aggCoreBandwidth, coreAggBandwidth, aggEdgeBandwidth, edgeHostBandwidth,
				 numPorts):
        
        self.systemParameters = SystemParameters(flowArrivalRate, probElephantFlow,
				 elephantBandwidth, elephantServiceShift, elephantServiceMean, elephantServiceType,
                 miceBandwidth, miceServiceShift, miceServiceMean, miceServiceType,
                 hostEdgeBandwidth, edgeAggBandwidth, aggCoreBandwidth, coreAggBandwidth, aggEdgeBandwidth, edgeHostBandwidth)
        
        self.topology = FatTreeTopology(self.systemParameters, numPorts)

        self.activeFlowList     = []
        self.numFlows           = 0
        
        self.arrival            = ExponentialArrival(self.systemParameters.flowArrivalRate)
        self.elephantParameters = self.systemParameters.elephant
        self.miceParameters     = self.systemParameters.mice

        self.nextArrivalTime            = 0
        self.nextDepatureTime           = 'inf'
        self.departureTimeOfLastFlow    = 0
        self.linkUnderObservation       = random.choice(self.topology.hostEdgeLinks)
        self.linkState                  = []
        self.linkEventTime              = []
        
    def __repr__(self):

        return '%s,\n\
%s,\n\
< System # Flow in activeFlowList: %s,\n\
nextArrivalTime: %s, nextDepartureTime: %s>\n' %(
                                                self.systemParameters,
                                                self.topology,
                                                len(self.activeFlowList),
                                                self.nextArrivalTime, self.nextDepatureTime)

    def runSimulation(self, numFlows):
        while(self.numFlows < numFlows or self.nextDepatureTime <= self.departureTimeOfLastFlow):
            if(self.numFlows < numFlows):
                # When flows are still arriving we need to check whether we are going to have arrival or departure
                if (self.nextArrivalTime < self.nextDepatureTime):
                    self.updateAtArrival()
                else:
                    self.updateAtDeparture()
                # When the last flow arrives the the loop should run till the last flow leaves the system
                if (self.numFlows == numFlows) :
                    for flow in self.activeFlowList:
                        self.departureTimeOfLastFlow = flow.departureTime if flow.departureTime > self.departureTimeOfLastFlow else self.departureTimeOfLastFlow
        
                #print(str(self.numFlows) + ' : ' + str(len(self.activeFlowList)))
            else:
                self.updateAtDeparture()
                #print(str(self.numFlows) + ' : ' + str(len(self.activeFlowList)))
    

    def updateAtArrival(self):
        self.probeLink()        
        
        newFlowId       = self.numFlows
        sourceDest      = self.findSourceDestination(self.topology.sourceDestinationDictionary)
        sourceDestId    = sourceDest._id
        path            = random.choice(sourceDest.pathList)
        
        if (random.random() <= self.systemParameters.probElephantFlow):
            newFlow     = ElephantFlow(newFlowId, sourceDestId, self.nextArrivalTime, path, self.elephantParameters)
        else:
            newFlow     = MiceFlow(newFlowId, sourceDestId, self.nextArrivalTime, path, self.miceParameters)
        
        
        newFlow.path.addFlowToLinks(newFlow)
        self.activeFlowList.append(newFlow)
        
        self.nextDepatureTime           = newFlow.departureTime if self.nextDepatureTime > newFlow.departureTime else self.nextDepatureTime
        self.departureTimeOfLastFlow    = newFlow.departureTime if newFlow.departureTime > self.departureTimeOfLastFlow else self.departureTimeOfLastFlow
        self.numFlows                   += 1
        self.nextArrivalTime            += self.arrival.getDuration()


    def updateAtDeparture(self):
        self.probeLink()

        departingFlowList   = [ flow for flow in self.activeFlowList if flow.departureTime == self.nextDepatureTime]
        departingFlow       = departingFlowList[0]
        departingFlow.path.removeFlowFromLinks(departingFlow)
        self.activeFlowList.remove(departingFlow)
        self.nextDepatureTime = 'inf'
        for flow in self.activeFlowList:
            if (flow.departureTime < self.nextDepatureTime):
                self.nextDepatureTime = flow.departureTime

    def probeLink(self):
        self.linkState.append(self.linkUnderObservation.bandwidthUtilized)
        self.linkEventTime.append(self.nextDepatureTime)
        # self.linkEventTime[0] is 'inf' as self.nextDepartureTime in the first iteration is 'inf' so lets change it to make sense
        self.linkEventTime[0] = 0
        
    def postProcessingLinkData(self):
        # Post Processing the linkState to remove idle state after the last flow leave
        self.linkState      = self.linkState[::-1]
        self.linkEventTime  = self.linkEventTime[::-1]
        
        for stateIndex in range(len(self.linkState)):
            if(self.linkState[stateIndex] == 0):
                self.linkState[stateIndex] = 'inf'
                self.linkEventTime[stateIndex] = 'inf'
            else:
                break
            
        for stateIndex in range(self.linkState.count('inf')):
            self.linkState.remove('inf')
            self.linkEventTime.remove('inf')
            
        self.linkState      = self.linkState[::-1]
        self.linkEventTime  = self.linkEventTime[::-1]
        
    def findSourceDestination(self, srcDstDict):
        source      = random.choice(self.topology.hostList)
        dest        = random.choice(self.topology.hostList)
        while(dest == source):
            dest = random.choice(self.topology.hostList)
        return srcDstDict[str(source._id) + ':' + str(dest._id)]

            
    def findLastFlowLeft(self,activeFlowList):
        #find the time when the last flow leave the system or time when we stop observing
        pass
    
    def plotCountPackets(t1,t2):
        #counts the number of packets between time t1 and t2 while sampling
        pass
    
    def plotMicroBurst():
        #Plot CDF vs Microburst
        pass
