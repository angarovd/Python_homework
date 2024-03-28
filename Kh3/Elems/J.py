from Elems import elem_class

class J (elem_class.SuperClass):
    def __init__(self, el, h):
        super().__init__(el, h)
        self.current = el['Current']
        self.impedance = el['Impedance']
def set_current(self):
        return self.current
