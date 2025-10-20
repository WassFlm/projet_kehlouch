from abc import ABC,abstractmethod
from typing import override, TypeAlias, List
from real_parameters import RealParameter, IntParameter
import numpy as np


number: TypeAlias = float | int

# TODO : Mettre tout en forme canonique qui utilisent juste a, b, h, k

class MathFunction(ABC):
    def __init__(self,name: str,details: str,description: str):
        self.__name = name
        self.__description = description
        self.__details = details
        self._parameters: List[RealParameter]

    @abstractmethod
    def process(self,x: number) -> number:
        pass

    @abstractmethod
    def get_param(self,param_symbol: str)-> RealParameter:
        pass

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
    trig_name: str =  ""
    param_specs = [ 
        ("a","Amplitude","Facteur d'échelle vertical",-5.0,5.0,1.0),
        ("f","Fréquence","Facteur d'échelle horizontal",-5.0,5.0,1.0),
        ("p","Phase","Décalage horizontal",-2*np.pi,2*np.pi,0.0),
        ("o","Décalage vertical","Décalage vertical",-5.0,5.0,0.0)
    ]
    param_order = ['a','f','p','o']
    # form : f(x) = a * trg(fx + p) + o | trg -> fonction trigo
    def __init__(self, name, details, description):
        super().__init__(name, details, description)
        self._parameters = [RealParameter(*x) for x in self.param_specs]

    @override
    def get_param(self,param_symbol)-> RealParameter:
        return self._parameters[self.param_order.index(param_symbol)]
    
    @override
    def process(self,x: number) -> number:
        trg = getattr(np,self.trig_name)
        a = self.get_param('a').value
        f = self.get_param('f').value
        p = self.get_param('p').value
        o = self.get_param('o').value
        return a * trg(f*x + p) + o





class BaseExpoFunction(MathFunction, ABC):
    param_specs = [ 
        ("a","Coefficient","Facteur d'échelle vertical", -5.0, 5.0, 1.0),
        ("b","Base","Base de l'exposant", -5.0, 5.0, 1.0),
        ("c","c","Décalage vertical",-5.0, 5.0, 1.0),
    ]

    param_order = ['a','b','c']
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
    




class PolyFunction(MathFunction, ABC):
    param_specs = [ 
        ("n","Degré","Degré de la fonction", 0, 5, 2),
        ("a","Coefficients","Coefficient des variables", -5.0, 5.0, 1.0)
    ]
    
    # form : f(x) = a*x**n + b*x**n-1 + ... + z*x**0

    def __init__(self, name, details, description):
        super().__init__(name, details, description)

        self._n = IntParameter(*self.param_specs[0]) 

        self._coeffs_list: list[RealParameter] = []
        self._update_coeffs()

    def _update_coeffs(self):
        degree = self._n.value

        self._coeffs_list = []
        for i in range(degree, -1, -1):
            coeff_specs = (f"a{i}", f"Coefficient a{i}", f"Coefficient de x^{i}", -5.0, 5.0, 1.0)
            param = RealParameter(*coeff_specs)
            self._coeffs_list.append(param)

    @override
    def get_param(self, param_symbol: str) -> RealParameter:
        if param_symbol == "n":
            return self._n
        else:
            for param in self._coeffs_list:
                if param.symbol == param_symbol:
                    return param
        
    @override
    def process(self, x: number) -> number:
        coeffs = [param.value for param in self._coeffs_list]
        poly = np.poly1d(coeffs)
        return poly(x)
