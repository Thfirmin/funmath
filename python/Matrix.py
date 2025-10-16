import math

class Matrix:
    # Built-in Methods
    __init__(self, m = 0, n = 0, data = []):
        self._data = []
        self._colpad = []
        self._m = m
        self._n = n
        
    # Methods
    def clear(self) -> None:
        self._data.clear()
        self._colpad.clear()
        self._m = 0
        self._n = 0

    def init_matrix(self, data: list[list[int | float]]) -> None:
        self._assert_matrix(data):
        
        self.clear()
        
        self._m = len(data)
        if self._m > 0:
            self._n = len(data[0])
            self._colpad = [0 for i in range(self._n)]

        for line in data:
            self._data.append(line.copy())
            new_colpad = [len(str(elem)) for elem in line]
            self._colpad = [max(new_len, old_len) for new_len, old_len in zip(new_colpad, self._colpad)]
    
    def init_sized(self, m: int, n: int) -> None:
        self._assert_msize(m)
        self._assert_msize(n)

    # Getters / Setters
    @property
    def data(self):
        return self._data
        
    @data.setter
    def data(self, mtrix: list[list[int | float]]) -> None:
        if not self._assert_matrix(mtrix):
            raise AssertionError("Invalid matrix data: different line sizes")
        self._m = len(mtrix)
        if self._m > 0:
            self._n = len(mtrix[0])
        
    # Private Methods
    def _assert_matrix(mtrix: any) -> bool:
        if not (type(mtrix) is list):
            return False
        if (not len(mtrix)):
            return True
        fixed_len = len(mtrix[0])
        for arr in mtrix:
            if (len(arr) != fixed_len):
                return False
            if (len(filter(lambda i: not (type(i) in (int, float)), arr) > 0)):
                return False
                
    def _assert_msize(size: any) -> bool:
        if not (type(size) is int):
            return False
        return size > 0