from distutils import command
from ipaddress import ip_address
from netmiko import ConnectHandler
from setuptools import command


SW1={'host':'10.211.2.10',
'username':'samer','password':'cisco','device_type':'cisco_xr'}
SW1SSH=ConnectHandler(**SW1)
loopbacks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in loopbacks:
    P1=(f"interface loopback{i}".format(i))
    P2=(f"ip address 1.1.{i}.1 255.255.255.255".format(i))
    interface=SW1SSH.send_command_timing(P1)
    createint=SW1SSH.send_command_timing(P2)
    configmode=SW1SSH.send_command_timing("configure terminal")
    print(configmode)
    print(interface)
    print(createint)
showrun=SW1SSH.send_command('show ip inter br')


SW1SSH.disconnect()
