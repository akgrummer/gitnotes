ECON-SW
=======
## Getting started:
- *Libraries to compile software*:
    ```bash
    sudo yum -y install epel-release
    yum install epel-release
    yum update
    yum install cmake zeromq zeromq-devel cppzmq-devel libyaml libyaml-devel yaml-cpp yaml-cpp-devel boost boost-devel python3 python3-devel autoconf-archive pugixml pugixml-devel
    pip3 install pyzmq pyyaml smbus2 nested_dict --user
    ```
- *Clone repository*:
    ```bash
    # clone repository in `src/` folder or other working directory:
    git clone --recursive git@github.com:cmantill/econt_sw.git
    # to update submodules
    cd econt_sw/
    git submodule --init --recursive
    ```
- *uHal*: Visit https://gitlab.cern.ch/hgcal-daq-sw/ipbus-software
    ```bash
    # go into econt_sw directory
    cd econt_sw/
    # install libraries
    sudo yum install boost boost-devel
    sudo yum -y install epel-release
    sudo yum install pugixml-devel pugixml
    # numpy
    sudo yum install python-pip
    sudo yum install python-devel
    sudo yum groupinstall 'development tools'
    sudo pip install future
    sudo pip install numpy==1.9
    # clone ipbus-software
    git clone ssh://git@gitlab.cern.ch:7999/hgcal-daq-sw/ipbus-software.git
    cd ipbus-software/
    git checkout asteen/UIO-hgcal-dev 
	# ONLY FOR PYTHON 2 - see instructions for python 3 below
    # compile uHal
    make -j2 Set=uhal
    make install -j2 Set=uhal
    ```
- *python3 compatible uhal installation*
   If compiling to python3 instead of python2, do not checkout the `asteen/UIO-hgcal-dev` branch, but stick to the default `hgcal-uio` branch from the `hgcal-daq-sw/ipbus-software.git` repository.  Additionally, the `pybind11` libraries need to be installed:
   repo also exists here: 
   origin	https://gitlab.cern.ch/asteen/ipbus-software.git
	pastika	https://gitlab.cern.ch/pastika/ipbus-software.git
    ```
	sudo pip3 install "pybind11[global]"
    ```
    The Makefiles need to be updated in a couple of spots to build the python3 bindings instead of defaulting to python2
    In `config/Makefile.macros`, line 8, change `python` to `python3`
		```
	    -PYTHON ?= python
	    +PYTHON ?= python3
		```
	
and in uhal/Makefile, lines 22:
	```
	PACKAGES := $(filter-out python, $(PACKAGES))
	PACKAGES := $(filter-out python3, $(PACKAGES))
	```
and line 57:
	```
	-PYTHON ?= python
	+PYTHON ?= python3
	```


Then, finally, compile:
    ```
    # compile uHal
    sudo make -j2 Set=uhal
    sudo make install -j2 Set=uhal
    ```
## Install:
- **Basic installation of econt-sw on Zynq Trenz module**:
    ```bash
    # go to main directory in econt-sw
    cd econt-sw/econt-sw/
    # source libraries
    source env.sh
    # compile 
    mkdir build
    cd build
    cmake ../
    make install
    cd ../
    ```
