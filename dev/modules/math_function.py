# imports
from abc import ABC,abstractmethod
from typing import override, TypeAlias, List
from real_parameters import RealParameter
import numpy as np


number: TypeAlias = float | int

class MathFunction(ABC):
    def __init__(self,name: str,details: str,description: str):
        self.__name = name
        self.__description = description
        self.__details = details
        self._parameters: List[RealParameter]

    @abstractmethod # will be overriden by sub-classes
    def process(self,x: number) -> number:
        pass
    @abstractmethod
    def get_param(self,param_symbol: str)-> RealParameter:
        pass
    # getters setters
    # (read-only)
    @property
    def name(self):
        return self.__name
    @property
    def description(self):
        return self.__description
    @property
    def details(self):
        return self.__details


class TrigFunction(MathFunction,ABC):
    TRIG_NAME: str =  "" # overriden by sub-classes
    PARAM_SPECS = [ 
        # static data, should be on a different file for organization purposes
        ("a","Amplitude","Facteur d'échelle vertical",-5.0,5.0,1.0),
        ("f","Fréquence","Facteur d'échelle horizontal",-5.0,5.0,1.0),
        ("p","Phase","Décalage horizontal",-2*np.pi,2*np.pi,0.0),
        ("o","Décalage vertical","Décalage vertical",-5.0,5.0,0.0)
    ]
    PARAM_ORDER = ['a','f','p','o'] # defines order of the parameters (a is first, f second..)
    # form : f(x) = a * trg(fx + p) + o | trg is a trigonometric function 
    def __init__(self, name, details, description):
        super().__init__(name, details, description)
        
        # create the parameters according to PARAM_SPECS
        self._parameters = [RealParameter(*x) for x in self.PARAM_SPECS]
    @override
    def get_param(self,param_symbol)-> RealParameter:
        return self._parameters[self.PARAM_ORDER.index(param_symbol)]
    
    @override
    def process(self,x: number) -> number:
        trg = getattr(np,self.TRIG_NAME)
        # equivalant to:
        # np[self.TRIG_NAME](x) where TRIG_NAME is any trigonometric function from derived class
        a = self.get_param('a').value
        f = self.get_param('f').value
        p = self.get_param('p').value
        o = self.get_param('o').value
        return a * trg(f*x + p) + o

# Trig function definitions
class SinFunction(TrigFunction):
    TRIG_NAME = "sin" # so that parent classes will know which function to use
    def __init__(self):
        super().__init__("Sine Function", "details", "the description of a sine function is ..")

# it is that easy to create a new function
#class CosFunction(TrigFunction):
#    TRIG_NAME = "cos"
#    def __init__(self):
#        super.__init__("Cos function","my details","a description of cos function")


# usage exemple
f = SinFunction()
print(f.description) # get a description of a function (sin)

print(f.get_param('a').description) # get a description of a specified parameter

print(f.process(np.pi/2)) # process a value