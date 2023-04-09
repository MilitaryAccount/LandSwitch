# LandSwitch
to Ava

In __land_switch.py__ the function LANDSWITCH(ddos) handles incoming packet data, per packet.

The IP DDoS packet does not necessarily have a decimal point so is read as

    0.__data__ = __data__ / 2^size(data)
    
data is the IP DDoS packet data.