## Firmware:
- **To re-load new firmware**:
    ```bash
    # go to mylittledt directory
    cd ${MYLITTLEDT}
    cd /home/HGCAL_dev/src/mylittledt/
    # load firmware and set permissions
    sudo ./load.sh ${FIRMWARE_FOLDER}   && sudo chmod a+rw /dev/uio* /dev/i2c-*
    ```
    In HGCAL_dev board:
    ```
    ${MYLITTLEDT} = /home/HGCAL_dev/src/mylittledt/
    ${FIRMWARE_FOLDER} = econ-t-IO-Aug12
    ```
    
    In emulator-to-emulator setup:
    ```
    ${MYLITTLEDT} =  /home/HGCAL_dev/mylittledt/
    ${FIRMWARE_FOLDER} ASIC: `~/firmware/econ-t-emu-solo-Nov12/
    ${FIRMWARE_FOLDER} TESTER: `~/firmware/econ-t-tester-Nov12/
    ${FIRMWARE_FOLDER} ASIC: `~/firmware/econ-t-tester2-Dec3/
    ```
    To check the version of the firmware:
    ```
    # check which version of the firmware was loaded
    cat /sys/firmware/devicetree/base/fpga-full/firmware-name
    # find out the specific git commit on which the firmware was built
    cat /sys/firmware/devicetree/base/fpga-full/git-desc
    cat /sys/firmware/devicetree/base/fpga-full/git-sha    
    ```
- **When loading new firmware**:
    Need to link `address_table` directory. Default `fw_block_addresses.xml` files are available in the `econt_sw/econt_sw/address_table_reference_*/` directories for comparison.
    ```
    sudo ln -s /opt/hexactrl/uHAL_xml address_table
    ```    
### ZYNQ ECON-T testers:
To fix the IP address one can change the setup on `/etc/dhcp/dhcpd.conf` on the desktop that manages the dchp server.
See more instructions on hexactrl_setup.md
```
# On 14WH
ssh -K hcalpro@cmsnghcal01.fnal.gov
# econ-board 3
ssh HGCAL_dev@192.168.1.45   
# econ-board 2
ssh HGCAL_dev@192.168.1.48
# Outside
# hgcal-dev (from Jon)
ssh -p 23 HGCAL_dev@wilsonjc.us
```
### Communicating with hexactrl
All of the testing scripts use python3 uhal and can be run directly when logged in to the hexa-controller.
To control remotely:
1. In remote desktop, forward port to hexacontroller, e.g. for port 6677:
```
ssh -L 6677:localhost:6677 HGCAL_dev@192.168.1.48
```
2. In hexacontroller, run `zmq_server.py` with that IP address:
```
python testing/zmq_server.py --server 6677
```
3. In remote desktop, run `zmq_client.py` or script that calls the zmq server with that IP address:
```
python testing/zmq_client.py --server 6677
```
Alternatively, define `daq_controller` in `zmq_controller`. Such that all testing scripts communicate with daq_controller (similar to what i2c.py does).
### Slow control
- We use a zmq_server to start the [econ_interface](https://github.com/cmantill/econt_sw/blob/master/econt_sw/zmq_i2c/econ_interface.py) class.
- To start the server:
  ```
  # start server for i2c with asic
  cd zmq_i2c/
  python3 zmq_server.py --addr ADDRESS --server SERVER
  ```
- To interact with the econ_interface class one can use [testing/i2c.py](https://github.com/cmantill/econt_sw/blob/master/econt_sw/testing/i2c.py). This follows the following structure:
  ```
  for key in server.keys():
      i2c_sockets[key] = i2cController("localhost", str(server[key]))
      # to initialize
      i2c_sockets[key].initialize()
      # to update yaml config
      i2c_sockets[key].update_yamlConfig(yamlNode=new_config)
      # to configure
      i2c_sockets[key].configure()
      # to read values from yaml file and compare
      i2c_read = i2c_sockets[key].read_and_compare()
  
      # to read values
      read_socket = i2c_sockets[key].read_config(yamlNode=new_config)
    # terminate i2c servers
    for key,proc in procs.items():
        proc.terminate()
  ```
  - Examples of using the i2c.py script:
    Add `--quiet` if you do not want printouts
    - With a yaml file
      ```
      # To read the registers in a yaml file
      python3 testing/i2c.py --yaml configs/align.yaml
      ```
    - With specific register:
      ```
      # To read a specific register given access,block,register_name
      python3 testing/i2c.py --i2c ASIC --addr 0 --server 5554  --rw RW --block ALIGNER_ALL --register orbsyn_cnt_snapshot
      
      ```
    - To match the name with [ECON_i2c_dict.json](https://github.com/cmantill/econt_sw/blob/master/econt_sw/zmq_i2c/reg_maps/ECON_I2C_dict.json)
      ```
      # To read all header mis-match counters from ALIGNER block
      python3 testing/i2c.py --name CH_ALIGNER*hdr_mm_cntr
      # or
      python3 testing/i2c.py --name CH_ALIGNER[0-11]_hdr_mm_cntr
      # or
      python3 testing/i2c.py --name CH_ALIGNER[0-2]_hdr_mm_cntr
      ```
    - To list all the matching names in the json file:
      ```
      python3 testing/i2c.py --name CH_ALIGNER* --list
      ```
  - IMPORTANT: To write use all the above options but add `--write`.
- To start default serves for ASIC and emulator see [startServers.sh](https://github.com/cmantill/econt_sw/blob/master/econt_sw/zmq_i2c/startServers.sh).


# Added by Aidan:
```bash
sudo pip3 install Cython
sudo pip3 install numpy
#  -- skipped this - took a long time on zcu: sudo pip3 install pandas
sudo pip3 install tabulate
```

on ZCU did this:
```bash
pip3 install Cython --user
pip3 install pandas --user
```


## Configuration for pseudo Econ D
The following process should be use to configure the pseudo-ECON-d.

initial config (of ROCs):
```bash
./uhal_string.py -b ctrl_gpio --node direction.roc_rstb --val 7
./uhal_string.py -b ctrl_gpio --node direction.roc_rstb_i2c --val 7
./uhal_string.py -b ctrl_gpio --node direction.roc_resyncLoad --val 7
./uhal_string.py -b ctrl_gpio --node direction.roc_pwrEnable --val 7

./uhal_string.py -b ctrl_gpio --node direction.roc_rstb --val 0
./uhal_string.py -b ctrl_gpio --node direction.roc_rstb_i2c --val 0
./uhal_string.py -b ctrl_gpio --node direction.roc_resyncLoad --val 0
./uhal_string.py -b ctrl_gpio --node direction.roc_pwrEnable --val 0
```

Octal input does not work in the code yet...
```bash
./uhal_string.py -b ctrl_gpio --node data --val 07077
./uhal_string.py -b ctrl_gpio --node data --val 07777
./uhal_string.py -b ctrl_gpio --node data --val 07077

# intead can use:
./uhal_string.py -b ctrl_gpio --node data --val 3647
./uhal_string.py -b ctrl_gpio --node data --val 4095
./uhal_string.py -b ctrl_gpio --node data --val 3647
```
```bash
# set roc config with the devmem 
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060004
0xFFFFFFFF
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060004 32 0xFFFFF000
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060004
0xFFFFF000
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060000 32 0x08001E3F
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060000 32 0x08001FFF
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060000 32 0x08001E3F
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060000
0x08007E3F
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060000 32 0x08001E3F
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060000
0x08007E3F
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060000 32 0x08001FFF
[agrummer@hexactr-90]$ sudo ~/devmem 0x80060000
0x08007FFF


sudo ~/devmem 0x80060004

sudo ~/devmem 0x80060004 32 0xFFFFF000
sudo ~/devmem 0x80060004

sudo ~/devmem 0x80060000

sudo ~/devmem 0x80060000 32 0x08001E3F
sudo ~/devmem 0x80060000

