import numpy as np
import random
from Arrival import Arrival
from Lifetime import Lifetime
from ShiftedExponentialLifeTime import ShiftedExponentialLifeTime
from ShiftedParetoLifeTime import ShiftedParetoLifeTime
from Topology import Topology
from FatTreeTopology import FatTreeTopology
from Flow import Flow
from Path import Path
from Node import Node
from Host import Host
from Edge import Edge
from Aggregation import Aggregation
from Core import Core
from SourceDestination import SourceDestination

class System(SystemParameters, FatTreeTopology, Controller):


    def __init__(self, flowArrivalRate, serviceType, probElephantFlow, 
				 elephantBandWidth, miceBandwidth, elephantServiceShift,
				 elephantServiceMean, miceServiceShift, miceServiceMean, 
				 numPorts, hostList, connectivityMatrix):
        
        SystemParameters.__init__(self,flowArrivalRate, serviceType, probElephantFlow,
    								  elephantBandWidth, miceBandwidth, elephantServiceShift, 
    								  elephantServiceMean, miceServiceShift, miceServiceMean, 
    								  numPorts, hostList, connectivityMatrix)
        Controller.__init__(self,numPorts)
        
        # FatTreeTopology inherits Topology
        FatTreeTopology.__init__(self,numPorts)
    
        lifeTimeObjectMice		    = LifeTime(True, mean, shift)
        LifeTimeObjectElephant 		= LifeTime(False, mean, shift)

        self.flowList           = []
    
        self.eventTime          = 0
        self.arrival            = Arrival(self.SystemParameters.arrivalRate)
        self.nextArrivalTime    = self.arrival.getDuation()
        self.nextDepatureTime   = 'inf' # this would depend on type of the flow so let this be default
        
        if self.nextArrivalTime < self.nextDepatureTime:
            self.updateAtArrival()
        else:
            self.updateAtDeparture()

    def __repr__(self):

        return '%s,\n\
                %s,\n\
                %s,\n\
                <# Flow in flowList: %s,\n\
                EventTime: %s, Arrival: %s, nextArrivalTime: %s, nextDepartureTime: %s\n>' %(
                SystemParameters.__repr__(self),
                Controller.__repr__(self),
                FatTreeTopology.__repr__(self),
                len(self.flowList),
                self.eventTime, self.arrival, self.nextArrivalTime, self.nextDepatureTime)

    # Check whether to shift to State
    def updateAtArrival(self):
        self.arrivalNewFlow()

    # Check whether to shift to State
    def updateAtDeparture(self):
        # update the state of the varibles at the departure of an old flow
        
    def assignTotalFlowInSystem(self,numFlows):
        self.numFlows	= numFlows
        
    def arrivalNewFlow(self, _typeService = 0, _typePath = 0, _typeSourceDestination = 0):
		# _typeService decides the  serviceType of distribution
        # 0 shiftedExponential
        # 1 shiftedPareto
		
		# calculating the flow id of new flow
		_id 						= len(self.flowList)+1
		
        # finding the source and destination 
        sourceDestinationID         = self.sourceDestinationList[self.findSourceDestinaition()].index()
        
        #_typePath decides how is the next path assigned for the sourceDestination Pair
        # We can assign _typePath in 3 ways
        # 0 Random : use indexOfPath
        # 1 Round Robin
        # 2 Load Aware
		
        pathID                      = Controller.assignPath(sourceDestination, _typePath = 0)
		
        # arrivalTime 
		lastFlowArrived 			= self.flowList[-1].arrivalTime
		arrivalTime 				= lastFlowArrived + self.arrival.getDuration()
		
		#checking sample elephant or mice flow
        if (np.random.binomial(size=1, n=1, p= self.probElephantFlow) == 1):
            isMice = False
		else:
			isMice = True
            
		# setting lifeTime and bandwidth of the flow	
        if (isMice == True):
            if  (_typeService == 0):
                lifeTimeOfMice          = ShiftedExponentialLifeTime(lifeTimeObjectMice.isMice, lifeTimeObjectMice.mean, lifeTimeObjectMice.shift)
            elif(_typeService == 1):
                lifeTimeOfMice          = ShiftedParetoLifeTime(lifeTimeObjectMice.isMice, lifeTimeObjectMice.mean, lifeTimeObjectMice.shift)
            lifeTime	 			    = lifeTimeOfMice.getDuration()
            bandwidth 				= self.miceBandwidth

        else:
            if  (_typeService == 0):
                lifeTimeOfElephant          = ShiftedExponentialLifeTime(lifeTimeObjectElephant.isMice, lifeTimeObjectElephant.mean, lifeTimeObjectElephant.shift)
            elif(_typeService == 1):
                lifeTimeOfElephant          = ShiftedParetoLifeTime(lifeTimeObjectElephant.isMice, lifeTimeObjectElephant.mean, lifeTimeObjectElephant.shift)
            lifeTime 				= lifeTimeElephant.getDuration()
            bandwidth 				= self.elephantBandWidth
		
		#create a new flow
		newFlow						= Flow(_id, sourceDestinationID, pathID, arrivalTime, 
											isMice, lifeTime, bandWidth)
		
		self.flowList.append(newflow)
        
        
    def findSourceDestination(self, _typeSourceDestination = 0, source = 0, destination = 0)
        # Fetch the the source and destination pair and return the path or finds the sourceDestination Object corresponding to source and destination and return it
        if (_typeSourceDestination = 0):
            return random.sample(range(self.numSourceDestinationPair),1)
        
    def findLastFlowLeft(self,flowList):
        #find the time when the last flow leave the system or time when we stop observing
    
    def plotCountPackets(t1,t2):
        #counts the number of packets between time t1 and t2 while sampling
    
    def plotMicroBurst():
        #Plot CDF vs Microburst
