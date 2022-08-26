
import yaml



    
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
    
   

with open('./test_dict.yaml') as f:
    y = yaml.load(f, Loader=yaml.FullLoader)
    y= DotDict(y)
    
    # y.number1 = 'asd'
    # del y.number1
    
    print(y.number1)
    print(y.alphabet.aaa)
    print('----------------')
    print(y)
    print(y.number1)
    
    
























