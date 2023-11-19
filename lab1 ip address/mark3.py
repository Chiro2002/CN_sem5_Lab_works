import ipaddress

def get_ip_class(ip_address):
    ip = ipaddress.IPv4Network(ip_address, strict=False)
    if ip.network_address.is_private:
        return 'C'
    elif ip.network_address.is_multicast:
        return 'Multicast'
    elif ip.network_address.is_reserved:
        return 'Reserved'
    elif ip.network_address.is_loopback:
        return 'Loopback'
    elif ip.network_address.is_link_local:
        return 'Link Local'
    elif ip.network_address.is_unspecified:
        return 'Unspecified'
    else:
        return 'A' if ip.prefixlen <= 8 else 'B' if ip.prefixlen <= 16 else 'C'

def calculate_subnet_bits(num_subnets):
    subnet_bits = 0
    while 2 ** subnet_bits < num_subnets:
        subnet_bits += 1
    return subnet_bits

def main():
    while True:
        ip_address = input("Enter IP address (e.g., 193.1.2.0): ")
        try:
            ip_class = get_ip_class(ip_address)
            if ip_class == 'A':
                subnet_bits = int(input("Enter subnet bits (e.g., 8, 16, 24): "))
                if 8 <= subnet_bits <= 30:
                    break
                else:
                    print("Invalid subnet bits. Please enter a value between 8 and 30.")
            elif ip_class == 'B':
                subnet_bits = int(input("Enter subnet bits (e.g., 16, 24): "))
                if 16 <= subnet_bits <= 30:
                    break
                else:
                    print("Invalid subnet bits. Please enter a value between 16 and 30.")
            elif ip_class == 'C':
                subnet_bits = int(input("Enter subnet bits (e.g., 24): "))
                if subnet_bits == 24:
                    break
                else:
                    print("Invalid subnet bits. Please enter 24 for Class C.")
            else:
                print("Invalid IP address. Please enter a valid IP address.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    num_subnets = 2 ** (32 - subnet_bits)
    print(f"IP Address: {ip_address}")
    print(f"IP Class: {ip_class}")
    print(f"Subnet Mask: {ipaddress.IPv4Network(f'{ip_address}/{subnet_bits}', strict=False).netmask}")
    print(f"Total Number of Subnets: {num_subnets}")

    while True:
        try:
            num_requested_subnets = int(input("Enter the number of subnets you need: "))
            if 1 <= num_requested_subnets <= num_subnets:
                break
            else:
                print(f"Invalid number of subnets. Please enter a value between 1 and {num_subnets}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    new_subnet_bits = calculate_subnet_bits(num_requested_subnets)
    subnet = ipaddress.IPv4Network(f"{ip_address}/{new_subnet_bits}", strict=False)
    
    print(f"Subnet Mask for {num_requested_subnets} Subnets: {subnet.netmask}")
    
    for i, subnet_range in enumerate(subnet.subnets(new_prefix=new_subnet_bits), start=1):
        network_id = subnet_range.network_address
        broadcast_id = subnet_range.broadcast_address
        usable_range_start = network_id + 1
        usable_range_end = broadcast_id - 1
        print(f"Subnet {i} - Network ID: {network_id}, Usable Range: {usable_range_start} - {usable_range_end}, Broadcast ID: {broadcast_id}")

if __name__ == "__main__":
    main()
