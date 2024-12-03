#!/usr/bin/env python3


class Shoe:
    pass
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            error = "size must be an integer"
            print(error)
    
    def cobble(self):
        print('Your shoe is as good as new!')
        self.condition = "New"

    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, value):
        if isinstance(value, str):
            self._condition = value
        else:
            print('Condition must be a string')
        
    

