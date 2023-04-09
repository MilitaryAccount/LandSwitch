# LandSwitch

In __land_switch.py__ the function LANDSWITCH(ddos) handles incoming packet data, per packet.

The IP DDoS packet does not necessarily have a decimal point so is read as

    0.data = data / 2^size(data)
    
data is an entire IP DDoS packet
