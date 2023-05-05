from HardwareStore import HardwareStore
from UserFilter import UserFilter

class Main:
    data = HardwareStore()
    for i in range(0,10):
        data.addNew(data.createRandom())
    
    filter = UserFilter(data.base)
    filter.printbase()
    while filter.userHere:
        filter.askFilter()





