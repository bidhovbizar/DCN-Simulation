from SystemRandom import SystemRandom
import matplotlib.pyplot as plt
numFlows            = 2000

flowArrivalRate     = 20 
probElephantFlow    = 1

elephantBandwidth   = 10
elephantServiceShift = 0  
elephantServiceMean = 0.1
elephantServiceType = 1

miceBandwidth   = 1
miceServiceShift = 0
miceServiceMean = 1 
miceServiceType = 0
                 
hostEdgeBandwidth = 100
edgeAggBandwidth = 100 
aggCoreBandwidth = 100
coreAggBandwidth = 100
aggEdgeBandwidth = 100 
edgeHostBandwidth = 100

numPorts = 4

systemRandom    = SystemRandom(flowArrivalRate, probElephantFlow,
				 elephantBandwidth, elephantServiceShift, elephantServiceMean, elephantServiceType,
                 miceBandwidth, miceServiceShift, miceServiceMean, miceServiceType,
                 hostEdgeBandwidth, edgeAggBandwidth, aggCoreBandwidth, coreAggBandwidth, aggEdgeBandwidth, edgeHostBandwidth,
                 numPorts)

# To see the flows coming and leaving the system 
# Go to systemRandom and uncomment line 60 and 63. 
# OR 
# Look for print(str(self.numFlows) + ' : ' + str(len(self.activeFlowList))) within systemRandom.runSimulation(self,numFlows)
print("Initializing values \nStarting runSimulation")
systemRandom.runSimulation(numFlows)
print("Simulation Ended Successfully")

# Plot
systemRandom.linkUnderObservation

bandwidthOfLink = [systemRandom.linkUnderObservation.bandwidth] * len(systemRandom.linkEventTime)
y_pos   = systemRandom.linkEventTime
plt.figure(1)
plt.plot(y_pos, systemRandom.linkState, alpha=0.5, color='r', label='bandwidthUtilization')
plt.plot(y_pos, bandwidthOfLink, alpha=0.5, color='b', label='Linkbandwidth')


systemRandom.postProcessingLinkData()

bandwidthOfLink = [systemRandom.linkUnderObservation.bandwidth] * len(systemRandom.linkEventTime)
y_pos   = systemRandom.linkEventTime
plt.figure(2)
plt.plot(y_pos, systemRandom.linkState, alpha=0.5,color='r', label='bandwidthUtilization')
plt.plot(y_pos, bandwidthOfLink, alpha=0.5, color='b', label='Linkbandwidth')

plt.figure(1).savefig('observedLink.png')
plt.figure(2).savefig('observedLinkZoomed.png')