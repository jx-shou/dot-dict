# dot-dict

Dot notation access to dictionary attributes.

print(key1.key2.key3)

```python
class DotDict(dict):     
    """dot notation access to dictionary attributes"""      
    def __getattr__(*args):         
        res = dict.get(*args)         
        return DotDict(res) if type(res) is dict else res 
    
    ### make dict read-only
    __setattr__ = None
    __delattr__ = None
    
    # __setattr__ = dict.__setitem__     
    # __delattr__ = dict.__delitem__ 
 ```
