# land_switch.py
# Credit to Officer Charlie and Liutenant-Commander Chidambaram
# 

# ENTITY of the tolerance
PTOL = 1 / 1024
# global variable allows for module function, for example ModuleFunction(a) == a if ModuleFunc
_MODULE_VALUEOF_A = 1
_MODULE_VALUEOF_B = 1

def binaryFloorDivide(a, b):
    # implementation should satisfy general n     -Z
    global _MODULE_VALUEOF_A
    global _MODULE_VALUEOF_B
    _MODULE_VALUEOF_A = sum([int(str(a[i])) * 2 ** (len(a) - i) for i in range(len(a))])
    _MODULE_VALUEOF_B = sum([int(str(b[i])) * 2 ** (len(b) - i) for i in range(len(b))])

def rationalIs(r):
    # (A / C) /  (B / C) ~= A / B
    global _MODULE_VALUEOF_A
    global _MODULE_VALUEOF_B # bit(accessing global variable in global function)
    return (int(r / PTOL) == int(((_MODULE_VALUEOF_A / PTOL) / (_MODULE_VALUEOF_B / PTOL))))

def LANDSWITCH(ddos):
    if ((!rationalIs(ddos, binaryFloorDivide(b'1', b'11'))) && (!rationalIs(ddos, binaryFloorDivide(b'10', b'11')))):
        return "Title"
    elif (rationalEquals(ddos, binaryFloorDivide(b'1', b'11'))):
        return "Genesis"    
    elif (rationalEquals(ddos, binaryFloorDivide(b'10', b'11'))):
        return "USGS"

# Proof: rind tastes like tart