sudo ~/devmem 0x80060000 32 0x08001FFF
sudo ~/devmem 0x80060000

sudo ~/devmem 0x80060000 32 0x08001E3F
sudo ~/devmem 0x80060000
```

1.  Set passthrough bit in readout manager to 1
this is already the state after running sudo source/test/interposer
```bash
./uhal_string.py --block ro --node passthrough --val 1
```
2.  Enable auto bit alignment mode in link_capture for all links
- don't know the exact command - but looks like it is commented in one of Joe's scripts - and the addresses seem similar to
- these also seem to be set to 1 already
```bash
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.reg0.delay_mode
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.reg0.delay_mode
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link2.reg0.delay_mode
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link3.reg0.delay_mode
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link4.reg0.delay_mode
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link5.reg0.delay_mode

# set values:
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.reg0.delay_mode --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.reg0.delay_mode --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link2.reg0.delay_mode --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link3.reg0.delay_mode --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link4.reg0.delay_mode --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link5.reg0.delay_mode --val 1

./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.reg0.delay_mode --val 0
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.reg0.delay_mode --val 0
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link2.reg0.delay_mode --val 0
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link3.reg0.delay_mode --val 0
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link4.reg0.delay_mode --val 0
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link5.reg0.delay_mode --val 0
```
- IO block settings
```bash
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.reg0.delay_set
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.reg0.delay_set
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link2.reg0.delay_set
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link3.reg0.delay_set
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link4.reg0.delay_set
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link5.reg0.delay_set

./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node global.global_reset_counters --val 1
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node global.global_latch_counters --val 1

./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.bit_counter
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.bit_counter
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link2.bit_counter
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link3.bit_counter
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link4.bit_counter
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link5.bit_counter

./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.error_counter
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.error_counter
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link2.error_counter
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link3.error_counter
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link4.error_counter
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link5.error_counter

./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.reg3.delay_out
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.reg3.delay_out
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link2.reg3.delay_out
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link3.reg3.delay_out
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link4.reg3.delay_out
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link5.reg3.delay_out

# reading the eye width
Housekeeping-FastControl-FC-control.clk_int_select
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link0.reg3.delay_out_N
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.reg3.delay_out_N
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link2.reg3.delay_out_N
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link3.reg3.delay_out_N
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link4.reg3.delay_out_N
./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link5.reg3.delay_out_N

```
3.a (OR THIS STEP CAN COME AFTER 3) send align the idle the patterns on the input block
```bash
./uhal_string.py -b in --links explicit_align --val 1
```
3.  Send "link reset" fast command to trigger link alignment
- doesn't seem to be working from the hexacontroller:
```bash
./uhal_string.py --block Housekeeping-FastControl-fastcontrol-axi-0 --node command.link_reset --val 1
wait
./uhal_string.py --block Housekeeping-FastControl-fastcontrol-axi-0 --node command.link_reset --val 0
./uhal_string.py --block Housekeeping-FastControl-fastcontrol-axi-0 --node  counters.link_reset


# actually -- send a link reset from zcu:
# and then read it on hexa:
./uhal_string.py -b Housekeeping-FastControl-fastcontrol-v2-decod-0 --node link_reset_count
./uhal_string.py -b Housekeeping-FastControl-fastcontrol-v2-decod-0 --node l1a_count
```
FOR ROCv3:
```bash

./uhal_string.py --b fc --node request.count_rst --val 1
# no reset for link_reset counters in the fc rec block
# don't know what this does;
# ./uhal_string.py --b fcrec --node command.reset_counters_io --val 1
# on ZCU
./uhal_string.py -b fc --node request.link_reset_rocd --val 1
./uhal_string.py -b fc --node counters.link_reset_rocd
./uhal_string.py -b fc --node request.link_reset_econd --val 1
./uhal_string.py -b fc --node counters.link_reset_econd
#on hexaCntl:
./uhal_string.py -b fcrec --node counters.link_reset_rocd
./uhal_string.py -b fcrec --node counters.link_reset_econd
```
```bash
./uhal_string.py -b in --node global.explicit_align --val 1
./uhal_string.py -b in --node global.explicit_align --val 0
```
```bash
# trying to align output links:
./uhal_string.py --block ro --node passthrough --val 0
./uhal_string.py --block in --links L1A_offset_or_BX --val 25
./uhal_string.py --block ro --node enable_dual_output --val 1
./uhal_string.py --block in --node global.continous_acquire --val 63
./uhal_string.py --block in --node global.continous_acquire --val 0
# then send a link reset from zcu
```
4.  Set link_capture latency buffer delays to align any offset in input eLinks
not sure if this should actually be the latency on the output block 1, but probably we are configuring the input block first
```bash
./uhal_string.py --block in --links fifo_latency --val 13
# or 
./uhal_string.py --block in --links L1A_offset_or_BX --val 14
./uhal_string.py --block in --links L1A_offset_or_BX --val 9

# check in mode L1A capture (2):
./uhal_string.py --block in --links capture_mode_in --val 2

./uhal_string.py --block in --node global.continous_acquire --val 0
./uhal_string.py --block in --links explicit_rstb_acquire --val 0

