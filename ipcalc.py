import ipaddress

def subnet_info(addr):
    # hosts = [x for x in addr.hosts()]

    return {
        'network': addr.network_address,
        'broadcast': addr.broadcast_address,
        'range': [addr.network_address, addr.broadcast_address],
        'mask': addr.netmask,
        'hostaddrs': addr.num_addresses,
        'hostmin': addr.network_address + 1,
        'hostmax': addr.broadcast_address - 1
    }

def print_subnet(subnet):
    output = []

    output.append("Network {}".format(subnet['network']))
    output.append("Broadcast {}".format(subnet['broadcast']))
    output.append("Range {} - {}".format(subnet['range'][0], subnet['range'][1]))
    output.append("Mask {}".format(subnet['mask']))
    output.append("HostAddrs {}".format(subnet['hostaddrs']))
    output.append("HostMin {}".format(subnet['hostmin']))
    output.append("HostMax {}".format(subnet['hostmax']))

    return output

if __name__ == '__main__':
    
    subnet = input("Subnet: ")
    new_prefix = int(input("Prefix Length: "))
    print('\n\n')
    addr = ipaddress.ip_network(subnet)

    output = print_subnet(subnet_info(addr))
    output += '\n'
    if new_prefix:
        output += ['Subnets:']
        new_subnets = addr.subnets(new_prefix=new_prefix)
        for new_subnet in new_subnets:
            output += print_subnet(subnet_info(new_subnet))
            output += '\n'

print('\n'.join(output))

    