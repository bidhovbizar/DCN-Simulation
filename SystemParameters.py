class SystemParameters:

    def __init__(self, flowArrivalRate, _typeService ,probElephantFlow,
				 elephantBandWidth, miceBandwidth, elephantServiceShift, 
				 elephantServiceMean, miceServiceShift, miceServiceMean,
				 numPorts, hostList, connectivityMatrix):
        self.flowArrivalRate        = flowArrivalRate #arrivalRate of the flows
        # Push to global Variable
        self.numFlows               = 0
        
        self._typeService			= _typeService
        	
        self.probElephantFlow       = probElephantFlow
        self.elephantBandWidth      = elephantBandWidth
        self.elephantServiceShift   = elephantServiceShift
        self.elephantServiceMean    = elephantServiceMean
        
        self.miceBandwidth          = miceBandwidth
        self.miceServiceShift       = elephantServiceShift
        self.miceServiceMean        = elephantServiceMean
        
        self.connectivityMatrix     = connectivityMatrix

    def __repr__(self):
        return  '<SystemParameters flowArrivalRate: %s, \n\
                numFlows: %s, \n\
                _typeService: %s, \n\
                probElephantFlow: %s, elephantBandWidth: %s, elephantServiceShift: %s, elephantServiceMean: %s\n\
                miceBandwidth: %s, miceServiceShift: %s, miceServiceMean: %s\n\
                connectivityMatrix: %s\n>' %(
                self.flowArrivalRate,
                self.numFlows,
                self._typeService,
                self.probElephantFlow, self.elephantBandWidth, self.elephantServiceShift, self.elephantServiceMean,
                self.miceBandwidth, self.miceServiceShift, self.miceServiceMean,
                self.connectivityMatrix)