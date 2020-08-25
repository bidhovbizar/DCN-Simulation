import random
from Link import Link
from Node import Host, Edge, Agg, Core
from SourceDestination import SourceDestination
from Path import Path

class Topology:
    def __init__(self):
        var = None
        print(var)
        
    def __repr__(self):
        return '<Topology>'
    
class FatTreeTopology(Topology):
       
    def __init__(self, systemParameters, numPorts = 4):
        self.systemParameters           = systemParameters
        self.numPorts                   = numPorts
        
        self.numHosts                   = numPorts * numPorts * numPorts/ 4
        self.numEdges                   = numPorts * numPorts / 2
        self.numAggs                    = numPorts * numPorts / 2
        self.numCores                   = numPorts * numPorts / 4
        self.numSourceDestinationPair   = self.numHosts * (self.numHosts-1)
        self.numPaths                   = numPorts * numPorts / 4
        
        
        # Nodes
        self.hostList                   = [Host(hostId) for hostId in range(self.numHosts)]
        self.edgeList                   = [Edge(edgeId) for edgeId in range(self.numEdges)]
        self.aggList                    = [Agg(aggId) for aggId in range(self.numAggs)]
        self.coreList                   = [Core(coreId) for coreId in range(self.numCores)]
        
        # Links
        self.createHostEdgeLinks()
        self.createEdgeAggLinks()
        self.createAggCoreLinks()
        self.createCoreAggLinks()
        self.createAggEdgeLinks()
        self.createEdgeHostLinks()
        
        # Source Destination and its correspoding Paths
        self.createSourceDestination(self.hostList)
        #self.sourceDestinationDictionary = {}
        
    def __repr__(self):
        return '%s\n <FatTreeTopology NumPorts: %s,\n\
                NumHosts: %s, NumEdges: %s, NumAggs: %s, NumCores: %s,\n\
                NumSourceDestinationPair: %s, NumPaths: %s,\n\
                # Hosts in HostList: %s,\n\
                # Edges in EdgeList: %s,\n\
                # Aggs in AggList: %s,\n\
                # Cores in CoreList: %s,\n\
                # Links in HostEdgeLinks: %s,\n\
                # Links in EdgeAggLinks: %s,\n\
                # Links in AggCoreLinks: %s,\n\
                # Links in CoreAggLinks: %s,\n\
                # Links in AggEdgeLinks: %s,\n\
                # Links in EdgeHostLinks: %s,\n\
                # Pairs of SourceDestination: %s\n>' %(
                Topology.__repr__(self),self.numPorts,
                self.numHosts, self.numEdges, self.numAggs, self.numCores,
                self.numSourceDestinationPair, self.numPaths,
                len(self.hostList), len(self.edgeList), len(self.aggList), len(self.coreList),
                len(self.hostEdgeLinks), len(self.edgeAggLinks), len(self.aggCoreLinks),
                len(self.coreAggLinks), len(self.aggEdgeLinks), len(self.edgeHostLinks), 
                len(self.sourceDestinationDictionary))

        # Characterisation of Links
        #_type=0 -> hostEdgeLink
        #_type=1 -> edgeAggLink
        #_type=2 -> aggCoreLink
        #_type=3 -> coreAggLink
        #_type=4 -> aggEdgeLink
        #_type=5 -> edgeHostLink
        
    def createHostEdgeLinks(self):
        self.hostEdgeLinks  = []
        divisor         = self.numPorts/2
        for host in self.hostList:
            connectedEdgeId     = host._id/divisor
            connectedEdgeList   = [edge for edge in self.edgeList if edge._id == connectedEdgeId]
            connectedEdge       = connectedEdgeList[0]
            hostEdgeLink        = Link(host._id, host, connectedEdge, self.systemParameters.linkBandwidth.hostEdge, 0)
            self.hostEdgeLinks.append(hostEdgeLink)
            host.setEdge(connectedEdge)
            
    def createEdgeAggLinks(self):
        self.edgeAggLinks           = []
        divisor                     = self.numPorts/2
        for edge in self.edgeList:
            podId                   = edge._id/divisor
            connectedAggList        = [agg for agg in self.aggList if (agg._id/divisor) == podId]
            podEdgeId               = edge._id - (self.numPorts/2) * podId
            for agg in connectedAggList:
                podAggId            = agg._id - (self.numPorts/2) * podId
                linkId              = ((self.numPorts/2)**2 * podId) + ((self.numPorts/2)* podEdgeId) + podAggId 
                self.edgeAggLinks.append( Link(linkId, edge, agg, self.systemParameters.linkBandwidth.edgeAgg, 1))
                edge.setAgg(agg)
                

    def createAggCoreLinks(self):
        self.aggCoreLinks           = []
        divisor                     = self.numPorts/2
        for agg in self.aggList:
            podId                   = agg._id/divisor
            connectedCoreList       = [core for core in self.coreList if (agg._id % divisor) == (core._id/divisor)]
            for core in connectedCoreList:
                linkId              = ((self.numPorts/2)**2 * podId) + core._id
                self.aggCoreLinks.append( Link(linkId, agg, core, self.systemParameters.linkBandwidth.aggCore, 2))
                agg.setCore(core)
                
    def createCoreAggLinks(self):
        self.coreAggLinks           = []
        divisor                     = self.numPorts/2
        for core in self.coreList:
            connectedAggList        = [agg for agg in self.aggList if (core._id / divisor) == (agg._id % divisor)]
            for agg in connectedAggList:
                linkId              = (core._id * self.numPorts) + connectedAggList.index(agg)
                self.coreAggLinks.append( Link(linkId, core, agg, self.systemParameters.linkBandwidth.coreAgg, 3))
                core.setAgg(agg)
        
    def createAggEdgeLinks(self):
        self.aggEdgeLinks           = []
        divisor                     = self.numPorts/2
        for agg in self.aggList:
            podId                       = agg._id/divisor
            connectedEdgeList  = [edge for edge in self.edgeList if (edge._id/divisor) == podId]
            podAggId   = agg._id - (self.numPorts/2) * podId
            for edge in connectedEdgeList:
                podEdgeId    = edge._id - (self.numPorts/2) * podId
                linkId      = ((self.numPorts/2)**2 * podId) + ((self.numPorts/2)* podAggId) + podEdgeId 
                self.aggEdgeLinks.append( Link(linkId, agg, edge, self.systemParameters.linkBandwidth.aggEdge, 4))
                agg.setEdge(edge)        
        
    def createEdgeHostLinks(self):
        self.edgeHostLinks  = []
        divisor         = self.numPorts/2
        for host in self.hostList:
            connectedEdgeId     = host._id/divisor
            connectedEdgeList   = [edge for edge in self.edgeList if edge._id == connectedEdgeId]
            connectedEdge       = connectedEdgeList[0]
            edgeHostLink        = Link(host._id, connectedEdge, host, self.systemParameters.linkBandwidth.edgeHost, 5)
            connectedEdge.setHost(host)
            self.edgeHostLinks.append(edgeHostLink)

    def createSourceDestination(self, numHosts):
        self.sourceDestinationDictionary = {}
        for source in self.hostList:
            for dest in self. hostList:
                if(source == dest):
                    continue
                sourceDestId     = str(source._id)+ ':' +str(dest._id)
                newSourceDestPair = SourceDestination(sourceDestId, source, dest)
                [newSourceDestPair.addPath(
                        self.populateSourceDestinationPath(newSourceDestPair, self.numPaths, pathId)
                        ) for pathId in range(self.numPaths)]                
                self.sourceDestinationDictionary.update({sourceDestId : newSourceDestPair})
        
        
    def populateSourceDestinationPath(self, sourceDestination, numPaths, pathId):
