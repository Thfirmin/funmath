import math

class Matrix:
    _able_types = (int, float)
    row = 0
    col = 1

    # Built-in Methods
    def __init__(self, data: list[int | float] = [], dtype: type = int):
        self.clear()
        self._init_matrix(data, dtype)
        self._assert(self._assert_metadata(), ValueError("Invalid matrix metadata"))

    def __repr__(self):
        ret = f"Matrix({id(self)}):\n"
        ret += f"\tdata: {self._data}\n"
        ret += f"\tcolpad: {self._colpad}\n"
        ret += f"\tshape: {self._shape}\n"
        ret += f"\tdtype: {self._dtype}\n"
        ret += f"\tsize: {self._size}\n"
        return ret

    def __str__(self):
        ret = "┌" + ((sum(self._colpad) + (len(self._colpad) + 1)) * ' ') + "┐\n"
        for idx in range(self._shape[self.row]):
            rang = idx * self._shape[self.col]
            arr = self._data[rang:rang + self._shape[self.col]]
            ret += "│ " + " ".join([str(arr[i]).center(self._colpad[i]) for i in range(self._shape[self.col])]) + " │\n" 
            #ret += "│ " + " ".join([str(arr[i]).center(self._colpad[i]) for i in range(len(self._colpad))]) + " │\n" 
        ret += "└" + ((sum(self._colpad) + (len(self._colpad) + 1)) * ' ') + "┘\n"
        return ret
        
    # Constructors
    @staticmethod
    def default():
        return Matrix()

    @staticmethod
    def zero(shape: tuple):
        shape = tuple(shape)
        return Matrix([[0 for j in range(shape[Matrix.col])] for i in range(shape[Matrix.row])])

    # Methods
    def clear(self) -> None:
        self._data: list[int | float] = []
        self._colpad: list[int] = []
        self._size: int = 0
        self._shape: tuple = (0, 0)

    def resize(self, shape: tuple):
        shape = tuple(shape)
        self._assert(len(shape) == 2, ValueError("Matrix are 2D"))
        self._assert(self._size == math.prod(shape), ValueError("Invalid new shape"))
        self._shape = shape
        self._colpad = self._get_colpad()

    def retype(self, dtype):
        self._dtype = self._get_type(dtype)
        self._data = [self._dtype(elem) for elem in self._data]
        
    # Getters / Setters
    @property
    def data(self):
        return self._data

    @property
    def shape(self):
        return self._shape

    @property
    def size(self):
        return self._size

    @property
    def colpad(self):
        return self._colpad
        
    # Private Methods
    def _data_validation(self, data: list[list[int | float]], dtype: type) -> tuple:
        rows = len(data)
        if rows == 0:
            return (0, 0)
        fixed_cols = len(data[0])
        for arr in data:
            self._assert(type(arr) is list, ValueError("Invalid matrix structure"))
            wrong_columns = len([elem for elem in arr if (type(elem) is not dtype)])
            self._assert(wrong_columns == 0, ValueError("Invalid matrix data type"))
            self._assert(fixed_cols == len(arr), ValueError("Invalid matrix column size"))
        return (rows, fixed_cols)

    def _init_matrix(self, data: list[int | float], dtype: type):
        self._dtype = self._get_type(dtype)
        self._shape = self._data_validation(data, dtype)
        self._size = math.prod(self._shape)
        if self._size > 0:
            for arr in data:
                self._data += arr
        self._colpad = self._get_colpad()

    def _get_type(self, dtype: type):
        typ = dtype if dtype in self._able_types else None
        if (typ is None):
            raise ValueError(f"dtype need to be one of {self._able_types}")
        return typ

    def _get_colpad(self) -> None:
        if self._size == 0:
            return []
        return [len(str(max(self._data[i::self._shape[self.col]]))) for i in range(self._shape[self.col])]

    def _assert_metadata(self) -> bool:
        if (self._size != len(self._data)):
            return False
        if (self._size != math.prod(self._shape)):
            return False
        if (len(self._shape) != 2):
            return False
        return True

    def _assert(self, expr: bool, ex):
        if (not expr):
            raise ex
