To allow internet access on the devices add:
GATEWAY=192.168.1.251
(which points to the hcalpro machine's ip) 
to the network configuration file:
/etc/sysconfig/network-scripts/ifcfg-eth0

then need to reboot the hexacontroller


The zcu mac address can be reset during boot by adding a line in this file:
/etc/sysconfig/network-scripts/ifcfg-eth0

The default Mac address was:
00:0a:35:05:10:04
  
The line added:
MACADDR=00:0a:35:05:10:05