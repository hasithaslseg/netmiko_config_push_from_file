# netmiko_config_push_from_file
This program is used to send multiple commands to network devices from below two text files....

node_list.txt: contains the list of the MGT IPs/Hostnames
commands_list: contains the list of commands in order of execution

The program will ssh to each device in the node_list and execute commands in commands_list file in order....
The output will be saved in to seperate files per device
