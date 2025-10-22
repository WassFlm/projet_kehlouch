from abc import ABC,abstractmethod
from typing import override, TypeAlias, List
from Parameters import RealParameter, IntParameter
import numpy as np


number: TypeAlias = float | int


class MathFunction(ABC):
    def __init__(self,name:str, details:str, description:str):
        self.__name = name
        self.__description = description
        self.__details = details
        self.a = RealParameter(*RealParameter.params_specs["canonical"]["a"])
        self.b = RealParameter(*RealParameter.params_specs["canonical"]["b"])
        self.h = RealParameter(*RealParameter.params_specs["canonical"]["h"])
        self.k = RealParameter(*RealParameter.params_specs["canonical"]["k"])
        self._parameters: List[RealParameter] = [self.a, self.b, self.c, self.d]


    @abstractmethod
    def process(self,x: number) -> number:
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

    @property
    def parameters(self):
        return self._parameters



class TrigFunction(MathFunction, ABC):

    __trig_name: str =  ""

    # forme : f(x) = a * trg*(b*(x - h)) + k | trg -> fonction trigo

    def __init__(self):
        super().__init__()

    @override
    def process(self, x: number) -> number:
        trg = self.__trig_name
        a, b, h, k = [i for i in self._parameters]
        return a * trg*(b*(x - h)) + k





class BaseExpoFunction(MathFunction, ABC):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def process(self, x: number) -> number:
        return
    




class PolyFunction(MathFunction, ABC):
    param_specs = [ 
        ("n","Degré","Degré de la fonction", 0, 5, 2),
        ("ai","Coefficients","Coefficient des variables", -5.0, 5.0, 1.0)
    ]
    
    # form : f(x) = a*x**n + b*x**n-1 + ... + z*x**0

    def __init__(self):
        super().__init__()

        self.n = IntParameter(*self.param_specs[0]) 
        self.coeffs_list: list[RealParameter] = []
        self._update_coeffs()

    def _update_coeffs(self):
        degree = self.n.value

        self.coeffs_list = [] #reset la liste pour pas que ca s'ajoute par dessus les autres
        for i in range(degree, -1, -1):
            coeff_specs = (f"a{i}", f"Coefficient a{i}", f"Coefficient de x^{i}", -5.0, 5.0, 1.0)
            param = RealParameter(*coeff_specs)
            self.coeffs_list.append(param)
        
    @override
    def process(self, x: number) -> number:
        values = [param.value for param in self._coeffs_list]
        poly = np.poly1d(values)
        return poly(x)


# def RationalFunction(MathFunction)

# def AbsoluteValueFunction(MathFuntion)

# def etc...