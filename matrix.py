import builtins

class Matrix(object):
    """ 
    Read the matrix and store as part of the class object
    """
    def __init__(self, value = [], dim=(1,1)):            
        if isinstance(value, list):
            if builtins.len(value)>0:
                if isinstance(value[0], (int, float)):
                    row = (int, float)
                else:
                    row = type(value[0])
                for i in value:
                    if not isinstance(i, (int, float, list)):
                        raise RuntimeError("Matrix is invalid. Please ensure that all elements share a type.")
                if row is list:
                    lenInner = builtins.len(value[0])
                    for i in value:
                        if builtins.len(i) != lenInner:
                            raise RuntimeError("Matrix is invalid. Please ensure that all rows have uniform length.")
                        for j in i:
                            if not isinstance(j, (int, float)):
                                raise RuntimeError("Matrix is invalid. Please ensure that all elements are numeric (either float or int).")
                self.value = value
                try:
                    self.shape = (builtins.len(value), builtins.len(value[0]))
                except Exception:
                    self.shape = (builtins.len(value), 1)
            else:
                matrix = [[1 for _ in range(dim[1])] for _ in range(dim[0])]
                self.value = matrix
                self.shape = dim
        else:
            matrix = [[1 for _ in range(dim[1])] for _ in range(dim[0])]
            self.value = matrix
            self.shape = dim
    """
    Print the matrix to screen
    """           
    def __repr__(self):
        string = "  "
        for i in range(self.shape[0]):
            if self.shape[1]>1:
                if i < self.shape[0]-1:
                    string += "[ "
                    for j in range(self.shape[1]):
                        string += str(self.value[i][j]) + " "
                    string += "]\n  "
                else:
                    string += "[ "
                    for j in range(self.shape[1]):
                        string += str(self.value[i][j]) + " "
            else:
                if self.shape[0]==1:
                    string += "[ "
                if i < self.shape[0]-1:
                    if self.shape[1]>1:
                        string += "[ "
                    string += str(self.value[i]) + "\n  "
                else:
                    string += str(self.value[i]) + " "
        if self.shape[1]>1:
            string += "]\n\n"
        return string
