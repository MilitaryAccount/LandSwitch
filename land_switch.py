# LAND NORTH Of SAN GABRIEL MOUNTAINS tracking I-5 North
# land_switch.py illustrates the check of the IP ddos at head used to control the land (DAY OR NIGHT)
# Credit to Liutenant Charlie and Officer Chidambaram
# 

# understanding of binary to decimal conversion and finite representation tolerance in a specific base
d = 10
n = 2 ** d
PTOL = 1 / n
# global variable allows for functor, for example RationalFunctor(a) == "float(a)" if a is a decimal or fraction
# MODULE allows labeled datatypes as ModuleName(datavalue)
# FUNCTOR allows values as strings
_FUNCTOR_VALUEOF_A = 1
_FUNCTOR_VALUEOF_B = 1
_FUNCTOR_VALUEOF_C = 1
_FUNCTOR_VALUEOF_D = 1

def rationalDivide(a, b):
    # implementation should satisfy general b     -Z
    global _FUNCTOR_VALUEOF_A
    global _FUNCTOR_VALUEOF_B
    _FUNCTOR_VALUEOF_A = a
    _FUNCTOR_VALUEOF_B = b
    return "float(" + str(a) + "/" + str(b) + ")"

def ddosIs(bnum):
    global _FUNCTOR_VALUEOF_A # the bits of the code are crow("left") or crow("right") if windowCrowFlyby()
    global _FUNCTOR_VALUEOF_B # bit(accessing global variable in global function)
    global _FUNCTOR_VALUEOF_C
    global _FUNCTOR_VALUEOF_D
    global d#'
    # no Trees allowed, errors are allowed
    c_str = str(bnum) # format is b'[01]*'
    c_len = len(c_str) - 3
    c_val = 0
    i = 0
    while(i < min(c_len, d)):
        c_val += int(c_str[i+2]) * 2 ** (c_len-i-1)
        i += 1
    _FUNCTOR_VALUEOF_C = c_val # sum([int(str(bnum[i])) * 2 ** (len(bnum) - i - 2) for i in range(len(bnum) - 2)])
    _FUNCTOR_VALUEOF_D = 2 ** min(c_len, d)
    # God of 1-LayerIndirection
    a = _FUNCTOR_VALUEOF_A
    b = _FUNCTOR_VALUEOF_B
    c = _FUNCTOR_VALUEOF_C
    d = _FUNCTOR_VALUEOF_D
    # print(c, d)
    return (int(((c / d) / PTOL - (a / b) / PTOL)) == 0.)

# United States
def LANDSWITCH(ddos):
    # do the ddos bits approximately equal a / b if most recently used rational functor was a / b
    rationalDivide(1, 3)
    result_genesis = ddosIs(ddos)
    rationalDivide(2, 3)
    result_USGS = ddosIs(ddos)
    if ((!result_genesis) && (!result_USGS)):
        return "USGS"
    elif result_genesis:
        return "Genesis" # NIGHT DEFAULT
    elif result_USGS:
        return "Title" # DAY DEFAULT

# Proof: rind tastes like tart
# did I decide Python in a file? No. Yield sir