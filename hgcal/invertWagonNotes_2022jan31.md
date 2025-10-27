ssh HGCAL_dev@192.168.1.94

in raspberry pi changed:

from 
invert_gc_v2wagon=[1,1,1,1, 1,1,0,0, 0,0,1,1, 1,1,1,1]
invert_gc_v2wagon=[1,1,1,1, 0,0,0,0, 0,0,0,0, 0,0,0,0]




Hi Aidan,

What you wrote below about FC errors sounds like a problem we had just before the Christmas break, so I am forwarding a summary of the things that fixed it for us. In short, the FC data stream had inverted polarity when it was reaching some of the Hexa Controller Boards. So, we flipped the polarity by reconfiguring the lpgbt using the setup_lpgbt.py script. You will also see bellow how we made sure the external FC clock and data streams were selected and how we confirmed that the FC error counter is constant at the receiver(meaning FC errors are resolved). Note that some steps are done from the HC FW ("busybox" stuff) and some from the ZCU FW(executing the setup_lpgbt.py). However, you should make sure that you initialize both the ZCU and the HC firmware same as us first so check all the color-coded steps.
## setup the zcu
//ssh into the ZCU102
//Load the bitstream onto the zcu
cd fw
./do_load.sh bitstream_name.bit.xz
//Go into the software directory to play with various scripts
cd sw
./zcu_multitool.py --setrefclk // to set the reference clock in the BE GTH
./zcu_multitool.py --resetlink // reset the link twice (reasons unknown)
./zcu_multitool.py --resetlink
// good to go

 [root@hc646571]# fw-loader load interposerV2/
Previously loaded firmware: /opt/cms-hgcal-firmware/hgc-test-systems/interposerV2
Using bitstream: /opt/cms-hgcal-firmware/hgc-test-systems/interposerV2/interposer.bit
Using device tree overlay: /opt/cms-hgcal-firmware/hgc-test-systems/interposerV2/device-tree/pl.dtbo
Loading the bitstream took: 3.097s
Loaded the device tree overlay successfully using the zynqMP FPGA manager

 *N.B. Jon suggested that
ROCv3 version of the firmware exists, and interposerV2 corresponds to ROCv2(that is what we currently use)

Everything fits together now! :) The Fast commands errors are no longer an issue here. An intervention was indeed needed. All that had to be done was to set the polarity of the FC streams in the transmitter (DAQ-lpGBT) to normal (not inverted). That is for all 3 receivers (Hexa Controller Board Firmware) that we currently have in the setup. I did not change any handles on the receiver side. Some details bellow for one of the receivers as an example.

# From the ZCU BE, Setting the polarity of the appropriate FC DAQ lpGBT output port to be normal (not inverted)
./setup_lpgbt.py --protocol IC 
# Here, note that one must make an edit to the invert_gc_v2wagon=[1,1,1,1, 0,0,0,0, 0,0,0,0, 0,0,0,0]
# Above example reads: 
# ePorts 0,1,2,3 of eGroup0 are inverted
# ePorts 0,1,2,3 of eGroup1 are not inverted
# ePorts 0,1,2,3 of eGroup2 are not inverted
# ePorts 0,1,2,3 of eGroup3 are not inverted

# Checking if the external clock is being received
[root@hc646573 busybox-1.31.1]# ./busybox devmem 0x80060000
0x08001845 

# Selecting external sources for both the FC data stream and the clk320
[root@hc646573 busybox-1.31.1]# ./busybox devmem 0x80060000 32 0x00000000 

# Confirming that the FC error counter is constant
[root@hc646573 busybox-1.31.1]# ./busybox devmem 0x80050030; sleep 1;./busybox devmem 0x80050030
0x59132590
0x59132590

A sanity check in the two paragraphs bellow.

# Setting the polarity of the appropriate FC DAQ lpGBT output port to be *inverted*
./setup_lpgbt.py --protocol IC 
# Here, note that an edit of the setup_lpgbt.py is needed so that invert_gc_v2wagon=[1,1,1,1, 0,0,0,0, 0,1,0,0, 0,0,0,0]
# That inverts the polarity of ePort1 of eGroup2 

# Because we had a constant error counter value (0x59132590) before inversion, now we expect to see this counter to increase and keep increasing (not be constant)
[root@hc646573 busybox-1.31.1]# ./busybox devmem 0x80050030; sleep 1;./busybox devmem 0x80050030
0x880BF491
0x8A7242C7
# Which, indeed, is the case.

Hopefully, this helps with the FC errors. I have no experience with Link Reset nor the ~/source/test/clkSource script. 

And, regarding the I2C bus scan, this is what we exactly did: 

 On the zcu, setup the environment: 
[HGCAL_dev@umn-zcu102 ~]$ cd /home/HGCAL_dev/sw/gbt_sca_sw/
[HGCAL_dev@umn-zcu102 gbt_sca_sw]$ source env.sh 

 Then execute:
[HGCAL_dev@umn-zcu102 gbt_sca_sw]$ python3 gbtsca_bus_scan.py

And we did get a reply from one of the ECON-Ts on the West Wagon as I showed in my letter last week:

Note, the script scans only the West side of the Train and we had only 1 ECON-T connected.
Cheers,
Milos
