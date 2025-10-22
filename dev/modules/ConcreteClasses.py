from typing import override, TypeAlias
from AbstractClasses import TrigFunction, BaseExpoFunction, PolyFunction
import numpy as np


number: TypeAlias = float | int


class SinFunction(TrigFunction):
    _trig_name = "sin"
    def __init__(self):
        super().__init__("Sine Function", "details", "the description of a sine function is ..")




class ExpoFunction(BaseExpoFunction):
    def __init__(self):
        super().__init__("Exponential", "details", "description")

    @override
    def process(self, x: number) -> number:

        return 
    
# class LogFunction(BaseExpoFunction):
#     def __init__(self):
#         super().__init__("Log", "details", "description")

#     @override
#     def _process_func(self,x):
#         # calculer log selon x et la base
#         base = self.c.value
#         return np.log(x) / np.log(base)

class QuadFunction(PolyFunction):
    def __init__(self):
        super().__init__("Quadratic Funtion", "details", "the description of a quad function is ..")


