# LAND NORTH Of SAN GABRIEL MOUNTAINS tracking I-5 North
# land_switch.py
# Credit to Officer Charlie and Liutenant-Commander Chidambaram
# 

# ENTITY fo the tolerance
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
    return "float(" + str(a) + "/" + str(b) + ")"

def rationalIs(r):
    # (A / C) /  (B / C) ~= A / B
    global _MODULE_VALUEOF_A # the bits of the code are crows
    global _MODULE_VALUEOF_B # bit(accessing global variable in global function)
    return (int(r / PTOL) == int(((_MODULE_VALUEOF_A / PTOL) / (_MODULE_VALUEOF_B / PTOL))))

def LANDSWITCH(ddos):
    binaryFloorDivide(b'1', b'11')
    result_genesis = rationalIs(ddos)
    binaryFloorDivide(b'10', b'11')
    result_USGS = rationalIs(ddos)
    if ((!result_genesis) && (!result_USGS)):
        return "Title"
    elif result_genesis:
        return "Genesis"    
    elif result_USGS:
        return "USGS"

# Proof: rind tastes like tart