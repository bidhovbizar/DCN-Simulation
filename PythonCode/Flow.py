from Path import Path
class Flow:

    def __init__(self,_id, sourceDestinationID, arrivalTime, path):
    
        self._id                    = _id
        self.sourceDestinationID    = sourceDestinationID
        self.arrivalTime            = arrivalTime

        self.path                   = path
                
    def __repr__(self):
         return '<Flow _id: %s, sourceDestinationID: %s, arrivalTime: %s,\n\
path: %s>' %(
            self._id, self.sourceDestinationID, self.arrivalTime,
            self.path)
           
class MiceFlow(Flow):
    
    def __init__(self, _id, sourceDestinationID, arrivalTime, path, miceParameters):
        Flow.__init__(self, _id, sourceDestinationID, arrivalTime, path)
        self.bandwidth      = miceParameters.bandwidth
        self.lifeTime       = miceParameters.lifeTime.getDuration()
        self.departureTime  = self.arrivalTime + self.lifeTime

    def __rept__(self):
        return '< MiceFlow ID: %s, sourceDestinationID: %s, pathID: %s, arrivalTime: %s,\n\
bandwidth: %s, lifeTime: %s, departureTime: %s>\n' %(
                                                    self._id, self.sourceDestinationID, self.path.pathID, self.arrivalTime,
                                                    self.bandwidth, self.lifeTime, self.departureTime)
        

class ElephantFlow(Flow):
    
    def __init__(self, _id, sourceDestinationID, arrivalTime, path, elephantParameters):
        Flow.__init__(self, _id, sourceDestinationID, arrivalTime, path)
        self.bandwidth      = elephantParameters.bandwidth
        self.lifeTime       = elephantParameters.lifeTime.getDuration()
        self.departureTime  = self.arrivalTime + self.lifeTime

    
    def __rept__(self):
        return '< ElephantFlow ID: %s, sourceDestinationID: %s, pathID: %s, arrivalTime: %s,\n\
bandwidth: %s, lifeTime: %s, departureTime: %s>\n' %(
                                                    self._id, self.sourceDestinationID, self.path.pathID, self.arrivalTime,
                                                    self.bandwidth, self.lifeTime, self.departureTime)