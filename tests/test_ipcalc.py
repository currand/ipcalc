import pytest
import ipaddress
import ipcalc

def test_ipcalc():
    subnet = ipaddress.ip_network('2001:1960::/125')
    assert ipcalc.format_subnet(subnet) == ['Network 2001:1960::', 
    'Broadcast 2001:1960::7', 
    'Range 2001:1960:: - 2001:1960::7', 
    'Mask ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff8', 
    'HostAddrs 8', 
    'HostMin 2001:1960::1', 
    'HostMax 2001:1960::6']