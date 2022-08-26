# dot-dict

Dot notation access to dictionary attributes.

```python
class DotDict(dict):        
    def __getattr__(*args):         
        res = dict.get(*args)         
        return DotDict(res) if type(res) is dict else res 
    
    ### make dict read-only
    __setattr__ = None
    __delattr__ = None
    
    # __setattr__ = dict.__setitem__     
    # __delattr__ = dict.__delitem__ 
 ```
