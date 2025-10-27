## DAQ meeting May 2:
- DESY: don't put the ethernet connection in to the wrong ethernet port - the voltages may not match and it is a bad idea - and it broke the tileboard tester
	- RJ45 - used for the trigger portal
	- 
	- solder blogs on the west side of the engine
	- hefty pins
	- east one
	- west everything can work
	- econT
- ROC v3 read out wiht the v3 trophy board
	- can read out data and i2c
	- pll to lock - needed for standard readout
	- best board was sent to - somewhere - and that won't happen until may
- Econ-T emulators
	- uncorrupted data in the zcu backend
	- capture is uncorrupted when data from the front 
	- a particular sfp cage --?
		- Andre - may be due to routing in the firmware....?
		- Jeremy says not likely
		- critical warnings in the design?
		- CI?
		- Engine design... Jon can only build these in the gitlab CI - he hasn't looked closely at the {missed word} outputs
			- Jon doesn't have a license
			- for the Kria's vivado version will need to be updated
			- a site license
			- how legal it is to use a remote service
				- logging in may be legal
		- all cages were tested by Jeremy
		- Jeremy - try a link trick is part of the system reproducing and capturing the signal 
			- link trick should be sfp dependent - pll in the sfp, pushing a raw 
			- analogue behavior is different in the different classes of sfp
			- amplify and pass through what they get
			- analogue line performance.
			- inherent zcu behavior ? Minnisota has a different version of the sfps
			- Jeremy would go in an use the wizard for this.
		- Andre - rate of errors is huge 
	- otherwise it is corrupted 
	- introducing a serenity - more realistic backend
	- perform the capture there
	- mini version of the stage 1 tpg algorithm - for one (or two) lpGBTs - full depth but not as wide
	- one link
	- fully process data 
	- engine v3...

- uHal discussion
	- 2 address ranges 
	- UIO may or may not do something
	- FCC file
	- one axi interface
	- Axi for , axi wide
	- capture block is the same what?
	- ipif interface 
	- axi lite
		- a separate block in the block design
	- simple extention
	- different memory maps
	- multiple maps
	- one uio with different maps

olivier - cooling tests
- SiPM 
- open top 
- rocv3 test boards
- open top HD VGA socket assembled on test boards
- using adcs on the test boards?
- don't have more details than that
- on the list
	- Arnaud - modifactions are very light
	- Andre - add them to firmware designs
	- Arnaud - more difficult than I though
	- Andre - someone with boards to map out where i2c access are
	- O: boards belong to Omega
	- schematics versus reality
	- Kivanc.... may be able to help

- There is a firmware address xml file
	- link-capture-axi-0 and axi-1
	- and axi-0 and axi-1 FIFO nodes
	- loaded the RPM
	- connections 
 
sis/class/IO
device tree is not matching 
bit file from something
haveing the software from RPM

- From Milos:
 
Aidan, I am using this version of ZCU fw:
Package zcu102-siengine-v1p0.noarch 0:2022.01.29.19.35.44-5bea77fa
And it requires adding connections.xml manually and also adding "backend" node manually in fw_block_addresses.xml


packet reset Econ T
trigger the capture
FC bits
econ T data is very scrambled
very hard to tell if it is aligned
need the aligned message
for user to look at?
data acquisition
don't use it for a work alignment
word alignment
it is also a consumer
link capture is used by firmware also
sync with the source.


not all of the clocks are being used in the firmware
backend clock



request from Milos:
[HGCAL_dev@umn-zcu102 ~]$ sudo fw-loader load zcu102-siengine-v1p0
Previously loaded firmware: /opt/cms-hgcal-firmware/hgc-test-systems/zcu102-siengine-v1p0 Using bitstream: /opt/cms-hgcal-firmware/hgc-test-systems/zcu102-siengine-v1p0/zcu102-siengine-v1p0.bit Using device tree overlay: /opt/cms-hgcal-firmware/hgc-test-systems/zcu102-siengine-v1p0/device-tree/pl.dtbo Loading the bitstream took: 12.523s Loaded the device tree overlay successfully using the zynqMP FPGA manager 
[HGCAL_dev@umn-zcu102 ~]$ ls /dev/uio*
/dev/uio0 /dev/uio1 /dev/uio2 /dev/uio3 
[HGCAL_dev@umn-zcu102 ~]$ sudo rmmod uio_pdrv_genirq 
[HGCAL_dev@umn-zcu102 ~]$ sudo insmod /lib/modules/4.19.0-xilinx-v2019.2/kernel/drivers/uio/uio_pdrv_genirq.ko of_id="linux,uio-pdrv-genirq"

_A sanity check_ - The bellow command should return the below output: 
[HGCAL_dev@umn-zcu102 fw]$ ls /dev/uio*
/dev/uio0 /dev/uio10 /dev/uio12 /dev/uio14 /dev/uio3 /dev/uio5 /dev/uio7 /dev/uio9 /dev/uio1 /dev/uio11 /dev/uio13 /dev/uio2 /dev/uio4 /dev/uio6 /dev/uio8

ls /dev/uio* needs to return what is above, it is very important