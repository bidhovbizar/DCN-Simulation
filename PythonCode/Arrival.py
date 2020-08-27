import random
from scipy.stats import pareto

class Arrival:
    
    def __init__(self, rate):
        self.rate   = rate
    
    def __repr__(self):
        return '< Arrival rate: %s >' %(self.rate)
    
    
class ExponentialArrival(Arrival):
    
    def __init__(self, rate):
        Arrival.__init__(self, rate)
        self.mean   = 1.0/(self.rate)
        
    def __repr__(self):
        return '< ExponentialArrival rate: %s, mean: %s>' %(self.rate, self.mean)
    
    def getDuration(self):
        return random.expovariate(self.rate)

class ParetoArrival(Arrival):
    def __init__(self, rate, shift = 0):
        Arrival.__init__(self, rate)
        self.mean   = 1.0/(self.rate)
        self.shift  = shift
        self.shape  = self.mean/(self.mean - self.shift)
	
    def __repr__(self):
        return '< PareoArrival rate: %s, mean: %s, shift: %s, shape: %s>' %(self.rate, self.mean, self.shift, self.shape)
    
    def getDuration(self):
        return self.shift+pareto.rvs(self.shape)