./uhal_string.py -b in --node global.aquire --val 1
./uhal_string.py --fifo in
```
4.5 reset the alignment pattern on the output block
```bash
# ./uhal_string.py -b out --node link0.align_pattern --val 2899102912
# ./uhal_string.py -b out --node link1.align_pattern --val 2899102912
./uhal_string.py -b out --links align_pattern --val 2899102912
./uhal_string.py -b out --links align_pattern --myhex
```
4.5.5 also requires a link align (sometimes)
```bash
./uhal_string.py -b out --node global.explicit_align --val 1
```

5.  Set passthrough bit in readout manager to 0
```bash
./uhal_string.py --block ro --node passthrough --val 0
```
6.  Set capture mode to "AutoDAQ" for all links in link_capture
```bash
./uhal_string.py --block in --links capture_mode_in --val 3
```
7.  Set acquire length and spy length to 39 for all links in link_capture
```bash
./uhal_string.py --block in --links aquire_length --val 39 
./uhal_string.py --block in --links total_length --val 39 
./uhal_string.py -b ro --node num_words --val 39
./uhal_string.py --block in --links aquire_length --val 40 
./uhal_string.py --block in --links total_length --val 40 
```
8.  Set link_enable enable_output1 as desired in the readout manager
this should probably be done before step 5 .. unless there is a force idles fast command, or link reset fast command to get block 1 out of align state 3
```bash
./uhal_string.py --block ro --node enable_dual_output --val 1
```
9.  Set "global continuous acquire" in link capture to same setting as "link_enable" setting in readout manage
```bash
./uhal_string.py --block in --node global.continous_acquire
./uhal_string.py --block ro --node link_enable
./uhal_string.py --block in --node global.continous_acquire --val 63

./uhal_string.py --block in --links explicit_rstb_acquire --val 0

```


```bash
./uhal_string.py -b out --links capture_mode_in --val 2
./uhal_string.py --block out --node global.continous_acquire --val 3
```

```bash
./uhal_string.py -b in --node global.aquire --val 1
./uhal_string.py --fifo in

./uhal_string.py -b in --node global.aquire --val 0

./uhal_string.py -b out --node global.aquire --val 1
./uhal_string.py -b out --node global.aquire --val 0
```

```bash
./uhal_string.py -b out --node global.explicit_align --val 1
./uhal_string.py -b out --node global.explicit_align --val 0
```


recipe:
set latency to 25,
and offset to 0
then send a link reset from zcu 

can disable links:
```bash
./uhal_string.py -b out --node global.link_enable.link1
```


pll settings need to be sent to ROC
in auto delay mode - delay_out_N shows you the eye ...
delay_out_N will normally show you the negative side of the receiver (for block input) or transeiver

./uhal_string.py -b out --links link0.align_pattern --myhex
./uhal_string.py -b out --node link0.align_pattern --myhex
for accccccc0
```bash
# ./uhal_string.py -b out --node link0.align_pattern --val 2899102912
# ./uhal_string.py -b out --node link1.align_pattern --val 2899102912
./uhal_string.py -b out --links align_pattern --val 2899102912
./uhal_string.py -b out --links align_pattern --myhex
```
for accccc080
./uhal_string.py -b out --node link0.align_pattern --val 2899099776

./uhal_string.py -b out --links aquire_length --val 500

```bash
# acquire out block
./uhal_string.py -b out --links aquire_length --val 500
./uhal_string.py -b out --node global.aquire --val 1
./uhal_string.py -b out --node global.aquire --val 0
```

./uhal_string.py -b ro --node link_enable --val 0

./uhal_string.py -b in --links aquire_length --val 39
./uhal_string.py -b in --links total_length --val 39

./uhal_string.py -b out --links aquire_length --val 1024

```bash
#acquire
./uhal_string.py -b in --node global.aquire --val 1
./uhal_string.py -b in --node global.aquire --val 0
```


reset links:
./uhal_string.py -b in --links explicit_rstb_acquire --val 1 
./uhal_string.py -b in --links explicit_rstb_acquire --val 0
./uhal_string.py -b in --links explicit_rstb_acquire --val 1 


depth of the fifo is:
./uhal_string.py -b out --node global.bram_size

reset link:
link4.explicit_rstb_acquire


to disable a link: set this to 0:
status.waiting_for_trig
which means set the continutous_aquire in the input block to the correct value - 1111111=63 or 110111 = 55
and the link_enable to t
```bash
./uhal_string.py --block in --node global.continous_acquire --val 54
./uhal_string.py --block ro --node link_enable --val 54
./uhal_string.py --block in --links explicit_rstb_acquire --val 1
./uhal_string.py --block in --links explicit_rstb_acquire --val 0
./uhal_string.py --block in --links explicit_rstb_acquire --val 1
```

```bash
./uhal_string.py -b out --links explicit_rstb_acquire --val 1
./uhal_string.py -b out --links explicit_rstb_acquire --val 0
./uhal_string.py -b out --links explicit_rstb_acquire --val 1
```

```bash
# for backend
./uhal_string.py -s
./uhal_string.py --links align_pattern --val 2899102912
./uhal_string.py --links align_pattern --myhex
# might need:
./uhal_string.py --node global.explicit_align --val 1
./uhal_string.py -s
./uhal_string.py --links aquire_length --val 300
./uhal_string.py --node global.aquire --val 1
./uhal_string.py --node global.aquire --val 0
./uhal_string.py --fifo
./uhal_string.py --links capture_mode_in --val 2
#  select acquire number based on enabled links
./uhal_string.py --node global.continous_acquire --val 63

./uhal_string.py --links explicit_rstb_acquire --val 1
./uhal_string.py --links explicit_rstb_acquire --val 0
./uhal_string.py --links explicit_rstb_acquire --val 1
```
to configure backend:
```bash
./uhal_string.py --links align_pattern --val 2899102912
./uhal_string.py --links align_pattern --myhex
./uhal_string.py --node global.explicit_align --val 1

