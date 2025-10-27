
4 steps of petalinux automation build
There is the Creation of the PetaLinux project, the Configuration, the Construction, and the Packaging.



## Vivado LAB install
This file says prerequisite libraries - instructions should have said to install this first probably. Didn't hvae probablems though. See below.
installLibs.sh


Note: Cable Crivers are not installed on Linux. Please sollow the instructions in UG973 to install the LInux cable drivers
Installed with Vivado:
Vivado Lab, UpdateMEM, Installation Options

to install, downloaded vivado Lab (2022.2) tarball from vivado page
- there was an option to choose vivado Lab UPDATE 2, but it did not say linux on it.
- decided this was best since it is still avaiable on the website

Requires 7.16 GB of disk space

installed under:
/tools/Xilinx
/tools/Xilinx/Vivado_Lab/2022.2

### cable install
installed cable drivers post-vivado labs install

https://docs.amd.com/r/en-US/ug973-vivado-release-notes-install-license/Installing-Cable-Drivers

cd /tools/Xilinx/Vivado_Lab/2022.2/data/xicom/cable_drivers/lin64/install_script/install_drivers/
./install_drivers

CRITICAL WARNING: Cable(s) on the system must be unplugged then plugged back in order for the driver scripts to update the cables.

### more libraries
dnf install lsb_release
from installer untarred folder:
source installLibs.sh - actually for th 2022.2 install, almalinux os isn't an option. So I ran the dnf install for each of the packages from centos8. Most were already installed redhat-lsb could not be installed. 2 others were installed.
after sourcing environment vivado_lab still doesnt run
complains about libtinfo5
--> resolved this complaint with ncurses-compat-libs


must source this file for vivado to start:
source /tools/Xilinx/Vivado_Lab/2022.2/settings64.sh



## Software installations on VCU PC

### IPBUS:
installed with yum:
https://ipbus.web.cern.ch/doc/user/html/software/install/yum.html
sudo curl https://ipbus.web.cern.ch/doc/user/html/_downloads/ipbus-sw.el9.repo -o /etc/yum.repos.d/ipbus-sw.repo
sudo yum groupinstall uhal

have to include this in bashrc:
export LD_LIBRARY_PATH=/opt/cactus/lib:$LD_LIBRARY_PATH

--> EMP used python3.11 so had to install these separately:
sudo yum install cactuscore-uhal-python311
sudo yum install cactuscore-uhal-python311-gui

### EMP + Serenity

webpage instructions:
https://serenity.web.cern.ch/serenity/emp-fwk/software/install.html


https://serenity.web.cern.ch/serenity/emp-fwk/software/install.html
sudo curl https://serenity.web.cern.ch/serenity/emp-fwk/_downloads/emp.repo -o /etc/yum.repos.d/emp.repo
--> but install failed

```
>>> sudo yum install "cactusboards-emp-*"
EMP software repository                                                                                  42 kB/s | 4.4 kB     00:00
Errors during downloading metadata for repository 'emp-sw':
  - Status code: 404 for https://emp-fwk.web.cern.ch/sw/release/0.8/repos/el9/x86_64/repodata/repomd.xml (IP: 2001:1458:d00:62::100:2e8)
Error: Failed to download metadata for repo 'emp-sw': Cannot download repomd.xml: Cannot download repodata/repomd.xml: All mirrors were tried
```
this page doesn't exist:
--> https://emp-fwk.web.cern.ch/sw/release/0.8/repos/el9/x86_64/repodata/repomd.xml
but this one does:
https://emp-fwk.web.cern.ch/sw/release/0.9/repos/el9/x86_64/repodata/repomd.xml

edit this file: `vim /etc/yum.repos.d/emp.repo`
to change to release 0.9

install was successful -> installed some things for python 3.11


### py venv

had to make sure pip method was installed
python -m ensurepip --upgrade

python3.11 -m venv --system-site-packages pyvenv311
source pyvenv311/bin/activate

(needed --system-site-packages to get uhal in)

python packages serenity recommends to install (with python 3.6 for some reason, ignoring that):
sudo python -m pip install --upgrade
click==8.0.4
click_didyoumean==0.3.0
pytest==7.0.1
python-dateutil==2.8.2
pyyaml==5.1.2
colorama==0.4.5

used this command inside pyvenv311:
python -m pip install --upgrade click click_didyoumean pytest python-dateutil pyyaml colorama
python3.11 -m pip install --upgrade click click_didyoumean pytest python-dateutil pyyaml colorama

export PATH=/opt/cactus/bin/emp:$PATH
export LD_LIBRARY_PATH=/opt/cactus/lib:$LD_LIBRARY_PATH
export PYTEST_ADDOPTS="--rootdir=."


sudo vim `which empbutler`
#!/usr/bin/python3.11
#!/usr/bin/env python3


### without py venv (to avoid changing emp butler python path)

uninstall and reinstalled emp:
sudo yum remove "cactus*emp*"
sudo yum clean all
sudo yum install "cactusboards-emp-*"

make sure pip in in python3.11
python3.11 -m ensurepip --upgrade

before package installs:
```bash
[agrummer@hgcalpcvcu1 ~]$ pip3.11 freeze
cactusboards-emp-python311==0.9.4
cactuscore-uhal-python311==2.8.16
cactuscore-uhal-python311-gui==2.8.16
```

