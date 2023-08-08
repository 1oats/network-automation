from netmiko import ConnectHandler

#Define device details

accesscloset = {
    "device_type": "extreme_exos",
    "ip": "10.10.1.24",
    "username": "XXXXXX",
    "password": "XXXXXX",
    "port": 22,
}

#Establish SSH connection to device
connection = ConnectHandler(**accesscloset)

output = connection.send_command("show vlan")
print("Existing VLANS in Access Closet 1")
print(output)

#Disconnect from switch
connection.disconnect()
