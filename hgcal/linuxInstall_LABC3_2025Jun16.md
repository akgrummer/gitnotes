# Hardware
install intel core ultra
WATCH the youtube vidoe

Follow Motherboard maunal (comes as pamphlet
plastic piece on CPU cover pops off when installing CPU to the socket (check the alignment)
rubber spacer inserted for underneath storage SSE
M2 goes in at an anlge
insert metal nut spacer to mount the M2
remove peal frm metal fastener
Memory sticks go in


could install a network card and pass 100GB ethernet from vcu to card to PC


thermal paste was expired (spread evenly) rotate cooling connection when placing it (back and forth) to make sure the spread is even

PCIe cart SFP connectors point away from the cpu
put standoffs on the chassis (box) before placing motherboard (note the one is asymmetric because of the USB/display port etc hub)

Plug Pump cable in to pump connector on motherboard (3 pin female cable to 4 pin male connector on motherboard)
Plug fan to fan connector on motherboard
ignore lights ARGP connectors
dress cables so that they don't get in the way of the fans (redo the twist-ties)

# OS install
notes for all linux PC installs:
linuxInstall_LABC2_2025Mar13.md
linuxInstall_LABC3_2025Jun16.md
2025JanVCU.md
installLinux_ReceptionRoomPC.md



in BIOS advanced - enable Network Stack then exit and Save Bios (restart it)
the mac address came up on the screen during restart - but was in a strange font (difficult to read)
The restart took longer that I expected
Once BIOs restarted Mac address is found in the last entry of Advanced options. (not in a dropdown menu, not under something called "Network" - doesn't even say network in the entry
"Realtek PCIe 2.5GBE Family Controller Mac:
MAC: A0:AD:9F:85:36:62

adding to DHCP of labc1


Update the BIOS:
the bios was on version 2001
updating to version 2006 (date: 2025/05/14)
ignoring message to update Bitlocker recovery key and suspend Bitlocker encryption key - I think this is for Window's devices...

for this motherboard:
https://www.asus.com/motherboards-components/motherboards/others/z890-ayw-gaming-wifi-w/helpdesk_bios?model2Name=Z890-AYW-GAMING-WIFI-W

https://www.youtube.com/watch?v=Ndnpw8sflpg

for removing secure boot:
https://www.youtube.com/watch?v=tnOHi0w77bU



for linux usb:
sudo mkfs.ext4 /dev/sda1


in ~/AlmalinuxImages on Aidan's mac - downloaded tar for Network driver
download from here:
https://www.realtek.com/Download/ToDownload?type=direct&downloadid=3763
https://www.realtek.com/Download/List?cate_id=584
for Realtek RTL8125
Network Interface Controllers > 2.5G Gigabit Ethernet > PCI Express

r8125-9.016.00.tar.bz2
copy over to labc2 and put on usb drive
reformat the usb with (removes data):
`mkfs.ext4 /dev/sda1`
also useful:
lsusb
ls /dev/
mkdir /mnt/usb
mount /dev/sda1 /mnt/usb

and
umount /mnt/usb

Trick - use the ethernetDongle to get network

follow instructions for labc2
- for adding the CERN repo in installation source - selected "Auto-detected instalation media (and not "On the network" like in CERN instructions ) and added the repourl as instructed with 9.6: `linuxsoft.cern.ch/cern/alma/9.6/CERN/x86_64/`

after reboot - select "No, I will do setup myself
and 2 locations: "enable auo check for updates"

did this again:
yum group install fermilab

installed network driver - notes from RPM instaleld from elrepo
the notes are on labc3
had to restart pc after installing to insert the module

## vivado install
had to register the license on the vivado webpage before installing vitus on pc
- so login didn't work at first
- needed node lock - so provided mac address (after installing labc3 network driver) and hostname
changed hostname with:
hostnamectl set-hostname labc3-fnal-gov
then
cat /etc/hostname


dnf install epel-release


BEFORE installing vivado:
https://adaptivesupport.amd.com/s/question/0D52E00006hpQNASA2/vivado-installation-got-stuck-says-generating-installed-devices-list?language=en_US

dnf install ncurses-c++-libs
dnf install ncurses-compat-libs
dnf install ncurses-devel
dnf install ncurses-libs
dnf install ncurses-term

installed the vitus tools in /home/agrummer
should have put it in /home/agrummer/Xilinx

moved all the directories to Xilinx/
and ran
find . -type f -exec sed -i 's#/home/agrummer#/home/agrummer/Xilinx#g' {} +


copy from LABC2 to LABC3:

some files owned by root in /home/agrummer were not coppied
also this was a bit problematic because on labc2 some old attempts to install vivado from agrummer were starting to be copied - so be wary

for root:

replace <tilda> with ~ below
 1060  rsync --info=progress2 --archive --ignore-existing cass-sw labc3:<tilda>/
 1061  rsync --info=progress2 --archive --ignore-existing cmake-3.30.0-rc4 labc3:<tilda>/
 1062  rsync --info=progress2 --archive --ignore-existing --exclude "*.tar.gz" --exclude "*.tar" cass-sw labc3: <tilda>/
 1063  rsync --info=progress2 --archive --ignore-existing --exclude "*.tar.gz" --exclude "*.tar" . labc3:/root

for Agrummer:
 1004  rsync --info=progress2 --archive --ignore-existing --exclude "*.tar.gz" --exclude "*.tar" mfDefs.hgcal labc3:
 1005  rsync --info=progress2 --archive --ignore-existing --exclude "*.tar.gz" --exclude "*.tar" . labc3:/home/agrummer
 1006  rsync --info=progress2 --progress --archive --ignore-existing --exclude "*.tar.gz" --exclude "*.tar" --exclude "Xilinx/*" . labc3:/home/agrummer
 1007  ls fw/
 1008  rsync --info=progress2 --progress --archive --ignore-existing --exclude "*.tar.gz" --exclude "*.tar" --exclude "Xilinx/*" --exclude ".Xilinx/*" . labc3:/home/agrummer
 1009  rsync --info=progress2 --progress --archive --ignore-existing --exclude "*.tar.gz" --exclude "*.tar" --exclude "Xilinx/*" --exclude ".Xilinx/*" --exlcude "fw/*" . labc3:/home/agrummer
 1010  rsync --info=progress2 --progress --archive --ignore-existing --exclude "*.tar.gz" --exclude "*.tar" --exclude "Xilinx/*" --exclude ".Xilinx/*" --exclude "fw/*" . labc3:/home/agrummer
 1011  rsync --info=progress2 --progress --archive --ignore-existing --exclude "*.tar.gz" --exclude "*.tar" --exclude "*Xilinx*" --exclude "fw/*" --exclude "*XIC*" . labc3:/home/agrummer



### cable install

installed cable drivers post-vivado install

https://docs.amd.com/r/en-US/ug973-vivado-release-notes-install-license/Installing-Cable-Drivers

for labc3 did not install Vivado Labs so installed cable drivers from Vivado:

/home/agrummer/Xilinx/Vivado/2022.2/data/xicom/cable_drivers/lin64/install_script/install_drivers
./install_drivers


## more
sudo yum groupinstall uhal

didn't have python3.11 this time for some reason:
yum install python3.11
sudo yum install cactuscore-uhal-python311
sudo yum install cactuscore-uhal-python311-gui

dnf install lsb_release


## email to Zoltan:

### 1

We replaced the modules on the cassette today.
Toni arrived and helped with this.
Also met with Danny and Jon. They are big proponents of pytest…

The new VCU PC is mostly installed now.
The network driver had to be installed manually.
Switch 16 on the VCU board had to be adjusted for JTAG mode.
I had to move the VCU to the first PCIe (G5) slot to get the kernel and OS to recognize that the VCU was in place. I tried two of the other 3 slots.
I reloaded the clocks on the fmc+ card and the 2 lights came up – one after programming the clocks and one after the “verification” step. I only see one light on the labc2 vcu card.
Empbutler is installed and reads registers from the firmware.

The SCUI software is timing out – so I couldn’t confirm that Si570_1 is still set. Maybe something is blocking the communication to the board (?). Hopefully the clock frequency is still set correctly – since we programmed the boot up frequency.

I plugged fiber 1 to the single module silicon train on the 10 degree cassette. The downlinks and uplinks did not come up immediately. I will continue to try it tomorrow.

### 2

I powered the system off. I confirmed all 3 switches are in the same positions on the 2 VCUs (with photos).

I still have not resolved the downlinks and uplinks not locking.

Step by step:
Powerup the PC
the SCUI communication works again – the clock rate on Si570_1 reads back 320.6 MHz after boot as expected.
Then I load the FW.
The PCIe is NOT found in the lspci list.
Then I do a “reboot” from the linux command line – which does NOT power cycle the VCU.
Then the PCIe and xdma module ARE found.
The SCUI still works and I read back 320.6 MHz
I program the FMC+mezzanine – the lights turn on.
The QPLL is locked in the EMPbutler status report
The downlinks are are all 0. So are the uplinks
I can read back the clock rates with empbutler. They are not correct – they are copied below.

Comments:
1. The manual rescan of the pcie slots is not working after this system is power cycled. I needed to do the reboot yesterday as well. I don’t know if this is true for the other FNAL VCU because I have not turned that VCU off in a long time.
2. One light on the FMC+ Mezzanine turns on if the FW is loaded after the mezzanine is programmed. Two lights turn on if the FW is already loaded and then the fmc card is programmed.


## getting pcie and Xdma on

Used slot G5 - Gen5 slot says x16 in the dmidecode list:
dmidecode --type 9
or equivelently
dmidecode --type slot
There two that say 4x x4
and one that says x1
tried one of each of the 4x x4 and x1
but didn't see the pcie come up in the pcie list


the sequence of steps at power on mattered - see emails above
-> not clear I had the right sequence for the other PCIe slots
-> might be able to avoid having to reboot by have some firmware loaded at power up

## VCU and VCU mezzanine switches

Make sure the 3 switches on the VCU and the one switch on the VCU mezzanine are set correctly
SW15 and SW12 - all zeros
SW16: 0101 - and the bits are counted 1,2,3,4 where 1:0, 2:1, 3:0, 4:1
mezzanine switch: 0101 again where 1:0, 2:1, 3:0, 4:1

## more software installs:

dnf install cmake

https://github.com/jbeder/yaml-cpp.git
commit: 28f93bd - (3 months ago) docs: Fix link in README - Salim B
installed with:
mkdir build
cd build
cmake3 ..
make
make install
(didn't make shared library - might need to...)


swamp-cpp install:
https://gitlab.cern.ch/hgcal-daq-sw/serenity-daq/swamp-cpp

during swamp-cpp have to install hiredis before redis-plus-plus

more installs (from the serenity-toolbox install instructions, note serenity toolbox was not installed)
this includes enough yaml-cpp to make swamp-cpp compile:
dnf install make rpm-build gcc-c++ boost-devel-1.75.0 pugixml-devel-1.13 yaml-cpp-devel-0.6.3 python3.11-devel python3.11-pip cactuscore-uhal-* cactuscore-build-utils-0.3.5



Yu-Wei - talk to for DQM server
Izaak, and Pedro - logical mappings of the boards


## Bluetooth device:

didnt really need these:
bluez bluez-utils
dnf install bluez bluez-utils

suspect motherboards for LABC2 and LABC3 don't have bluetooth on them

useful commands:
lsmod | grep bluetooth

systemctl status bluetooth
(needed restart event when it was on to get the bluetoothd recognized)
systemctl restart bluetooth



## updating to EMP10

new firmware (with all quads setup) should use emp version 0.10

https://emp-fwk.web.cern.ch/sw/release/0.10/repos/el9/x86_64/

/etc/yum.repos.d/emp.repo

previusly used
https://emp-fwk.web.cern.ch/sw/release/0.9/repos/el9/x86_64/


did a make remove of
yum remove cactusboards-emp*
then yum install of the same command after changing the url in the .repo file.


rebuilt swamp-cpp in:
/root/swamp-cpp/build_emp10
with
cmake3 ..
make -j 20


