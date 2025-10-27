setup zcu v3 train:

in the swamp directory:
git clone https://gitlab.cern.ch/lpgbt/lpgbt_control_lib.git
pip install --user -e lpgbt_control_lib/
pip install tqdm
pip install nested_dict
pip install pyyaml



setup vtrx is necessary!!
DLL hack may be necessary!

set the clocks:
power cycle engine
sudo fw-loader load active
(refclk already seems to be set at 320MHz- remembered this wasn't in the past - right after zcu boot?)
./zcu_multitool.py --status
./zcu_multitool.py --setrefclk
(REF gets updated, but right after boot up TX and TX40 are not updated so need to run
./zcu_multitool.py --resetlink
but not RX0 gets stuck at 321 until fw is reloaded and next command is run
)
./zcu_multitool.py --status
./setup_lpgbt.py --linktrick --protocol AUTO --daqonly
./zcu_multitool.py --status

then saw 40 MHz on RX0
(40 MHz didn't work if DLL HACK was true and E/W polarity was set to 1 in setup_lpgbt.py)

setup LPGBT
./setup_lpgbt.py --linktrick --protocol AUTO --daqonly

./setup_lpgbt.py --vtrx
(after this, daq RX0-DV reads 40, trigger RX*-DV read 0)
./setup_lpgbt.py --protocol AUTO --trigsetup
./setup_lpgbt.py --protocol ICEC --trigsetup
./setup_lpgbt.py --protocol ICI2C --trigsetup
./setup_lpgbt.py --protocol AUTO --gpiosetup

./setup_lpgbt.py --linktrick --protocol AUTO
./setup_lpgbt.py
then do DLL HACK
./setup_lpgbt.py
./setup_lpgbt.py --linktrick --protocol AUTO

./zcu_multitool.py --polarity 1 --olink 1
./zcu_multitool.py --polarity 0 --olink 2

lpgbt status:
./lpgbt_status.py --mode V3 --list
old style of register dumps
./lpgbt_status.py --mode V3 -t W --old
dump all registers
./lpgbt_status.py --mode V3 -t W --dump

gpio:
./gpio_control.py --mode V3 --list
./gpio_control.py --mode V3 --read WEST.PWR_EN0

WEST.PWR_EN0
WEST.PWR_EN1
WEST.PWR_EN2
WEST.HGCROC_RE_Hb0
WEST.HGCROC_RE_Hb1
WEST.HGCROC_RE_Hb2
WEST.HGCROC_RE_Sb0
WEST.HGCROC_RE_Sb1
WEST.HGCROC_RE_Sb2
WEST.ECON_RE_Hb0
WEST.ECON_RE_Hb1
WEST.ECON_RE_Hb2
WEST.ECON_RE_Sb0
WEST.ECON_RE_Sb1
WEST.ECON_RE_Sb2
WEST.PG_LDO0
WEST.PG_LDO1
WEST.PG_LDO2
WEST.PG_DCDC0
WEST.PG_DCDC1
WEST.PG_DCDC2

EAST.PWR_EN0
EAST.PWR_EN1
EAST.PWR_EN2
EAST.HGCROC_RE_Hb0
EAST.HGCROC_RE_Hb1
EAST.HGCROC_RE_Hb2
EAST.HGCROC_RE_Sb0
EAST.HGCROC_RE_Sb1
EAST.HGCROC_RE_Sb2
EAST.ECON_RE_Hb0
EAST.ECON_RE_Hb1
EAST.ECON_RE_Hb2
EAST.ECON_RE_Sb0
EAST.ECON_RE_Sb1
EAST.ECON_RE_Sb2
EAST.PG_LDO0
EAST.PG_LDO1
EAST.PG_LDO2
EAST.PG_DCDC0
EAST.PG_DCDC1
EAST.PG_DCDC2
X.RESETb
X.PWR_EN



sudo fw-loader load active
# need to apply polarity first it seems
./zcu_multitool.py --polarity 1 --olink 1
./zcu_multitool.py --polarity 0 --olink 2
# polarity should read 3 (after zcu_multitool status)
# if zcu already has right readings TX, else need to run zcu link trick
./zcu_multitool.py --status
./zcu_multitool.py --setrefclk
./zcu_multitool.py --status
./setup_lpgbt.py --linktrick --protocol AUTO --daqonly
./zcu_multitool.py --status
# this time vtrx value read back 0 - earlier was set to one - maybe already setup because no troubles later
./setup_lpgbt.py --vtrx
./zcu_multitool.py --status
###
# TRYING:
./setup_lpgbt.py
./setup_lpgbt.py --mode V3_ALL
###
# instead of
./setup_lpgbt.py
vim setup_lpgbt.py 
./setup_lpgbt.py
vim setup_lpgbt.py 
###  
./lpgbt_status.py --mode V3 -t E --old
./zcu_multitool.py --status
./setup_lpgbt.py --linktrick --protocol AUTO

# fnal branch, to set the drive strength and frequency properly:
git checkout engineSetup_FNAL
# applying this v3_ALL before do setup might help?
./setup_lpgbt.py --device zcu --mode V3_ALL
./doSetup.sh
./doLinkTrick.sh
./initAndAlign.sh

(runs V3_all)

swamp attempt to read a roc I2C:
python roc_control.py -s e0 -a 0x08 -rw read -pname "DigitalHalf".all."IdleFrame"


read I2C with hgc engine tools:
./roc_test.py --protocol EC2 --bus 0 --roc 1 --regs 43,24
./roc_test.py --protocol EC2 --bus 0 --roc 1 --regs 43,25
./roc_test.py --protocol EC2 --bus 0 --roc 1 --regs 43,24
./roc_test.py --protocol EC2 --bus 0 --roc 1 --regs 43,16
./roc_test.py --protocol EC2 --bus 0 --roc 1 --regs 43,17
./roc_test.py --protocol EC2 --bus 0 --roc 1 --regs 43,18
./roc_test.py --protocol EC2 --bus 0 --roc 1 --regs 43,19
./roc_test.py --protocol EC2 --bus 0 --roc 3 --regs 43,19
./roc_test.py --protocol EC2 --bus 0 --roc 5 --regs 43,19
./roc_test.py --protocol EC2 --bus 0 --roc 5 --regs 89,19
./roc_test.py --protocol EC2 --bus 0 --roc 3 --regs 89,19
./roc_test.py --protocol EC2 --bus 0 --roc 1 --regs 89,19
./roc_test.py --protocol EC2 --bus 0 --roc 1 --regs 89,15



######################################################
######################################################
the time it worked:
git checkout V3
./zcu_multitool.py --status
./zcu_multitool.py --setrefclk
./setup_lpgbt.py --linktrick --protocol AUTO --daqonly
./zcu_multitool.py --status
./setup_lpgbt.py --vtrx
./zcu_multitool.py --status
./setup_lpgbt.py
vim setup_lpgbt.py 
./setup_lpgbt.py 
fg
./lpgbt_status.py --mode V3 -t E --old
./setup_lpgbt.py --linktrick --protocol AUTO
./zcu_multitool.py --status
pwd
ls
pwd
git  status
git branch
git checkout engineSetup_FNAL
git status
ls
vim doSetup.sh 
# applying this v3_ALL before do setup might help?
./setup_lpgbt.py --device zcu --mode V3_ALL
./doSetup.sh
cat ./doLinkTrick
ls
cat ./doLinkTrick
cat ./doLinkTrick.sh 
./doLinkTrick.sh 
vim ./initAndAlign.sh
./initAndAlign.sh
then saw 1s on a couple lines on trig links in aidan_capture (immediate capture)
then did an lpgbt config for DAQ lpgbt in lpgbt_aidan and ROC run subblock set to 0xAB
then saw idles on last four trig links

#####################
./zcu_multitool.py --polarity 1 --olink 0




# Questions:
- what is the right way to reset the system? ZCU and lpgbts?
    - Reset all regesters to those at power up?
    - only real way to have repeatable results seems to power everything off 
        - zcu status output changes
    - vtrx state
    - https://lpgbt-support.web.cern.ch/t/procedure-to-reset-lpgbts-on-optoboard/902

- To configure: POWERUP2 = 0 , set registers, POWERUP2 = 6
    - always needed when setting registers on a given lpgbt?

- dll hack... standard procedure? Or has been replaced with other configurations?
Because: trig link notice: 0x1d9 to read 0e sometimes
PUSMStatus =  PAUSE_FOR_DLL_CONFIG_DONE
fix it by
cycling the POWERUP1 and POWERUP2 registers
0xf9: 0x0F --> 0x00
0xfa: 0xFF --> 0x00

- I2C stability
- phase
EPRX6CurrentPhase10
0x165

# Notes Sep 29

phase values are different only - between last night (idles on trig) and this morning (all zeros)
vim -d trig_2023Sep29_1045_allZerosAfterreboot_rocAB.txt trig_2023Sep27_2023Sep28_1945_afterReboot_idlesOnTrig.txt

concetrator mezzanine adapter I2C 
break out board
long board one connector of mezzannine

automattic phase setting
fixed mode
on the optical link
eye opening measurement





# Notes Oct 4:

1) clocks can get stuck - and then communication to daq lpgbt is lost
only recourse is to power cycle
RX0: 321.27540000 MHz
RX1: 321.27900000 MHz
RX2: 321.28250000 MHz

2) no multiple versions of the same fw name:
have to use:
sudo yum remove zcu102-ldv3-r1p0-ROCv3

3)
needs to be added afer line 10 of enginev3 backend uhal module xml file:
https://gitlab.cern.ch/cms-hgcal-firmware/engine_sa_backend/-/blob/4758fa665bd2c10d9df8824980f1fd31a632d91d/sw/xml/enginev3_backend.xml#L10
<node id="INVERT_RX_DATA_ORDER" mask="0x4000"/>
added now with a sed command

4) need to use DAQ mode for link capture



