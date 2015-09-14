
class Descriptor:
    def __get__(self, obj, objtype=None): 
        raise AttributeError("Unreadable attribute!")
    def __set__(self, obj, value):
        raise AttributeError("Unsetable attribute!")
    def __delete__(self, obj): 
        raise AttributeError("Undeletable attribute!")

# implemented with accumulator to reduce list cutting
def _cascade(foos, args=tuple(), kwargs=dict(), foo_idx = 0): 
    if len(foos)==foo_idx+1:
        return foos[foo_idx](*args, **kwargs)
    def continuation():
        return _cascade(foos, args, kwargs, foo_idx+1)
    return foos[foo_idx](continuation, *args, **kwargs)

class HookableDescriptor(Descriptor):
    def __init__(self, descriptor=None, at_get=[], at_set=[], at_del=[]):
        self.descriptor = descriptor or Descriptor()
        self.at_get = at_get
        self.at_set = at_set
        self.at_del = at_del
    
    def __get__(self, obj, objtype):
        return _cascade(self.at_get + [ self.descriptor.__get__ ], (obj, objtype))
    
    def __set__(self, obj, value):
        return _cascade(self.at_set + [ self.descriptor.__set__ ], (obj, value))
        
    def __delete__(self, obj):
        return _cascade(self.at_del + [ self.descriptor.__delete__ ], (obj, ))

class BackedProperty(Descriptor):
    def __init__(self, val = None):
        self.value = val
    
    def __get__(self, obj, objtype=None):
        return self.value
        
    def __set__(self, obj, value):
        self.value = value

def HookableBackedProperty(val):
    return HookableDescriptor(BackedProperty(val))

def 
