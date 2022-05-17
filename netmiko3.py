import netmiko
import time
from netmiko import ConnectHandler

"""
Please enter your credentials to log in to the router
"""

username = input("Please Enter Your User Name: ")
password = input("Please Enter Your Password: ")


"""
node_list.txt: contains the list of the MGT IPs/Hostnames
"""

with open("node_list.txt") as f1:
    node_list=f1.readlines()
with open("command_list.txt") as f2:
    commands1=f2.readlines()
    print(commands1)

    """
The list of commands as a list
"""
commands = ['router ospf 1',
            'network 10.0.0.0 0.255.255.255 area 0',
            'network 192.168.100.0 0.0.0.255 area 1']


#command = ["enable\n","\n","test\n","\n","ter len 0\n","\n","config t\n","\n","hostname DR-3\n","do show ip int br","\n"]

for hostname1 in node_list:

    cisco_router = {
        'device_type': 'cisco_ios',
        'host': hostname1,
        'username': username,
        'password': password,
        'secret': password,
        'port': 22,
    }
    filename = hostname1.strip('\n') + ".txt"

    try:
        ssh=ConnectHandler(**cisco_router)
        ssh.enable()

    except Exception as e:
        print(e)
        print("****************************************************************")
        print(f"Please check the issue in {hostname1.strip()}")
        print("****************************************************************")
        pass
    else:
        with open(filename, 'w') as f3:
            result = ssh.send_config_set(commands)
            ssh.exit_config_mode()
            result1=ssh.send_multiline(commands1)
            f3.write(result)
            f3.write(result1)
            print(f"Connection to {hostname1.strip()} is successful...Output is saved in {filename}")



