from Node import Node
from Host import Host
from SourceDestination import SourceDestination

class Flow:
    def __init__(self,_id, sourceDestinationID, pathID, arrivalTime, isMice, lifeTime, bandWidth, path):
        self._id                    = _id
        
        self.sourceDestinationID    = sourceDestinationID
        self.pathID                 = pathID
        
        self.arrivalTime            = arrivalTime
        self.departureTime          = arrivalTime + lifeTime
        self.excessTime             = self.updateExcessTime(arrivalTime)

        self.isMice                 = isMice
        self.lifeTime               = lifeTime
        self.bandWidth              = bandWidth
            
    def __repr__(self):
         return '<Flow _id: %s, sourceDestinationID: %s, pathID: %s\n\
                arrivalTime: %s, departureTime: %s, excessTime: %s\n\
                isMice: %s, lifeTime: %s, bandwidth: %s, path: %s\n>' %(
                self._id, self.sourceDestinationID, self.pathID,
                self.arrivalTime, self.departureTime, self.excessTime,
                self.isMice, self.lifeTime, self.bandwidth,   self.path)


    def updateExcessTime(self, eventTime):
            self.eventTime  = eventTime
            self.excessTime = self.departureTime - self.eventTime
