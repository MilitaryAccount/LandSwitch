# LandSwitch

In __land_switch.py__ the function LANDSWITCH(ddos) handles incoming packet data, per packet.

The IP DDoS packet does not necessarily have a decimal point so is read as

    0.data = data / 2^size(data)
    
# EVE's mistake: data is an entire IP DDoS packet
data is the data field of the IP DDoS packet or IP packet which is flooded with binary sequence data
