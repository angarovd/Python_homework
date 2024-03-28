from Elems import R
from Elems import EDS
from Elems import J
from Elems import C
from Elems import L

class Fabric():

    def serialize(elem, h):

        if elem['type'] == 'R':
            return Fabric.R(elem, h)

        if elem['type'] == 'E':
            return Fabric.E(elem, h)
        
        if elem['type'] == 'J':
            return Fabric.J(elem, h)

        if elem['type'] == 'C':
            return Fabric.C(elem, h)

        if elem['type'] == 'L':
            return Fabric.L(elem, h)

    def R(elem, h):
        return R.Resistance(elem, h)

    def E(elem, h):
        return EDS.EDS(elem, h)
    
    def J(elem, h):
        return J.J(elem, h)

    def C(elem, h):
        return C.C(elem, h)

    def L(elem, h):
        return L.L(elem, h)
