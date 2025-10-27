# Notes for setting up the HexaController system
log in to lpc then hcalpro
pswd for the components below is daq5HGCAL!

in different tabs:

log in to zcu
ssh HGCAL_dev@192.168.1.47
now: ssh zcu
run ~/agrummer/HexaCookbook/coldstart.sh

log in to raspberry pi:
ssh HGCAL_dev@192.168.1.94
now: ssh raspi
during the zcu setup run
/home/HGCAL_dev/agrummer/cookbook/lpgbtColdstart.sh

log in to a hexaController
(list all computers on the network with 
`arp | grep ether` note: 45 and 48 are for econ)
--now set to 90, 91, and 95
ssh HGCAL_dev@192.168.1.95
ssh HGCAL_dev@192.168.1.91
now: ssh hexaE1, ssh hexaW1, ssh hexaW2

from /home/HGCAL_dev/mylittledt/
run `sudo make interposer`
from /home/HGCAL_dev/source/test
run `sudo ./interposer`
run `sudo ./clkRates`
run `sudo ./clkSource`
clkRates will only show System 160 = ~>160 if ./interposer is run first
clkSource will show  orbit sync errors and many FC errors before ./interposer is run

instructions for setting the IP addresses are in:
https://github.com/cmantill/econt_sw/blob/master/econt_sw/hexactrl_setup.md
-search for Mac Address

ssh setup in: ~/.ssh/config


package:
readlines


sudo chmod 777 /dev/uio*
source ./env.sh

start uHal server on interposer
executable:
source/interposer/bin/interposer_server

source code
sources/main/executables/interposer_server.cxx

to control sca...:
see wagoneer on hexacontroller or zcu..?
