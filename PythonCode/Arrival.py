import random
from scipy.stats import pareto

class Arrival:
    
    def __init__(self, mean):
        self.rate   = mean
    
    def __repr__(self):
        return '<Arrival mean: %s\n>' %(self.mean)
    
    
class ExponentialArrival(Arrival):
    
    def __init__(self, mean):
        Arrival.__init__(self, mean)
        self.rate   = 1.0/(self.mean)
        
    def __repr__(self):
        return ' %s \n <%s rate: %s\n>' %(Arrival.__repr__(self), ExponentialArrival.__class__, self.rate)
    
    def getDuration(self):
        return random.expovariate(self.rate)

class ParetoArrival(Arrival):
    def __init__(self, mean, shift = 0):
        Arrival.__init__(self, mean)
        self.rate   = 1.0/(self.mean)
        self.shift  = shift
        self.shape  = self.mean/(self.mean - self.shift)
	
    def __repr__(self):
        return ' %s \n <%s rate: %s, shift: %s, shape: %s\n>' %(Arrival.__repr__(self), ParetoArrival.__class__, self.rate, self.shift, self.shape)
    
    def getDuration(self):
        return self.shift+pareto.rvs(self.shape)