from ipaddress import ip_address
from netmiko import ConnectHandler

SW1={'host':'10.211.10.36',
'username':'samer','password':'cisco','device-type':'cisco-ios'}
SW1SSH=ConnectHandler(**SW1)

for loopbacks in (10):
    print ("interface loopback{}".format(loopbacks))
    print("ip address 1.1.{}.1 255.255.255.255".format(loopbacks))


SW1SSH.disconnect()