# imports
from abc import ABC,abstractmethod
from typing import override, TypeAlias, List
from real_parameters import RealParameter, IntParameter
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



class BaseExpoFunction(MathFunction, ABC):
    param_specs = [ 
        # static data, should be on a different file for organization purposes
        ("a","Coefficient","Facteur d'échelle vertical", -5.0, 5.0, 1.0),
        ("b","Base","Base de l'exposant", -5.0, 5.0, 1.0),
        ("c","c","Décalage vertical",-5.0, 5.0, 1.0),
    ]

    param_order = ['a','b','c'] # defines order of the parameters (a is first, f second..)
    # form : f(x) = a * b**x + c

    def __init__(self, name, details, description):
        super().__init__(name, details, description)

        self._parameters = [RealParameter(*x) for x in self.param_specs]

    @override
    def get_param(self,param_symbol)-> RealParameter:
        return self._parameters[self.param_order.index(param_symbol)]
    
    @abstractmethod
    def process(self,x: number) -> number:
        return
    

class ExpoFunction(BaseExpoFunction):
    def __init__(self):
        super().__init__("Exponential", "details", "description")

    @override
    def process(self, x: number) -> number:
        a = self.get_param('a').value
        b = self.get_param('b').value
        c = self.get_param('c').value
        return a * b**x + c


class PolyFunction(MathFunction, ABC):
    param_specs = [ 
        # static data, should be on a different file for organization purposes
        ("n","Degré","Degré de la fonction", 0, 5, 2),
        ("a","Coefficients","Coefficient des variables", -5.0, 5.0, 1.0)
    ]
    
    def __init__(self, name, details, description):
        super().__init__(name, details, description)

        self._n = IntParameter(*self.param_specs[0]) 

        self._a: list[RealParameter] = []
        self._update_coeffs()

    def _update_coeffs(self):
        degree = self._n.value

        self._a = []
        for i in range(degree, -1, -1):
            coeff_specs = (f"a{i}", f"Coefficient a{i}", f"Coefficient de x^{i}", -5.0, 5.0, 1.0)
            param = RealParameter(*coeff_specs)
            self._a.append(param)

    @override
    def get_param(self, param_symbol: str) -> RealParameter:
        if param_symbol == "n":
            return self._n
        else:
            for param in self._a:
                if param.symbol == param_symbol:
                    return param
        
    @override
    def process(self, x: number) -> number:
        coeffs = [param.value for param in self._a]
        poly = np.poly1d(coeffs)
        return poly(x)
    

class QuadFunction(PolyFunction):
    def __init__(self):
        super().__init__("Quadratic Funtion", "details", "the description of a quad function is ..")

# usage exemple
f = SinFunction()


print(f.description) # get a description of a function (sin)

print(f.get_param('a').description) # get a description of a specified parameter

print(f.process(np.pi/2)) # process a value


e = ExpoFunction()
print(e.process(2))

quad = QuadFunction()
print(quad.process(10))