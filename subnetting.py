def main():
    ip = input("ENTER IP: ") #The program asks the user to enter an IP address, which is stored in the variable ip.
    checkclass = ip.split('.')[0]  #The IP address is split by the dot (.) separator to get its parts. checkclass holds the first octet of the IP address, which indicates the class of the IP.

    cc = int(checkclass)    #cc stores the integer form of this octet.
    mask = None

    if cc > 0:
        if cc <= 127:
            mask = "255.0.0.0"
            print("Class A IP Address")
            print("SUBNET MASK:\n" + mask)
        elif cc >= 128 and cc <= 191:
            mask = "255.255.0.0"
            print("Class B IP Address")
            print("SUBNET MASK:\n" + mask)
        elif cc >= 192 and cc <= 223:
            mask = "255.255.255.0"
            print("Class C IP Address")
            print("SUBNET MASK:\n" + mask)
        elif cc >= 224 and cc <= 239:
            mask = "255.0.0.0"
            print("Class D IP Address Used for multicasting")
        elif cc >= 240 and cc <= 254:
            mask = "255.0.0.0"
            print("Class E IP Address Experimental Use")

    if mask:
        ip_addr_parts = ip.split('.') #ip.split('.') splits the IP address into its four parts, or "octets." Eg : ['192', '168', '1', '1'].
        mask_parts = mask.split('.') #mask.split('.') does the same for the subnet mask. Eg : ['255', '255', '255', '0'].

        network_addr = []  #Empty Lists Holds Results
        last_addr = []

        for i in range(4):

            #int(ip_addr_parts[i]) and int(mask_parts[i]) convert these octet strings into integers so bitwise operations can be performed on them.
            ip_part = int(ip_addr_parts[i])
            mask_part = int(mask_parts[i])

            #Network address calculation (The network address is calculated using the bitwise AND operator (&) between the IP address and subnet mask.)
            network_part = ip_part & mask_part
            network_addr.append(str(network_part))

            #Broadcast address calculation ( The broadcast address is calculated using two operations: Bitwise NOT (~mask_part): This inverts the bits in mask_part, changing each 1 to 0 and each 0 to 1. Bitwise AND (& 255): Limits the result to 8 bits, which is necessary for IPv4 octets.
            last_part = network_part | (~mask_part & 255) #Broadcast Address (last IP) by using a combination of the OR and NOT operations.
            last_addr.append(str(last_part))

        # Join the parts with '.' to form complete IP addresses. (The calculated parts of network_addr and last_addr are joined with dots to form complete IP addresses and printed as the first and last IPs in the range.)
        network_addr = '.'.join(network_addr)
        last_addr = '.'.join(last_addr)

        print("First IP of block: " + network_addr)
        print("Last IP of block: " + last_addr)


if __name__ == "__main__":
    main()






