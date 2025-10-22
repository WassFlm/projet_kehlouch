
class RealParameter(): 

    params_specs = {
        "canonical" : {
            "a" : ("a", "Coefficient a", "Facteur d'échelle vertical", -5.0, 5.0, 1.0),
            "b" : ("b", "Coefficient b", "Facteur d'échelle horizontal", -5.0, 5.0, 1.0),
            "h" : ("h", "Coefficient h", "Facteur de translation horizontale", -5.0, 5.0, 1.0),
            "k" : ("k", "Coefficient k", "Facteur de translation verticale", -5.0, 5.0, 1.0),
            "c" : ("c", "Base", "Base de l'exposant ou du logarithme", 0, 15.0, 10.0)
        },

        "other(math, etc... (plus tard))" : {

        }
    }
    
    def __init__(self, symbol:str, name:str, description:str, min_value:float, max_value:float, default_value:float):
        self.__symbol = symbol
        self.__name = name
        self.__description = description
        self.__min_value = min_value
        self.__max_value = max_value
        self.__default_value = default_value
        self.__value = default_value
        pass

    def set_default_values(self): #utile pour reset les valeurs plus tard ?
        self.__value = self.__default_value 

    # getters/setters
    @property
    def symbol(self):
        return self.__symbol
    
    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value : float):
        if value < self.__min_value:
            value = self.__min_value
        elif value > self.__max_value:
            value = self.__max_value
        self.__value = value

    @classmethod
    def parameters(cls, group, key):
        return cls(*cls.params_specs[group][key])

    
    

class IntParameter(): 
    
    params_specs = {
        "math??" : {
            "n" : ("n", "nb de rectangles / truc ds derviation", "description", -5, 5, 1)
        },

        "other(? (plus tard))" : {

        }
    }
    
    def __init__(self, symbol:str, name:str, description:str, min_value:int, max_value:int, default_value:int):
        self.__symbol = symbol
        self.__name = name
        self.__description = description
        self.__min_value = min_value
        self.__max_value = max_value
        self.__default_value = default_value
        pass

    def set_default_values(self):
        self.__value = self.__default_value

    # getters/setters
    @property
    def symbol(self):
        return self.__symbol
    
    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value : int):
        if value < self.__min_value:
            value = self.__min_value
        elif value > self.__max_value:
            value = self.__max_value
        self.__value = value

    @classmethod
    def parameters(cls, group, key):
        return cls(*cls.params_specs[group][key])
