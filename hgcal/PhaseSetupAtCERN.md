DIO5 zcu name: hgczcu102-mbv2 
user: agrummer or HGCAL_dev

Unicorn ZCU name: hgcalzcu102be
username: HGCAL_dev


installed the mac uart drivers C210x:
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers

then used screen to log in:
screen /dev/tty.SLAB_USBtoUART
(there are a few other tty.SLAB... devices but this one -without a number at the end - worked)

Simon was also able to use a program called 
minicom
to log in to the device

the unicorn image is here:
https://cernbox.cern.ch/files/link/public/1gzGQt659PVs9IZ?tiles-size=1&items-per-page=100&view-mode=resource-table

had to deal with GATEWAY option (remove it) in the fermilab image
from:
/etc/sysconfig/network-scripts/ifcfg-eth0


now:
ssh zcuunicorn
and
ssh zcudio5

on zcudio5:
sudo fw-loader load zcu102-siengine-v1p0-ROCv3

Unicorn SW:
https://gitlab.cern.ch/cms-hgcal-firmware/hgc-engine-tools/-/tree/unicorn_sw/unicorn_sw

Notes on Intalling a new petalinux build from:

dnf install rpm-name
take three files and copy them in to the BOOT location and then reboot linux
the tree files should be copied to /dev/mmcblk0p1 
after mounting it to boot:

sudo mount /dev/mmcblk0p1 /boot/

[agrummer@zcuUNICORN]$ ll /boot/
total 53396
-rwxr-xr-x 1 root root  1162040 Feb 19  2020 BOOT.BIN
-rwxr-xr-x 1 root root 18082304 Feb 19  2020 Image
-rwxr-xr-x 1 root root 18138248 Feb 19  2020 image.ub
-rwxr-xr-x 1 root root    54037 Feb 19  2020 system.dtb
-rwxr-xr-x 1 root root 17228291 Apr 23  2020 zcu102-boot.tgz

 
TODO:

- repeat internal clock test
- Test the ext clock - latest fw is on both zcu's now...
   - does data still arrive well at the DIO5 zcu
- Have to check the IO-blocks settings in unicorn repo

- change constraints file for ZCU106??


Trigger BE block logic...
https://gist.github.com/akgrummer/3c79556a42b06fd993e72dda99b707fc
- Can the other DAQ link send idles always? or a counter? Do I really care? The trigger links won't be read
- how do you stop the triggers coming in?
- busy signal?

sudo fw-loader load unicorn

Setting Internal Clock for unicorn ZCU
./uhal_unicorn.py -b ECONS-fast-commands-clk-FC-mux-0 --node clk_int_select --val 1

Use internal Fast Commands:
./uhal_unicorn.py -b ECONS-fast-commands-clk-FC-mux-0 --node FC_int_select --val 1

./uhal_unicorn.py --b Housekeeping-fast-commands-fastcontrol-axi-0 --node counters.errors
./uhal_unicorn.py --b ECONS-fast-commands-fastcontrol-recv-axi-0 --node counters.errors
./uhal_unicorn.py -b ECONS-fast-commands-fastcontrol-recv-axi-0 --node command.reset_counters_io

./uhal_unicorn.py -b phase-link-capture-AXI-0 --node link0.delay.bit_reverse --val 1


Talk to Arnaud:
how to calibrate ADC to TOA calibration
set threshold


on Serenity 4
empbutler -c /home/cmx/rshukla/test_stand/connections.xml do x0 frontend lpgbt status -c

on Serenity 3
source setEMP
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend lpgbt reset -c 11
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -c 11 0x70 0x36 0x80


empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend lpgbt -c 11 reset
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend lpgbt reset -c 11
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write 0x36 80 -c 11

empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend lpgbt reset -c 11
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -c 11 0x36 0x80
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -h
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -c 11 0x70 0x36 0x80
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend lpgbt reset -c 11
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend lpgbt reset -c 15
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -c 15 0x70 0x36 0x80
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend lpgbt reset -c 15
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -c 15 0x70 0x36 0x80
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -c 15 0x71 0x36 0x80
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -c 15 0x72 0x36 0x80
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -c 15 0x70 0x36 0x80
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 reset legacy
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -c 15 0x70 0x36 0x80
history |less
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend lpgbt reset -c 15
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend ic-write -c 15 0x70 0x36 0x80
jobs
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend lpgbt reset -c 15
empbutler -c /opt/hgc_utils/etc/connections.xml do x0 frontend lpgbt reset -c 14
empbutler -c /home/cmx/rshukla/test_stand/connections.xml do x0 frontend lpgbt status -c 14

o



daq out of 6
daq in to 7
trigger fibers on 4 and 5


how to get a new device (ZCU) online
NETWORK request form:
https://network.cern.ch/sc/fcgi/sc.fcgi?Action=SelectForDisplay


To put a device online:
https://network.cern.ch/sc/fcgi/sc.fcgi?Action=SearchForDisplay&DeviceName=HGCALZCU102FNAL1&PersonName=&PersonFirstName=&Location=&OutletID=&RackName=&IPaddress=&HardwareAddress=&Tag=&SerialNumber=&InventoryNumber=&OperatingSystem=&Domain=
search for devie:
HGCALZCU102FNAL1

The LANDB page is also useful for reference:
https://landb.cern.ch/portal/devices/HGCALZCU102FNAL1

Another zcu device:
https://network.cern.ch/sc/fcgi/sc.fcgi?Action=SearchForDisplay&DeviceName=&PersonName=&PersonFirstName=&Location=&OutletID=&RackName=&IPaddress=&HardwareAddress=00%3A0a%3A35%3A04%3AF9%3A75&Tag=&SerialNumber=&InventoryNumber=&OperatingSystem=&Domain=


There is a pretty fast turn around to bring the device up - if all configurations are set well


bmon linux command



run:
1691537835



Questions about phase data:
why is the alignment on 0xcacccccc? not inverted endian... how can it be byte endian?
why don't I have to subtract the value of fc7 phase from 32? 


