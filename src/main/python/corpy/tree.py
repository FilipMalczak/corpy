from collections import defaultdict

EMPTY_VALUE = object()

class Tree:
    empty = object()

    def __init__(self, value=EMPTY_VALUE):
        self.value = value
        self.children = defaultdict(Tree)
    
    def __getitem__(self, name):
        if isinstance(name, tuple):
            current = self
            for n in name:
                current = current.children[n]
            return current
        return self.children[name]
    
    def __call__(self):
        return self.value
    
    def __setitem__(self, name, val):
        self.children[name].value = val
        
