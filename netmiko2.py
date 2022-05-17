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
commands_list: contains the list of commands in order of execution
"""

with open("node_list.txt") as f1:
    node_list=f1.readlines()

with open("command_list.txt") as f2:
    command=f2.readlines()



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
            for command1 in command:
                output = ssh.send_command(command1)
                f3.write(f"*********************** {command1} *****************************\n")
                f3.write(output)
            print(f"Connection to {hostname1.strip()} is successful...Output is saved in {filename}")



