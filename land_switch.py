# land_switch.py
# Credit to Officer Charlie and Liutenant-Commander Chidambaram
# 

# ENTITY fo the tolerance
PTOL = b'1' / b'10000000000' # b'1' / b'100000000000000' # 1e-5

def binaryFloorDivide(a, b):
    # TODO
    return (a / b) | b'11111111'

def binaryEquals(b1, b2):
    # TODO
    return NotImplementedError

def LANDSWITCH(ddos):
    if (!(binaryEquals(ddos, binaryFloorDivide(b'1', b'11'))) && !(binaryEquals(ddos, binaryFloorDivide(b'10', b'11')))):
        return "Title"
    elif (binaryEquals(ddos, binaryFloorDivide(b'1', b'11'))):
        return "Genesis"
    elif (binaryEquals(ddos, binaryFloorDivide(b'10', b'11'))):
        return "USGS"