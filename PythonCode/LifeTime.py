import random
from scipy.stats import pareto

class LifeTime:

    def __init__(self, mean, shift):
        self.mean   = mean
        self.shift  = shift
    
    def __repr__(self):
        return '< LifeTime mean: %s, shift: %s> \n' %(self.mean, self.shift)


class ShiftedExponentialLifeTime(LifeTime):

    def __init__(self, mean, shift):
        LifeTime.__init__(self, mean, shift)
        self.rate   = 1.0/(self.mean-self.shift)
	
    def __repr__(self):
        return '< ShiftedExponentialLifeTime mean: %s, shift: %s, rate: %s >' %(self.mean, self.shift, self.rate)

    def getDuration(self):
        return self.shift+random.expovariate(self.rate)
    
    
class ShiftedParetoLifeTime(LifeTime):

    def __init__(self, mean, shift = 0):
        LifeTime.__init__(self, mean, shift)
        self.rate   = 1.0/(self.mean)
        self.shape  = self.mean/(self.mean - self.shift)
        
    def __repr__(self):
        return '< ParetoLifeTime mean: %s, shift: %s, rate: %s, shape: %s >' %(self.mean, self.shift, self.rate, self.shape)

    def getDuration(self):
        return self.shift+pareto.rvs(self.shape)

