from netmiko import ConnectHandler

#define device details
local_switch = {
    'device_type': 'extreme_exos',
    'ip': '10.10.1.24',
    'username': 'XXXXXX',
    'password': 'XXXXXX',
    'port': 22,
    'timeout': 20,
}

#VLAN access
vlan_details = {
    'User_Network': {'ip': '10.10.1.8', 'vlan_id': 100},
    'ACCT_Network': {'ip': '10.10.1.7', 'vlan_id': 200},
    'MGMT_Network': {'ip': '10.10.1.6', 'vlan_id': 300},
    'IT_Network': {'ip': '10.10.1.5', 'vlan_id': 400},
}

#Connect to local switch
try:
    connection = ConnectHandler(**local_switch)
    print(f"Connected to Local Switch ({local_switch['ip']})")

    #Configure VLANS on local switch
    for vlan_name, vlan_info in vlan_details.items():
        vlan_id = vlan_info['vlan_id']
        config_commands = [
            f'create vlan {vlan_name} tag {vlan_id}'
        ]
        output = connection.send_config_set(config_commands)
        print(f"VLAN {vlan_name} is successfully created on the local switch")

    connection.disconnect()
    print(f"Disconnected from local switch ({local_switch['ip']})\n")

#Connect to other switches and configure VLANs
    for vlan_name, vlan_info in vlan_details.items():
        switch_ip = vlan_info['ip']
        vlan_id = vlan_info['vlan_id']
        switch = {
            'device_type': 'extreme_exos',
            'ip': switch_ip,
            'username': 'XXXXXX',
            'password': 'XXXXXX',
            'port': 22,
            'timeout': 20,
            'fast_cli': True,
        }
        try:
            connection = ConnectHandler(**switch)
            print(f"Connected to switch ({switch_ip})")

            config_commands = [
                f'create vlan {vlan_name} tag {vlan_id}'
            ]
            output = connection.send_command(config_commands[0])
            print(output)
            print(f"VLAN {vlan_name} successfully configured on switch ({switch['ip']})")

            connection.disconnect()
            print(f"Disconnected from switch ({switch['ip']})\n")

        except Exception as e:
            print(f"Failed to configure VLAN on switch ({switch['ip']}): {str(e)}")


except Exception as e:
    print(f"Failed to connect to local switch ({local_switch['ip']}): {str(e)}")

#Confirm VLANs were created
print("VLAN deployment complete.\n")
