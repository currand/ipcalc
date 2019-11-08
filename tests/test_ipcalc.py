import pytest
import ipaddress
import functions

def test_format_subnet():
    subnet = ipaddress.ip_network('2001:1960::/125')
    assert functions.format_subnet(subnet) == ['Network 2001:1960::', 
        'Broadcast 2001:1960::7', 
        'Range 2001:1960:: - 2001:1960::7', 
        'Mask ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff8', 
        'HostAddrs 8', 
        'HostMin 2001:1960::1', 
        'HostMax 2001:1960::6']

def test_subnet_info():
    subnet = ipaddress.ip_network('2001:1960::/125')
    subnet_info = functions.subnet_info(subnet)
    
    assert subnet_info == {
        'network': '2001:1960::',
        'broadcast': '2001:1960::7',
        'range': ['2001:1960::', '2001:1960::7'],
        'mask': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff8',
        'hostaddrs': 8,
        'hostmin': '2001:1960::1',
        'hostmax': '2001:1960::6'
    }
