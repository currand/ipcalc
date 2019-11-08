import pytest
from app import app as client


@pytest.fixture
def app():
    return client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_main_subnet(client):
    response = client.get('/api/prefix/192.168.86.0_24/')
    assert response.json == {
        "broadcast": "192.168.86.255", 
        "hostaddrs": 256, 
        "hostmax": "192.168.86.254", 
        "hostmin": "192.168.86.1", 
        "mask": "255.255.255.0", 
        "network": "192.168.86.0", 
        "range": [
            "192.168.86.0", 
            "192.168.86.255"
        ]
    }

def test_new_prefixes(client):
    response = client.get('/api/prefix/2001:1960::_125/127/')
    assert response.json == [
        {
            "network": "2001:1960::", "broadcast": "2001:1960::7", 
            "range": ["2001:1960::", "2001:1960::7"], 
            "mask": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:fff8", 
            "hostaddrs": 8, "hostmin": "2001:1960::1", "hostmax": "2001:1960::6"
        }, {
            "network": "2001:1960::", "broadcast": "2001:1960::1",
            "range": ["2001:1960::", "2001:1960::1"], 
            "mask": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe",
            "hostaddrs": 2, "hostmin": "2001:1960::1", "hostmax": "2001:1960::"
        }, {
            "network": "2001:1960::2", "broadcast": "2001:1960::3",
            "range": ["2001:1960::2", "2001:1960::3"],
            "mask": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe",
            "hostaddrs": 2, "hostmin": "2001:1960::3", "hostmax": "2001:1960::2"
        }, {
            "network": "2001:1960::4", "broadcast": "2001:1960::5",
            "range": ["2001:1960::4", "2001:1960::5"],
            "mask": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe",
            "hostaddrs": 2, "hostmin": "2001:1960::5", "hostmax": "2001:1960::4"
        }, {
            "network": "2001:1960::6", "broadcast": "2001:1960::7",
            "range": ["2001:1960::6", "2001:1960::7"],
            "mask": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:fffe",
            "hostaddrs": 2, "hostmin": "2001:1960::7", "hostmax": "2001:1960::6"
        }
    ]