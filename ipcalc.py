import ipaddress

def format_subnet(subnet):
    output = []

    output.append("Network {}".format(subnet.network_address))
    output.append("Broadcast {}".format(subnet.broadcast_address))
    output.append("Range {} - {}".format(subnet.network_address, subnet.broadcast_address))
    output.append("Mask {}".format(subnet.netmask))
    output.append("HostAddrs {}".format(subnet.num_addresses))
    output.append("HostMin {}".format(subnet.network_address + 1))
    output.append("HostMax {}".format(subnet.broadcast_address - 1))

    return output


if __name__ == '__main__':

    # subnet = '2601:1960::/125'
    # new_prefix = 127
    output = []

    subnet = input("Subnet: ")

    new_prefix = input("\nPrefix Length: ")

    subnet_obj = ipaddress.ip_network(subnet)
    output = format_subnet(subnet_obj)

    if new_prefix != '':
        output += '\n'

        output += ['Subnets:']
        new_subnets = subnet_obj.subnets(new_prefix=int(new_prefix))
        for new_subnet in new_subnets:
            subnet_obj = ipaddress.ip_network(new_subnet)
            output += format_subnet(subnet_obj)
            output += '\n'

    print('\n'.join(output))