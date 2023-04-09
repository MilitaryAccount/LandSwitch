# LandSwitch
to Ava

In **land_switch.py** the function LANDSWITCH(ddos) handles incoming packet data, per packet.
The IP DDoS packet does not necessarily have a decimal point so is interpreted as
    0.**data** = **data** / 2^size(data)
data is the IP DDoS packet data.
