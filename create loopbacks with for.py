from distutils import command
from ipaddress import ip_address
from netmiko import ConnectHandler
from setuptools import command
import time

SW1={'host':'10.211.2.10',
'username':'samer','password':'cisco','device_type':'cisco_xr'}
SW1SSH=ConnectHandler(**SW1)
#you can use range in loop but I used this below.
loopbacks=(11, 12, 13, 14, 15, 16, 17, 18, 19, 100)

#this is a for loop to create interfaces and add ip addresses
for i in loopbacks:
    P1=(f"interface loopback{i}".format(i))
    P2=(f"ip address 1.1.{i}.1 255.255.255.255".format(i))
    interface=SW1SSH.send_command_timing(P1) #timing here will make code run little slow and it is recommended for Cisco IOS,XE,XR
    createint=SW1SSH.send_command_timing(P2)
    configmode=SW1SSH.send_command_timing("configure terminal")
    print(configmode)
    print(interface)
    print(createint)
showrun=SW1SSH.send_command('show ip inter br')
print(showrun)


SW1SSH.disconnect()