./uhal_string.py --links aquire_length --val 300
./uhal_string.py --links capture_mode_in --val 2
./uhal_string.py --node global.continous_acquire --val 63

```

```bash
sudo fw-loader load interposer-ROCv2
sudo rmmod uio_pdrv_genirq
sudo insmod /lib/modules/4.19.0-xilinx-v2019.2/kernel/drivers/uio/uio_pdrv_genirq.ko of_id="linux,uio-pdrv-genirq"
```



check if you see an external clk:
```bash
./uhal_string.py -b Housekeeping-FastControl-FC-control --node clk_int_select
clk_int_select: 0
./uhal_string.py -b Housekeeping-FastControl-FC-control --node FC_int_select
FC_int_select: 0
./uhal_string.py -b Housekeeping-FastControl-FC-control --node ext_clk_active
ext_clk_active: 1
```


ROC config:
from `/home/agrummer/hexactrl-sw/zmq_i2c` on hexaE1
```
python3 configure_rocs.py -d hb -i localhost -f configs/initLD.yaml --i2cPort 5555
```
git submodule update --remote

## Main Issues with ROC config sw:
1. IO read and write errors in ROC.py - recursion is just stuck, but works on second run
	```bash
	[agrummer@hexactr-95]$ python3 zmq_client.py 
	[roc_s0] Configured
	[roc_s1] Configured
	IOError in write. Attempting re-write. In ROC:  0 roc_s2
	IOError in write. Attempting re-write. In ROC:  1 roc_s2
	IOError in read. Attempting re-read.
	ERROR in configure:  unsupported operand type(s) for &: 'NoneType' and 'int'
	[roc_s0] GPIO reset
	[roc_s1] GPIO reset
	[roc_s2] GPIO reset
	[roc_s0] Configured
	[roc_s1] Configured
	[roc_s2] Configured
	```
2. ROCs have to be reset manually for I2Cs to work
	```bash
	sudo ~/devmem 0x80060004
	
	sudo ~/devmem 0x80060004 32 0xFFFFF000
	sudo ~/devmem 0x80060004
	
	sudo ~/devmem 0x80060000
	
	sudo ~/devmem 0x80060000 32 0x08001E3F
	sudo ~/devmem 0x80060000
	
	sudo ~/devmem 0x80060000 32 0x08001FFF
	sudo ~/devmem 0x80060000
	
	sudo ~/devmem 0x80060000 32 0x08001E3F
	sudo ~/devmem 0x80060000
	```
3. configure_rocs.py fails - wrong pairs are sent
	```bash
	[agrummer@hexactr-95]$ python3 configure_rocs.py 
	{'dut': 'hb', 'hexaIP': 'localhost', 'configFile': './configs/initLD.yaml', 'i2cPort': '5555', 'initialize': False}
	[roc_s1] Configured
	[roc_s0] Configured
	[roc_s2] Configured
	IOError in write. Attempting re-write. In ROC:  0 roc_s2
	IOError in read. Attempting re-read.
	IOError in read. Attempting re-read.
	... this error is repeated ~100 times
	Traceback (most recent call last):
	  File "zmq_server.py", line 36, in <module>
	    elif string == "read": redirect(board.read)
	  File "zmq_server.py", line 17, in redirect
	    ans_yaml = fn(cfg_yaml)
	  File "/home/agrummer/hexactrl-sw/zmq_i2c/Boards.py", line 62, in read
	    else: return self.__read_fr_cache()
	  File "/home/agrummer/hexactrl-sw/zmq_i2c/Boards.py", line 87, in __read_fr_cache
	    rd_cfg = self.translator.cfg_from_pairs(rd_pairs)
	  File "/home/agrummer/hexactrl-sw/zmq_i2c/Translator.py", line 40, in cfg_from_pairs
	    paramVal = self.__paramVal_from_regVal(reg, pairs[addr], prev_regVal)
	  File "/home/agrummer/hexactrl-sw/zmq_i2c/Translator.py", line 129, in __paramVal_from_regVal
	    param_val = reg_value & reg["reg_mask"]
	TypeError: unsupported operand type(s) for &: 'NoneType' and 'int'
	
	^CTraceback (most recent call last):
	  File "configure_rocs.py", line 54, in <module>
	    print( yaml.dump(i2csocket.read_config()) )
	  File "/home/agrummer/hexactrl-sw/hexactrl-script/zmq_controler.py", line 95, in read_config
	    yamlread = yaml.safe_load( self.socket.recv_string() )
	  File "/usr/local/lib64/python3.6/site-packages/zmq/sugar/socket.py", line 592, in recv_string
	    msg = self.recv(flags=flags)
	  File "zmq/backend/cython/socket.pyx", line 791, in zmq.backend.cython.socket.Socket.recv
	  File "zmq/backend/cython/socket.pyx", line 827, in zmq.backend.cython.socket.Socket.recv
	  File "zmq/backend/cython/socket.pyx", line 186, in zmq.backend.cython.socket._recv_copy
	  File "zmq/backend/cython/checkrc.pxd", line 13, in zmq.backend.cython.checkrc._check_rc
	KeyboardInterrupt
	```
	are you able to print the pairs? or if the server is killed is it not possible
4. new error when running zmq_client:
	```bash
	File "zmq_server.py", line 36, in <module>
	    elif string == "read": redirect(board.read)
	  File "zmq_server.py", line 17, in redirect
	    ans_yaml = fn(cfg_yaml)
	  File "/home/agrummer/hexactrl-sw/zmq_i2c/Boards.py", line 62, in read
	    else: return self.__read_fr_cache()
	  File "/home/agrummer/hexactrl-sw/zmq_i2c/Boards.py", line 87, in __read_fr_cache
	    rd_cfg = self.translator.cfg_from_pairs(rd_pairs)
	  File "/home/agrummer/hexactrl-sw/zmq_i2c/Translator.py", line 40, in cfg_from_pairs
	    paramVal = self.__paramVal_from_regVal(reg, pairs[addr], prev_regVal)
	  File "/home/agrummer/hexactrl-sw/zmq_i2c/Translator.py", line 129, in __paramVal_from_regVal
	    param_val = reg_value & reg["reg_mask"]
	TypeError: unsupported operand type(s) for &: 'NoneType' and 'int'
	```

## Check delay ready:
`./uhal_string.py --block ECON-d-to-ECOND-IO-IO-blocks-0 --node link1.reg3.delay_ready`
there is a link reset in the io blocks
you can also invert the link in the io blocks



## Fast commands for ROCv3
```bash
./uhal_string.py -b fastcontrol-axi-0.periodic0 --ls
./uhal_string.py --atts fastcontrol-axi-0.periodic0.flavor
./uhal_string.py --b fastcontrol-axi-0.periodic0 --node flavor --val 0
```

```bash
./uhal_string.py --b fastcontrol-axi-0 --node counters.errors
./uhal_string.py --b fastcontrol-axi-0 --node counters.l1a_suppressed
./uhal_string.py --b fastcontrol-axi-0 --node counters.bx_suppressed
./uhal_string.py --b fastcontrol-axi-0 --node counters.l1a
./uhal_string.py --b fastcontrol-axi-0 --node counters.l1a_nzs
./uhal_string.py --b fastcontrol-axi-0 --node counters.orbit_sync
./uhal_string.py --b fastcontrol-axi-0 --node counters.orbit_count_reset
./uhal_string.py --b fastcontrol-axi-0 --node counters.internal_calibration_pulse
./uhal_string.py --b fastcontrol-axi-0 --node counters.external_calibration_pulse
./uhal_string.py --b fastcontrol-axi-0 --node counters.chipsync
```


```bash
./uhal_string.py --b fastcontrol-axi-0 --node periodic0.enable
./uhal_string.py --b fastcontrol-axi-0 --node periodic0.request
./uhal_string.py --b fastcontrol-axi-0 --node periodic0.flavor
./uhal_string.py --b fastcontrol-axi-0 --node periodic0.enable_follow
./uhal_string.py --b fastcontrol-axi-0 --node periodic0.follow_which
./uhal_string.py --b fastcontrol-axi-0 --node periodic0.bx
./uhal_string.py --b fastcontrol-axi-0 --node periodic0.orbit_prescale
./uhal_string.py --b fastcontrol-axi-0 --node periodic0.burst_length
```

```bash
./uhal_string.py --b fastcontrol-axi-0 --node command.enable_fast_ctrl_stream
./uhal_string.py --b fastcontrol-axi-0 --node command.global_l1a_enable
```


count reset:
```bash
./uhal_string.py --b fastcontrol-axi-0.request --node count_rst --val 1
./uhal_string.py --b fc --node counters.l1a
```

```bash
./uhal_string.py -b fc --node request.link_reset_rocd --val 1
./uhal_string.py -b fc --node counters.link_reset_rocd

