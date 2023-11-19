import re
import ipaddress

def is_valid_ip(ip_address):
    try:
        ipaddress.IPv4Network(ip_address, strict=False)
        return True
    except ValueError:
        return False

def subnet_info(ip_address, subnet_bits):
    try:
        ip_network = ipaddress.IPv4Network(f"{ip_address}/{subnet_bits}", strict=False)
    except ValueError:
        return None  # Handle invalid IP address or subnet bits

    num_subnets = 2 ** (32 - subnet_bits)
    num_hosts_per_subnet = 2 ** (32 - subnet_bits) - 2

    subnet_mask = ip_network.netmask

    subnet_ranges = []
    for subnet in ip_network.subnets():
        network_id = subnet.network_address
        broadcast_id = subnet.broadcast_address
        usable_range_start = network_id + 1
        usable_range_end = broadcast_id - 1
        subnet_range = {
            "Network ID": network_id,
            "Usable Range": f"{usable_range_start} - {usable_range_end}",
            "Broadcast ID": broadcast_id,
        }
        subnet_ranges.append(subnet_range)

    return num_subnets, num_hosts_per_subnet, subnet_mask, subnet_ranges, subnet_bits

while True:
    ip_class = input("Enter IP class (A, B, C): ").upper()
    if ip_class in ["A", "B", "C"]:
        break
    else:
        print("Invalid IP class. Please enter A, B, or C.")

while True:
    ip_address = input("Enter IP address (e.g., 193.1.2.0): ")
    if is_valid_ip(ip_address):
        break
    else:
        print("Invalid IP address format. Please enter a valid IP address.")

while True:
    subnet_bits = input("Enter subnet bits (e.g., 8, 16, 24): ")
    if subnet_bits.isdigit():
        subnet_bits = int(subnet_bits)
        if 1 <= subnet_bits <= 32:
            break
        else:
            print("Invalid subnet bits. Please enter a value between 1 and 32.")
    else:
        print("Invalid subnet bits. Please enter a valid number.")

if ip_class == "A":
    subnet_bits += 8
elif ip_class == "B":
    subnet_bits += 16
elif ip_class == "C":
    subnet_bits += 24

num_subnets, num_hosts_per_subnet, subnet_mask, subnet_ranges, cidr_count = subnet_info(ip_address, subnet_bits)

if num_subnets is not None:
    print(f"IP Address: {ip_address}")
    print(f"CIDR Count: /{cidr_count}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Total Number of Subnets: {num_subnets}")
    print(f"Number of Usable Hosts per Subnet: {num_hosts_per_subnet}")

    for i, subnet_range in enumerate(subnet_ranges, start=1):
        print(f"Subnet {i} - Network ID: {subnet_range['Network ID']}, Usable Range: {subnet_range['Usable Range']}, Broadcast ID: {subnet_range['Broadcast ID']}")
else:
    print("Invalid IP address or subnet bits.")