python3.11 -m pip install --upgrade click click_didyoumean pytest python-dateutil pyyaml colorama

after emp required package installs

```bash
[agrummer@hgcalpcvcu1 ~]$ pip3.11 freeze
cactusboards-emp-python311==0.9.4
cactuscore-uhal-python311==2.8.16
cactuscore-uhal-python311-gui==2.8.16
click==8.1.8
click-didyoumean==0.3.1
colorama==0.4.6
iniconfig==2.0.0
packaging==24.2
pluggy==1.5.0
pytest==8.3.4
python-dateutil==2.9.0.post0
PyYAML==6.0.2
six==1.17.0
```

## communicating over the PCIe

following along here:
https://github.com/ucsd-hep-ex/VCU118/tree/main

scripts/pcie_reconnect_xilinx.sh doesn't find the pcie device
-> rebooting the linux PC (after fw loaded on the VCU), now device is found:
/sbin/lspci -d 10ee:9031
-> this is the command that doesn't work:
echo 1 > /sys/bus/pci/rescan

so don't run this script: scripts/pcie_reconnect_xilinx.sh - it will only remove the Xilinx device and won't find it again
but if fw is reloaded may need a way to reset the device in the device tree

```bash
[root@hgcalpcvcu1 scripts]# /sbin/lspci -d 10ee:9031
01:00.0 Serial controller: Xilinx Corporation Device 9031
```

had to edit the scripts/connections.xml file to point to the correct devices and top_emp.xml file
there were no xdma devices in /dev
have to add them using this repo: https://github.com/Xilinx/dma_ip_drivers
had to change one line in the code (using kernal 5.14 used code for kernal 6.3)
https://github.com/Xilinx/dma_ip_drivers/issues/288#issuecomment-2657164661
ran
make
and
make install
in the xdma directory

insmod xdma.ko failed
had to remove SecureBoot in Bios
then the xdma devices appeared in /dev (after reboot)

now empbutler commands in scripts/pattern_file_test.sh mostly work
(the reset works, the random pass didn't work)





# installing vivado

following instructions on serenity webpage

had to add to egroups
The EMP firmware framework is available at p2-xware / firmware / emp-fwk · GitLab.
You will have to subscribe to emp-fwk-users e-group to access this repository and to cms-tcds2-users e-group to get TCSD2 firmware dependencies.

ipbb proj create vivado my_projects_name emp-fwk:projects/examples/vcu118 top_lpgbt.dep

missed the gbtsca

emp_payload.vhd
emp_project_decl_lpgbt.vhd

empttc_decl.vhd
emp_device_decl.vhd

clock_constraints



decode top emp .xml
pins.tcl


addrtop -t

emp_idcode.vhd

emp_slink_test +pattern_generator
ipbus_syncreg_v.vhd

downloaded the bin file from the Xilinx AMD webpage
changed permissions to make the file executable
saved the file in /home/zgecse


# update Vivado to 2022.2.2
Couple days later - pop up window appears to update the vivado version (from 2022.2.0 I think)
taking 30-45 min
17 GB

# install serenity-toolbox (and smash)
https://gitlab.cern.ch/p2-xware/software/serenity-toolbox
https://gitlab.cern.ch/p2-xware/software/serenity-toolbox#build-instructions

followed instructions in alma 9

using pyvenv311 venv  again (sourcing it, not remaking it)
not using sudo to install python packages

install latest versions (and ignoring the other pip packages - because latest versions are already installed):
python3.11 -m pip install pylint pyyaml pexpect pyzmq
instead of
python3.11 -m pip install pylint==3.2.6 pyyaml==6.0 pexpect==4.8.0 pyzmq==23.2.1


everything here was already installed:
sudo dnf install make rpm-build gcc-c++ boost-devel-1.75.0 pugixml-devel-1.13 yaml-cpp-devel-0.6.3 python3.11-devel python3.11-pip cactuscore-uhal-* cactuscore-build-utils-0.3.5

installed smash: (cactusboards-emp* were already installed)
sudo dnf install cactusboards-emp* smash-*

smash install wasn't successful afterall
 smash-components
 smash-core
 smash-extern
 smash-logger
 smash-pcieutils
 smash-python311
 smash-serenity
 smash-unit-tests
 smash-unittests

 there were conflicts between the two unit tests
 will just pick the one with the larger unittests
 smash-unit-tests x86_64 1.0.1-0.alma9.gcc11_4_1 smash 175 k
 smash-unittests x86_64 1.0.2-0.alma9.gcc11_4_1 smash 353 k

sudo dnf install smash-components smash-core smash-extern smash-logger smash-pcieutils smash-python311 smash-serenity smash-unittests
have to clone serenity-toolbox with:
git clone --recurse-submodules https://gitlab.cern.ch/p2-xware/software/serenity-toolbox.git

compile serenity toolbox
make

had to also install:
pip install rpm


# Reinstalled vivado 2022.2

after install it says:

"""
Installation completed successfully.
For the complete setting to use Versal ACAP tools, please run the script "installLibs.sh" uncer
/home/zgecse/Xilinx/Vitis/2022.2/scripts, which requires the root privilege.
"""



# adding users:

groupadd -g 5063 us_cms
useradd -g zh -u 79227 -d /home/smallios smallios