./uhal_string.py -b fc --node request.link_reset_econd --val 1
./uhal_string.py -b fc --node counters.link_reset_econd

./uhal_string.py -b fcrec --node counters.link_reset_rocd
./uhal_string.py -b fcrec --node counters.link_reset_econd


./uhal_string.py --b fc --node periodic0.enable
./uhal_string.py --b fc --node periodic0.enable --val 1
 ./uhal_string.py --b fc --node command.global_l1a_enable
./uhal_string.py --b fc --node command.global_l1a_enable --val 1
./uhal_string.py --b fc --node command.global_l1a_enable --val 0
```


```bash
./uhal_string.py --b fc --node command.global_l1a_enable --val 1
./uhal_string.py --b fc --node periodic0.request --val 1
./uhal_string.py -b fc --node counters.l1a
./uhal_string.py --b fc --node command.global_l1a_enable --val 0
```
to view fc on hexa controller need to use the fcrec block
```bash
./uhal_string.py -b fc --node counters.l1a
./uhal_string.py -b fcrec --node counters.l1a
```


## GPIO lines:
```
line name is:  S1_RSTB 
line name is:  S2_RSTB 
line name is:  S3_RSTB 

line name is:  S1_I2C_RST 
line name is:  S2_I2C_RST 
line name is:  S3_I2C_RST 

line name is:  S1_RESYNCLOAD 
line name is:  S2_RESYNCLOAD 
line name is:  S3_RESYNCLOAD 

line name is:  S1_PWR_EN 
line name is:  S2_PWR_EN 
line name is:  S3_PWR_EN 

line name is:  S1_PWR_PG 
line name is:  S2_PWR_PG 
line name is:  S3_PWR_PG 

line name is:  S1_ERROR_R 
line name is:  S2_ERROR_R 
line name is:  S3_ERROR_R 

