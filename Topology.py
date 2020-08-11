from Path import Path
from Link import Link
from Node import Node
from Host import Host
from HostEdgeLink import HostEdgeLink
from EdgeHostLink import EdgeHostLink
from EdgeAggregationLink import EdgeAggregationLink
from AggregationEdgeLink import AggregationEdgeLink
from AggregationCoreLink import AggrgeationCoreLink
from CoreAggregationLink import CoreAggregationLink
from SourceDestination import SourceDestination

class Topology:
    def __init__(self):
        #Something

    def __repr__(self):
        return '<Topology>'
    
class FatTreeTopology(Topology):
       
    def __init__(self, numPorts = 4):
        self.numPorts                   = numPorts
        
        self.numHosts                   = self.findNumHosts(self.numPorts)
        self.numEdges                   = self.findNumEdges(self.numPorts)
        self.numAggregations            = self.findNumAggregations(self.numPorts)
        self.numCores                   = self.findNumCores(self.numPorts)
        self.numSourceDestinationPair   = self.findNumSourceDestinationPair(self.numHosts)
        self.numPaths                   = self.findNumPaths(self.numPort)
        
        
        # Nodes
        self.hostList                   = self.populateHosts(self.numHosts) 
        self.edgeList                   = self.populateEdges(self.numEdges)
        self.aggregationList            = self.popluateAggregations(self.numAggregations)
        self.coreList                   = self.populateCores(self.numCores)
        
        # Links
        self.hostEdgeLinks			    = self.populateLinks(self.hostList, self.edgeList, _type = 0)
        self.edgeAggregationLinks       = self.populateLinks(self.edgeList, self.aggregationList, _type = 1)
        self.aggregationCoreLinks       = self.populateLinks(self.aggregationList, self.coreList, _type = 2)
        self.coreAggregationLinks       = self.populateLinks(self.coreList, self.aggregationList, _type = 2)
        self.aggregationEdgeLinks       = self.populateLinks(self.aggregationList, self.edgeList, _type = 1)
        self.edgeHostLinks              = self.populateLinks(self.edgeList, self.hostList, _type = 0)
        
        # Source Destination and its correspoding Paths
        self.sourceDestinationList      = self.populateSourceDestination(self.hostList)
       
        
    def __repr__(self):
        return '%s\n <FatTreeTopology NumPorts: %s,\n\
                NumHosts: %s, NumEdges: %s, NumAggregations: %s, NumCores: %s, NumPath: %s,\n\
                # Hosts in HostList: %s,\n\
                # Edges in EdgeList: %s,\n\
                # Aggregations in AggregationList: %s,\n\
                # Cores in CoreList: %s,\n\
                # Links in HostEdgeLinks: %s,\n\
                # Links in EdgeAggregationLinks: %s,\n\
                # Links in AggregationCoreLinks: %s,\n\
                # Links in CoreAggregationLinks: %s,\n\
                # Links in AggregationEdgeLinks: %s,\n\
                # Links in EdgeHostLinks: %s,\n\
                # Pairs of SourceDestination: %s\n>' %(
                Topology.__repr__(self),self.numPorts,
                self.numHosts, self.numEdges, self.numAggregations, self.numCores,
                len(self.hostList), len(self.edgeList), len(self.aggregationList), len(self.coreList),
                len(self.hostEdgeLinks), len(self.edgeAggregationLinks), len(self.aggregationCoreLinks),
                len(self.coreAggregationLinks), len(self.aggregationEdgeLinks), len(self.edgeHostLinks), 
                len(self.sourceDestinationList))

        
    def findNumHosts(self,numPorts):
        # calculate the number of Hosts connected in Fat-Tree Topology
        return numPorts * numPorts * numPorts/ 4

    def findNumEdges(self,numPorts):
        # return the number of edges in the Fat-Tree Topology
        return numPorts * numPorts * numPorts/ 2
    
    def findNumAggregations(self, numPorts):
        # return the number of aggregation in the Fat-Tree Topology
        return numPorts * numPorts * numPorts/ 2
    
    def findNumCores(self, numPorts):
        # return the number of core in the Fat-Tree Topology
        return numPorts * numPorts * numPorts/ 4
    
    def findNumSourceDestinationPair(self,numHost):
        # calculate the number of source destination Pair and return an integer
        return numHost * (numHost-1)

    def findNumPaths(self,numPorts):
        # calculate the number of paths for Fat Tree Topology
        return numPorts * numPorts / 4
    
    def populateHosts(self,numHosts):
        # return a list of Hosts with ID
        
    def populateEdges(self,numEdges):
        # return a list of Edges with ID
        
    def populateAggregation(self,numAggregations):
        # return a list of Aggregation with ID
        
    def populateCores(self,numCores):
        # return a list of Cores with ID
                
    def populateLinks(self, sourceLayer, destinationLayer, _type):
        if(_type == 0):
            # Use HostEdgeLink and EdgeHostLink
            # Creates link from Host to Edges indexed from 0 -> len(HostList)-1 to 0 to len(EdgeList)-1
            # Creates link from Edge to Host indexed from 0 -> len(EdgeList)-1 to 0 -> len(HostList)-1
            # Eg: hostToEdgeLink  = list(range(0,  self.numHosts ))
            
        elif(_type == 1):
            # Use EdgeAggregationLink and AggregationEdgeLink
            # Creates link from Edge to Aggregation from 0 -> len(edgeList) to 0 -> len(aggregationList)
            # Creates link from Aggregation to Edge from 0 -> len(aggregationList)  to 0 -> len(edgeList)
            # Eg: edgeToAggregationLink  = list(range(self.numHosts, ( 2* self.numHosts )))
            
        elif(_type == 2):
            # Use AggregationCoreLink and CoreAggregationLink
            # Creates link from Edge to Aggregation from 0 -> len(aggregationList) to 0 -> len(coreList)
            # Creates link from Aggregation to Edge from 0 -> len(coreList)  to 0 -> len(aggregationList)
            # Eg: aggregationCoreLinks = list(range((2*self.numHosts),(3*self.numHosts)))

    def populateSourceDestination(self, numHosts):
        # return a list of all source destination pair
        # "Source_id" + "Destination_id" + "j \in Path"
        # for every source find all the remaining destination and create sourceDestinationList by appending them
        
        # for every sourceDestination in sourceDestinationList populate the pathsList of object path and index from 0 to self.numpath-1
        # E.g. self.sourceDestinationList[i].pathList[j] = self.populateSourceDestinationPaths(soureDestination,self.numPaths)
        
    def populateSourceDestinationPaths(self,sourceDestination,numPaths):
        # generate all the possible paths from source to destination for all source to all destination
            # Find all paths for {(host1,host2) \in hostList \times hostList \setminus (host,host)}
            # Use encoding technique of bin(source._id)+bin(destination.id)+indexOfPath
            
            indexOfPath                                     = list(range(0, numpaths))
            #loop for indexOfPath
            self.sourceDestinationList[sourceDestination._id].pathList[indexOfPath].sourceToEdge                = self.findSourceToEdgeLink(source)
            self.sourceDestinationList[sourceDestination._id].pathList[indexOfPath].edgeToAggregation 			= self.findEdgeToAggregationLink(source, indexOfPath)
            self.sourceDestinationList[sourceDestination._id].pathList[indexOfPath].aggregationToCore 			= self.findAggregationToCoreLink(source, indexOfPath)

            self.sourceDestinationList[sourceDestination._id].pathList[indexOfPath].coreToAggregation 			= self.findCoreToAggregationLink(destination)
            self.sourceDestinationList[sourceDestination._id].pathList[indexOfPath].aggregationToEdge 			= self.findAggregationToEdgeLink(destination)
            self.sourceDestinationList[sourceDestination._id].pathList[indexOfPath].edgeToDestination 			= self.findEdgeToDestinationLink(destination)
    
    def findSourceToEdgeLink(self,source):
        # As per the indexing the source id will be the link id
        return source._id
    
    def findEdgeToAggregationLink(self,source, indexOfPath):
        # Find the link between edge and aggregation, this depends on the source and random path available
        # Find the link between edge and aggregation, this depends on the random path available
    		
    def findAggregationToCoreLink(self,source,indexOfPath):
        # Find the link between aggregation and core, this depends on the source andrandom path available
    		
    def findCoreToAggregationLink(self,destination):
        # Find the link between core and aggregation, this depends on the destination
    
    def findAggregationToEdgeLink(self,destination):
        # Find the link between aggregation and host, this depends on the destination
    
    def findEdgeToDestinationLink(self,destination):
        # As per the indexing the destination id will br the link id
        return destination._id
    
    def findPathID(self,_typePath, sourceDestination = 0, lastPathList = [])
        # We have to run 
        # populateHosts(),populateSourceDestination() populateEdges(), populateAggregation(), populateEdges(), populateLinks() and populateAllPaths() to run this 
        # Find the id corresponding to the 6 links found out and return the pathid
        # We can assign typeOfPathSelection in 3 ways
            # 0 Random : use indexOfRandomPath
            # 1 Round Robin
            # 2 Load Aware
        if(_type == 0):
            # Search over sourceDestination and pathList to return pathID using indexOfRandomPath
            return random.sample(range(self.numPaths),1)
            
        elif( _type == 1):
            # Use lastPathList and sourceDestination to return the next path in pathList
            
        elif(_type == 2):
            # Load Aware and return the path with least congestion
        
    def plotTopology(self):
        # Run this to visualize the graph with given number of port
