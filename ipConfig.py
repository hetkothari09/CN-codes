import ipaddress

def ip_class(ip):
    first_octet = int(ip.split('.')[0])
    if 1 <= first_octet <= 126:
        return 'A'
    elif 128 <= first_octet <= 191:
        return 'B'
    elif 192 <= first_octet <= 223:
        return 'C'
    elif 224 <= first_octet <= 239:
        return 'D'
    elif 240 <= first_octet <= 255:
        return 'E'
    else:
        return 'Unknown'

def subnet_mask(ip_class):
    if ip_class == 'A':
        return '255.0.0.0'
    elif ip_class == 'B':
        return '255.255.0.0'
    elif ip_class == 'C':
        return '255.255.255.0'
    else:
        return 'N/A'

def first_ip_address(ip, ip_class):
    ip_int = int(ipaddress.ip_address(ip))
    subnet_int = int(ipaddress.ip_address(subnet_mask(ip_class)))
    
    network_int = ip_int & subnet_int
    
    network_ip = str(ipaddress.ip_address(network_int))
    return network_ip

def main():
    ip = input("Enter an IP address: ")
    
    try:
        ip_obj = ipaddress.ip_address(ip)
        ip_str = str(ip_obj)
        ip_cls = ip_class(ip_str)
        mask = subnet_mask(ip_cls)
        first_ip = first_ip_address(ip_str, ip_cls)
        
        print(f"IP Address: {ip_str}")
        print(f"Class: {ip_cls}")
        print(f"Subnet Mask: {mask}")
        print(f"First IP Address in the Class: {first_ip}")
    except ValueError as e:
        print(f"Invalid IP address: {e}")

if __name__ == "__main__":
    main()
