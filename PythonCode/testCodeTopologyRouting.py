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

numPorts = 6

systemParameters = SystemParameters(flowArrivalRate, probElephantFlow,
				 elephantBandwidth, elephantServiceShift, elephantServiceMean, elephantServiceType,
                 miceBandwidth, miceServiceShift, miceServiceMean, miceServiceType,
                 hostEdgeBandwidth, edgeAggBandwidth, aggCoreBandwidth, coreAggBandwidth, aggEdgeBandwidth, edgeHostBandwidth)
topology = FatTreeTopology(systemParameters, numPorts)

# Testing Routing connectivity continuity
print("Testing Routing connectivity continuity")
for source in topology.hostList:
            for dest in topology.hostList:
                if(source == dest):
                    continue
                sourceDestId     = str(source._id)+ ':' +str(dest._id)
                for pathId in range(topology.numPaths):
                    if(topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeAggLink == None and
                       topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggEdgeLink == None and
                       topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggCoreLink == None and 
                       topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].coreAggLink == None):
                        if( topology.sourceDestinationDictionary[sourceDestId].source == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].sourceEdgeLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].sourceEdgeLink.output == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeDestinationLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeDestinationLink.output  == topology.sourceDestinationDictionary[sourceDestId].destination ):
                            continue
                        else:
                            print(topology.sourceDestinationDictionary[sourceDestId].pathList[pathId])
                            break
                        
                    elif(topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].coreAggLink == None and
                         topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggCoreLink == None):
                        if(  topology.sourceDestinationDictionary[sourceDestId].source == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].sourceEdgeLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].sourceEdgeLink.output == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeAggLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeAggLink.output  == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggEdgeLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggEdgeLink.output  == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeDestinationLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeDestinationLink.output  == topology.sourceDestinationDictionary[sourceDestId].destination ):
                            continue
                        else:
                            print(topology.sourceDestinationDictionary[sourceDestId].pathList[pathId])
                            break
                        
                    elif(topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeAggLink != None and
                         topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggEdgeLink != None and 
                         topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggCoreLink != None and 
                         topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].coreAggLink != None and 
                         topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].sourceEdgeLink != None and 
                         topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeDestinationLink != None):                            
                        if( topology.sourceDestinationDictionary[sourceDestId].source == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].sourceEdgeLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].sourceEdgeLink.output == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeAggLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeAggLink.output  == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggCoreLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggCoreLink.output  == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].coreAggLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].coreAggLink.output  == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggEdgeLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].aggEdgeLink.output  == topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeDestinationLink.input and
                           topology.sourceDestinationDictionary[sourceDestId].pathList[pathId].edgeDestinationLink.output  == topology.sourceDestinationDictionary[sourceDestId].destination ):
                            continue
                        else:
                            print(topology.sourceDestinationDictionary[sourceDestId].pathList[pathId])
                            break
                    else:
                        print(topology.sourceDestinationDictionary[sourceDestId].pathList[pathId])
                        break
                    
                    