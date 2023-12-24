import re
import ipaddress

def is_valid_ip(ip_address):
    ip_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    return re.match(ip_pattern, ip_address) is not None

def subnet_info(ip_address, subnet_bits):
    num_subnets = 2 ** subnet_bits
    num_hosts_per_subnet = 2 ** (32 - subnet_bits) - 2

    subnet_mask = '255.255.255.' + str(256 - 2 ** (8 - subnet_bits))

    network = ipaddress.IPv4Network(ip_address + '/' + str(subnet_bits), strict=False)

    subnet_ranges = []
    for subnet in network.subnets():
        subnet_range = {
            "Network ID": subnet.network_address,
            "Broadcast ID": subnet.broadcast_address,
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
        break
    else:
        print("Invalid subnet bits. Please enter a valid number.")

if ip_class == "A":
    subnet_bits += 8
elif ip_class == "B":
    subnet_bits += 16
elif ip_class == "C":
    subnet_bits += 24

if subnet_bits > 32 or subnet_bits < 1:
    print("Invalid subnet bits.")
else:
    num_subnets, num_hosts_per_subnet, subnet_mask, subnet_ranges, cidr_count = subnet_info(ip_address, subnet_bits)

    print(f"IP Address: {ip_address}")
    print(f"CIDR Count: /{cidr_count}")
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Total Number of Subnets: {num_subnets}")
    print(f"Number of Usable Hosts per Subnet: {num_hosts_per_subnet}")

    for i, subnet_range in enumerate(subnet_ranges, start=1):
        print(f"Subnet {i} - Network ID: {subnet_range['Network ID']}, Broadcast ID: {subnet_range['Broadcast ID']}")
