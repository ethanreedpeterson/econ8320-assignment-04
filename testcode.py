class Matrix(object):
    """
    Read the matrix and store as part of the class object
    """
    def __init__(self, value = [], dim=(1,1)):            
        if isinstance(value, list):
            if len(value)>0:
                if type(value[0]) is int or type(value[0]) is float:
                    row = (int, float)
                else:
                    row = type(value[0])
                for i in value:
                    if type(i) is not int and type(i) is not float and type(i) is not list:
                        raise RuntimeError("Matrix is invalid. Please ensure that all elements share a type.")
                if row is list:
                    lenInner = len(value[0])
                    for i in value:
                        if len(i) is not lenInner:
                            raise RuntimeError("Matrix is invalid. Please ensure that all rows have uniform length.")
                        for j in i:
                            if type(j) is not int and type(j) is not float:
                                raise RuntimeError("Matrix is invalid. Please ensure that all elements are numeric (either float or int).")
                self.value = value
                try:
                    self.shape = (len(value), len(value[0]))
                except Exception:
                    self.shape = (len(value), 1)
            else:
                matrix = []
                for i in range(dim[0]):
                        row = []
                        for j in range(dim[1]):
                            row.append(1)
                        matrix.append(row)
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


result = '  [ 4 6 1 9 10 12 1 7 ]\n  [ 1 2 3 4 5 6 7 8 ]\n  [ 19 0 3 1 10 15 -1 -1 ]\n\n'

matrixList = [[4,6,1,9,10,12,1,7],
        [1,2,3,4,5,6,7,8],
        [19,0,3,1,10,15,-1,-1]]

mat2 = Matrix(matrixList)

print(str(mat2)==result)