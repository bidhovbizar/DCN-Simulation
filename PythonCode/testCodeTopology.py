from SystemParameters import SystemParameters
from Topology import FatTreeTopology
flowArrivalRate     = 1 
probElephantFlow    = 1

elephantBandwidth   = 10
elephantServiceShift = 0  
elephantServiceMean = 10 
elephantServiceType = 1

miceBandwidth   = 1
miceServiceShift = 0 
miceServiceMean = 1 
miceServiceType = 0
                 
hostEdgeBandwidth = 1
edgeAggBandwidth = 2 
aggCoreBandwidth = 3
coreAggBandwidth = 4
aggEdgeBandwidth = 5 
edgeHostBandwidth = 6

numPorts = 4

systemParameters = SystemParameters(flowArrivalRate, probElephantFlow,
				 elephantBandwidth, elephantServiceShift, elephantServiceMean, elephantServiceType,
                 miceBandwidth, miceServiceShift, miceServiceMean, miceServiceType,
                 hostEdgeBandwidth, edgeAggBandwidth, aggCoreBandwidth, coreAggBandwidth, aggEdgeBandwidth, edgeHostBandwidth)
topology = FatTreeTopology(systemParameters, numPorts)

#print(topology)
#print('\n')
#print(topology.hostList)
#print('\n')
#print(topology.edgeList)
#print('\n')
#print(topology.aggList)
#print('\n')
#print(topology.coreList)
#print('\n')
#print(topology.hostEdgeLinks)
#print('\n')
#print(topology.edgeAggLinks)
#print('\n')
#print(topology.aggCoreLinks)
#print('\n')
#print(topology.coreAggLinks)
#print('\n')
#print(topology.aggEdgeLinks)
#print('\n')
#
