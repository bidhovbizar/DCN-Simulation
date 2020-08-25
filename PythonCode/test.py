sourceDestinationDictionary = {}
from SourceDestination import SourceDestination
for source in range(16):
    for dest in range(16):
        if( source == dest):
            continue
        sourceDestId        = str(source) + ':' + str(dest)
        newSourceDestPair   =  SourceDestination(sourceDestId, source, dest)
        sourceDestinationDictionary.update({ sourceDestId : newSourceDestPair })
        
        