class SourceDestination:
    def __init__(self, _id, source, destination):
        self._id                = _id
        self.source             = source
        self.destination        = destination
        self.pathList           = []
        
    def __repr__(self):
        return '<SourceDestination _id: %s,\n\
source:%s,\ndestination: %s,\npathList: %s\n>' %(self._id, self.source, self.destination, self.pathList)

    def addPath(self, path):
        self.pathList.append(path)