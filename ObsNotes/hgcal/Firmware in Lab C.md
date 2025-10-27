# 
export PATH=$PATH:/tools/Xilinx/Vivado/2021.2/bin
export XILINXD_LICENSE_FILE=2100@xilinx-lic
export XILINXD_LICENSE_FILE=/home/agrummer/cass-fw/Xilinx.lic

The `./project` command is custom python wrapper for vivado batch commands and SDK, software design kit,  batch commands
	- This wrapper is loaded from `./prj_utils/` directory, `./project` just calls `./prj_utils/project.py`
	- the `click` python library is just a command line argument parser (wrapper for argparse)
looks like the SDK (software design kit), is needed for producing the device tree
these two SDK commands are used in `./project`:
1) `xsct` (xilinx software command line tools) command is used to... initialize the device tree overlay?
	https://docs.xilinx.com/r/en-US/ug1400-vitis-embedded/Xilinx-Software-Command-Line-Tool?tocId=CwnQ90bFNEhE~pGBspGuOQ
2) the command `dtc`  (device tree compiler) is used to generate the device tree
	https://xilinx-wiki.atlassian.net/wiki/spaces/A/pages/18842279/Build+Device+Tree+Blob

vivado

this repo doesn't work - no rights to econd-lightweight
git clone -b trunk_v2 ssh://git@gitlab.cern.ch:7999/cms-hgcal-firmware/engine_zcu.git

dont have to do this removal step any more (Jon gave Reporter access)
	vim .gitmodules 
	remove the econd-lightweight module
git submodule update --init --recursive



git clone -b trunk_v2_sans_ECONd --recursive ssh://git@gitlab.cern.ch:7999/cms-hgcal-firmware/engine_zcu.git

./project list

git clone -b trunk_v2 ssh://git@gitlab.cern.ch:7999/cms-hgcal-firmware/engine_zcu.git
git submodule update --init --recursive
using project name = zcu102-siengine-v1p0-ROCv3
./project clean {project Name}
./project create {project Name}
./project build {project Name}


```
git clone -b trunk_v2 [ssh://git@gitlab.cern.ch:7999/cms-hgcal-firmware/engine_zcu.git](ssh://git@gitlab.cern.ch:7999/cms-hgcal-firmware/engine_zcu.git)
cd engine_zcu
git submodule update --init --recursive
./project list
# using project name (the one I use normally) = zcu102-siengine-v1p0-ROCv3
./project clean {project Name}
./project create {project Name}
./project build {project Name}
```




check out zipcpu blog

sfp = something form factor plugable


lvds -low voltage differential signaling


## Example firmware for FMC card
constraints file:
https://ohwr.org/project/wr-cores/blob/proposed_master/top/clbv3_ref_design/clbv3_wr_ref_top.xdc
https://ohwr.org/project/wr-cores/blob/proposed_master/top/clbv3_ref_design/clbv3_wr_ref_top.xdc#L234

## TTL and NIM logic definitions:
http://www.physics.mcgill.ca/~corriveau/projects/spark/nim2.html#:~:text=A%20TTL%20signal%20has%20the,is%20made%20of%20bipolar%20transistors.
- NIM
	 A NIM signal has the following definition of a digital "1" and a digital "0":  
	 When a signal voltage is between -0.8 V and -1 V, it's a digital "1".  
	 When a signal voltage is exactly 0 V, it's a digital "0".  
	 NIM is an acronym for Nuclear Instrument Modules since it has been developped for this kind of experiment.
- TTL
	A TTL signal has the following definition of a digital "1" and a digital "0":  
	When a signal voltage is between 1.5 V and 5 V, it's a digital "1".  
	When a signal voltage is between 0 V and 0.7 V, it's a digital "0".  
	TTL is an acronym for Transistor-Transistor Logic since it is made of bipolar transistors.

## Tracker FW:
https://gitlab.cern.ch/cms_tk_ph2/d19c-firmware/-/tree/master/fw/src/usr/dio5

