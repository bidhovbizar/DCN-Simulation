class Flow:

    def __init__(self,_id, sourceDestinationID, arrivalTime, path):
    
        self._id                    = _id
        self.sourceDestinationID    = sourceDestinationID
        self.arrivalTime            = arrivalTime

        self.path                   = path
                
    def __repr__(self):
         return '<Flow _id: %s, sourceDestinationID: %s, pathID: %s, arrivalTime: %s,\n\
                 path: %s>' %(
                self._id, self.sourceDestinationID, self.pathID, self.arrivalTime,
                self.path)
           
class MiceFlow(Flow):
    
    def __init__(self, _id, sourceDestinationID, arrivalTime, path, miceParameters):
        Flow.__init__(self, _id, sourceDestinationID, arrivalTime, path)
        self.bandwidth      = miceParameters.bandwidth
        self.lifeTime       = miceParameters.lifeTime.getDuration()
        self.departureTime  = self.arrivalTime + self.lifeTime

    def __rept__(self):
        return '%s\n\
                <MiceFlow bandwidth: %s, lifeTime: %s, departureTime: %s\n>' %(
                Flow.__repr__(self),
                self.bandwidth, self.lifeTime, self.departureTime)
        

class ElephantFlow(Flow):
    
    def __init__(self, _id, sourceDestinationID, arrivalTime, path, elephantParameters):
        Flow.__init__(self, _id, sourceDestinationID, arrivalTime, path)
        self.bandwidth      = elephantParameters.bandWidth
        self.lifeTime       = elephantParameters.lifeTime.getDuration()
        self.departureTime  = self.arrivalTime + self.lifeTime

    def __rept__(self):
        return '%s\n\
                ElephantFlow bandwidth: %s, lifeTime: %s, departureTime: %s\n>' %(
                Flow.__repr__(self),
                self.bandwidth, self.lifeTime, self.departureTime)
        
