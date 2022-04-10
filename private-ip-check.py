import ipaddress

input_ip = input('Enter an IP address: ')

result = ipaddress.ip_address(input_ip).is_private

print(result)

# ---
# Other ideas

# >>> from IPy import IP
# >>> ip = IP('127.0.0.0/30')
# >>> ip.iptype()
# 'PRIVATE'

# ---
# More ideas:
# https://stackoverflow.com/q/691045