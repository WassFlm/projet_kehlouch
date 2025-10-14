class RealParameter(): 
    # TODO fill in data
    def __init__(self,symbol:str,name:str,description:str,min_value: float,max_value:float,default_value: float):
        self.__description = description
        self.__value = default_value
        pass
    def set_default_values(self):
        self.__value = self.__default_value 
    # getters/setters
    @property
    def description(self):
        return self.__description
    @property
    def value(self):
        return self.__value