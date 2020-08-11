import random
from scipy.stats import pareto

class LifeTime:

    def __init__(self, isMice, mean, shift):
        self.isMice = isMice
        self.mean   = mean
        self.shift  = shift
    
    def __repr__(self):
        return '<LifeTime isMice: %s, mean: %s, shift: %s\n>' %(self.isMice, self.mean, self.shift)


class ShiftedExponentialLifeTime(LifeTime):

    def __init__(self, isMice, mean, shift):
        LifeTime.__init__(self, isMice, mean, shift)
        self.rate   = 1.0/(self.mean-self.shift)
	
	def __repr__(self):
		return '%s \n <ShiftedExponentialLifeTime rate: %s\n>' %(LifeTime.__repr__(self), self.rate)

    def getDuration(self):
        return self.shift+random.expovariate(self.rate)
    
    
class ShiftedParetoLifeTime(LifeTime):

    def __init__(self, isMice, mean, shift = 0):
        LifeTime.__init__(self, isMice, mean, shift)
        self.rate   = 1.0/(self.mean)
        self.shape  = self.mean/(self.mean - self.shift)
        
	def __repr__(self):
            return '%s \n <ParetoLifeTime rate: %s, shape: %s\n>' %(LifeTime.__repr__(self), self.rate, self.shape)

    def getDuration(self):
        return self.shift+pareto.rvs(self.shape)