line name is:  clk_ext_active 
line name is:  CFGRSTB_HGCROC 
line name is:  RSTB_HARD_ECON 
line name is:  RSTB_SOFT_ECOND 
line name is:  RSTB_SOFT_ECONT 
```


Programs set up on linux machines:
```
yum install -y xorg-x11-server-Xorg xorg-x11-xauth xorg-x11-apps
https://prasadlinuxblog.wordpress.com/2018/05/29/how-configure-x11-forwarding-in-centos-rhel-6-7/
```


# installing python3 on ZCU102
openssl instructions:
https://help.dreamhost.com/hc/en-us/articles/360001435926-Installing-OpenSSL-locally-under-your-username
actually, using these instructions now:
https://gist.github.com/fernandoaleman/5459173e24d59b45ae2cfc618e20fe06
! have to use `make` not `make -j2`

installed: 
```
yum install -y make gcc perl-core pcre-devel wget zlib-devel
```

needs to be version 1.1.1
added to bash profile:
```bash
export PATH=$HOME/openssl/bin:$PATH
export LD_LIBRARY_PATH=$HOME/openssl/lib  
export LC_ALL="en_US.UTF-8"  
export /LDFLAGS="-L /home/agrummer/openssl/lib -Wl,-rpath,/home/agrummer/openssl/lib"
```

make python3.10 has to have these instructions(https://github.com/actions/setup-python/issues/93):
```
1. first install openssl, please refer to [this page](https://help.dreamhost.com/hc/en-us/articles/360001435926-Installing-OpenSSL-locally-under-your-username)

2. install python and `./configure --with-openssl=/home/username/openssl`

3. at last, run `python3 -m ssl` and nothing outputs, it's ok.
```
## For python3.10 install instructions, followed something similar to: 
yum install doesn't work - because the epel rpm only goes up to python3.6

note - will need the openssl ./configure step above for correct pip3 behavior
https://linuxstans.com/how-to-install-python-centos/
yum install openssl-devel bzip2-devel libffi-devel
also see:
https://www.atlantic.net/dedicated-server-hosting/how-to-install-python-3-10-on-oracle-linux-8/

on hcalpro:
used (similar instructions to above):
https://www.liquidweb.com/kb/how-to-install-python-3-on-centos-7/
and got version Python-3.9.13 from python.org
this version should be compatible with the openssl version on hcalpro
note: need to use sudo for the make altinstall
python3.9 now exists in:
/usr/local/bin/python3.9

the other python versions exist in:
/usr/bin/

```bash
WARNING: The script pip3.9 is installed in '/usr/local/bin' which is not on PATH.
Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

Successfully installed pip-22.0.4 setuptools-58.1.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```

## Working in a virtual environment for python3.9
https://docs.python.org/3/tutorial/venv.html

## install python3.9 on ZCU:
```bash
# https://www.liquidweb.com/kb/how-to-install-python-3-on-centos-7/
wget https://www.python.org/ftp/python/3.9.15/Python-3.9.15.tgz
tar -xzf Python-3.9.15.tgz
cd Python-3.9.15/
./configure --enable-optimizations
make altinstall
```
Messages:
```bash
Installing collected packages: setuptools, pip
  WARNING: The script pip3.9 is installed in '/usr/local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-22.0.4 setuptools-58.1.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
```

## hexactrl sw
- cmake makes the Makefile
- then compile with make
- then install with make install
- then cpack - I think this step creates the rpm...?

Setting the branch name in the cmake
```bash
mkdir build
chdir build
cmake -DBUILD_CLIENT=ON -DROOT_INCLUDE_DIRS=/usr/include/root -DBRANCH_NAME=ROCv3 -DCMAKE_INSTALL_PREFIX=/opt/hexactrl/ROCv3 ../
make -j2
```

for server:
adding root libraries in the server build
```bash
mkdir build
chdir build
cmake -DBUILD_CLIENT=OFF -DROOT_INCLUDE_DIRS=/usr/include/root -DBRANCH_NAME=ROCv3 -DCMAKE_INSTALL_PREFIX=/opt/hexactrl/ROCv3 ../
make -j2
```

```bash
g++ demo2.cxx $(root-config --glibs --cflags --libs) -o demo2
g++ serverRoot.cxx $(root-config --glibs --cflags --libs) -o serverRoot
g++ clientRoot.cxx $(root-config --glibs --cflags --libs) -o clientRoot
g++ hclient.cxx $(root-config --glibs --cflags --libs) -o hclient
g++ hserv2.cxx $(root-config --glibs --cflags --libs) -o hserv2
g++ hserv.cxx $(root-config --glibs --cflags --libs) -o hserv
```


## What happens if the elements in the numpy array have be cropped? 
- I want the first 10 bits of the word - but shifting all elements by the same amout will cause some values to be wiped out

notes on numpy manipulations
	90      # https://www.quora.com/How-do-you-convert-a-series-of-integers-in-an-array-to-hex-value-Python-arrays-numpy-development
	  1     # hexes = np.vectorize(hex)(inputVec) 
	  2     # hexes = np.fromiter(map(hex, inputVec), dtype='<U10') 
	  3     # hexes = np.fromiter(map(hex, inputVec), dtype='<U5') 
	  4     # print('Datatype:', hexes.dtype)
	  5     # print(hexes)
	  6     # inputVec = inputVec.view()
	  7     # print(inputVec[0])
	  8     # a = np.array([[1,10], [16,255]])
	  9     # print('Datatype:', a.dtype)
	 10     # a = a.tobytes()[::8]
	 11     # a = a.view('S8')
	 12     # print(a)
	 13     # print(a[0,0])
	 14     # inputVec = inputVec.tobytes()
	 15     # print(inputVec[0])
	


## interposer-passthrough:
`./uhal_passthrough.py -s`

`./uhal_passthrough.py --block in --links aquire_length --val 52`
`./uhal_passthrough.py -b in --node global.aquire --val 1`
`./uhal_passthrough.py --fifo in`

`./uhal_passthrough.py --block out --links aquire_length --val 52`
`./uhal_passthrough.py -b out --node global.aquire --val 1`
`./uhal_passthrough.py --fifo out`

`./uhal_passthrough.py --b ch0select --node select --val 0`
`./uhal_passthrough.py --b ch1select --node select --val 1`

`./uhal_passthrough.py --block in --links capture_mode_in --val 2`
`./uhal_passthrough.py --block out --links capture_mode_in --val 2`
	
`./uhal_passthrough.py --block in --links explicit_rstb_acquire --val 0`
`./uhal_passthrough.py --block out --links explicit_rstb_acquire --val 0`

`./uhal_passthrough.py --block in --node global.continous_acquire --val 63`
`./uhal_passthrough.py --block out --node global.continous_acquire --val 3`

`./uhal_passthrough.py --fifo in`
`./uhal_passthrough.py --fifo out`


## MUX links:
Enable Econ Links
```bash
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI0_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI1_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI2_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI3_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI4_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI5_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI6_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI7_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI8_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI9_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI10_DISABLE --val 0
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI11_DISABLE --val 0
```

attach (multiplexer) Econ Links
```bash
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI0_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI1_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI2_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI3_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI4_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI5_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI6_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI7_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI8_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI9_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI10_MUX --val 2
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node MI11_MUX --val 2
```


Update link settings
```bash
./uhal_frontend_ECOND.py --b ECOND-input-munging-axis-switch-0 --node update_settings --val 1
```


```bash
./uhal_backend_ECOND.py --b DAQ-capture-DAQ-link-capture --node link2.override_align_position --val 1
./uhal_backend_ECOND.py --b DAQ-capture-DAQ-link-capture --node link2.align_position --val 28
```


alignment:
```bash
./uhal_backend_ECOND.py --b DAQ-capture-DAQ-link-capture --node link2.align_position --val 7
link2.align_position: 7
./uhal_backend_ECOND.py --b DAQ-capture-DAQ-link-capture --node link2.L1A_offset_or_BX --val 29
```

ECOND get out of reset:
```bash
./uhal_frontend_ECOND.py --b ECOND-ECOND-support-0 --node SOFT_RESET_B --val 1
./uhal_frontend_ECOND.py --b ECOND-ECOND-support-0 --node RESET_B --val 1
```


## List I2C bus
`i2cdetect -l`


## RPM installs
```bash
sudo yum list available zcu102-siengine-v1p0-ROCv3-ECOND-feature_ROCv3_ENGv2_ECOND.v1_6_0 --showduplicates
sudo yum --showduplicates list zcu102-siengine-v1p0-ROCv3-ECOND
sudo yum --showduplicates list installed zcu102-siengine-v1p0-ROCv3-ECOND
```

```bash
sudo yum downgrade zcu102-siengine-v1p0-ROCv3-ECOND-feature_ROCv3_ENGv2_ECOND.v1_6_0-2022.10.28.17.25.12.d29fadf9
```

## output for Danny
```bash
alignment pattern 1 byte: ['0x9c']
PUSM_state: ['0x1']
run bit: ['0x0']
write 0x80 to run bit
run bit: ['0x80']
PUSM_state: ['0x8']

###
eRX defaults: ['0x0', '0x0']
eRX new settings: ['0xf0', '0xff']

###
eTx defaults: ['0x0']
eTx new settings: ['0x3f']

```

```bash
./uhal_frontend_ECOND.py -b in --node global.aquire --val 1
./uhal_frontend_ECOND.py --fifo in
```

```bash
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node bx_link_reset_econd
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node request.link_reset_econd --val 1
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node counters.link_reset_econd
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-recv-axi-0 --node counters.link_reset_econd


./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node request.link_reset_rocd --val 1
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node counters.link_reset_rocd
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-recv-axi-0 --node counters.link_reset_rocd

./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node bx_link_reset_rocd
```

```bash
# check how many econd resets have been sent
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node counters.link_reset_econd
counters.link_reset_econd: 0
# check how many econd resets have been received
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-recv-axi-0 --node counters.link_reset_econd
counters.link_reset_econd: 0
# read or set which bx the reset will be sent on 
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node bx_link_reset_econd
bx_link_reset_econd: 3540
# request a reset on econd
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node request.link_reset_econd --val 1
request.link_reset_econd: 0
# check how many econd resets have been sent
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node counters.link_reset_econd
counters.link_reset_econd: 1
# check how many econd resets have been received
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-recv-axi-0 --node counters.link_reset_econd
counters.link_reset_econd: 1
```

```bash
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-recv-axi-0 --node counters.orbit_sync
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-recv-axi-0 --node counters.orbit_count_reset
```


## Proceedure to align the orbits (BCR, buncrossing reset) between EconD and ROC
- Set the default value of the EconD orbit with i2C
-  `./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node request`
-  `./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-recv-axi-0 --node counters.orbit_sync`

```bash
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node counters.orbit_sync
counters.orbit_sync: 226386
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node counters.orbit_sync
counters.orbit_sync: 255993
./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node command.enable_orbit_sync --val 0
command.enable_orbit_sync: 0

./uhal_frontend_ECOND.py --b housekeeping-FastCommands-fastcontrol-axi-0 --node request.orbit_count_reset
```


## Econ D output links capture mode:
`./uhal_frontend_ECOND.py -b in --links aquire_length --val 300`
`./uhal_frontend_ECOND.py -b in --links capture_mode_in --val 2`
`./uhal_frontend_ECOND.py -b in --node global.continous_acquire --val 63`