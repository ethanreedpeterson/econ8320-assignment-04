import pdb
class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imag)
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5
    
    def __lt__(self, other):
        if abs(self)<abs(other):
            return True
        else:
            return False
    def __gt__(self, other):
        if abs(self)>abs(other):
            return True
        else:
            return False
        
    def __eq__(self, other):
        if (self.real==other.real) & (self.imag==other.imag):
            return True
        else:
            return False
        
    def __ne__(self, other):
        return not self==other

mycn = ComplexNumber(2, 3)
othercn = ComplexNumber(3, 1)
#pdb.set_trace()
mycn > othercn