#        # generate all the possible paths from source to destination for all source to all destination
#        # Find all paths for {(host1,host2) \in hostList \times hostList \setminus (host,host)}
#        # Use encoding technique of bin(source._id)+bin(destination.id)+indexOfPath
#        
#        indexOfPath                                     = list(range(0, numpaths))
#        #loop for indexOfPath
#        self.sourceDestinationDictionary[sourceDestination._id].pathList[indexOfPath].sourceToEdge           = self.findSourceToEdgeLink(source)
#        self.sourceDestinationDictionary[sourceDestination._id].pathList[indexOfPath].edgeToAgg 			= self.findEdgeToAggLink(source, indexOfPath)
#        self.sourceDestinationDictionary[sourceDestination._id].pathList[indexOfPath].aggToCore 			= self.findAggToCoreLink(source, indexOfPath)
#
#        self.sourceDestinationDictionary[sourceDestination._id].pathList[indexOfPath].coreToAgg 			= self.findCoreToAggLink(destination)
#        self.sourceDestinationDictionary[sourceDestination._id].pathList[indexOfPath].aggToEdge 			= self.findAggToEdgeLink(destination)
#        self.sourceDestinationDictionary[sourceDestination._id].pathList[indexOfPath].edgeToDestination 	     = self.findEdgeToDestinationLink(destination)          
        sourceEdgeLink  = self.findSourceToEdgeLink(sourceDestination.source)
        edgeAggLink     = self.findEdgeToAggLink(sourceDestination.source, pathId)
        aggCoreLink     = self.findAggToCoreLink(sourceDestination.source, pathId)
        coreAggLink     = self.findCoreToAggLink(sourceDestination.destination)
        aggEdgeLink     = self.findAggToEdgeLink(sourceDestination.destination)
        edgeDestLink    = self.findEdgeToDestinationLink (sourceDestination.destination)
        newPath = Path(sourceDestination._id, pathId, sourceEdgeLink, edgeAggLink, aggCoreLink, coreAggLink, aggEdgeLink, edgeDestLink)
        return newPath
    
    def findSourceToEdgeLink(self, source):
        return source._id
        # As per the indexing the source id will be the link id
        
    
    def findEdgeToAggLink(self, source, indexOfPath):
        return None 
        # Find the link between edge and agg, this depends on the source and random path available
        # Find the link between edge and agg, this depends on the random path available
    def findAggToCoreLink(self, source, indexOfPath):
        return None
    		
    def findCoreToAggLink(self, destination):
        return None
        # Find the link between core and agg, this depends on the destination
    
    def findAggToEdgeLink(self, destination):
        return None
        # Find the link between agg and host, this depends on the destination
    
    def findEdgeToDestinationLink(self, destination):
        # As per the indexing the destination id will br the link id
        return destination._id
    
    def findPathID(self, _typePath, sourceDestination = 0, lastPathList = []):
    
        # We have to run 
        # populateHosts(),populateSourceDestination() populateEdges(), populateAgg(), populateEdges(), populateLinks() and populateAllPaths() to run this 
        # Find the id corresponding to the 6 links found out and return the pathid
        # We can assign typeOfPathSelection in 3 ways
            # 0 Random : use indexOfRandomPath
            # 1 Round Robin
            # 2 Load Aware
        if(_typePath == 0):
            # Search over sourceDestination and pathList to return pathID using indexOfRandomPath
            return random.sample(range(self.numPaths),1)
            
        elif( _typePath == 1):
            # Use lastPathList and sourceDestination to return the next path in pathList
            return 0
            
        elif(_typePath == 2):
            # Load Aware and return the path with least congestion
            return 0
        
    def plotTopology(self):
        # Run this to visualize the graph with given number of port
        return 0