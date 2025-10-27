# debug session with Milos and Arnaud



- snapshot window on the ROCv3b has to be changed by 3 bx
roc config: "snaphot" in parameter name
3077-> 3080
- sqlite


yaml/profile

need to destroy the mux file
>>> rm <mux> command
start XDAq
run_<>.sh -<flag> command


run from:
`/home/cmx/asteen/frontend-controller`
first command is required only if second doesn't work
`rm /dev/shm/sem.serenity-z1p2-hnzu\:emptransactor0`
`./run.sh -d`

then from HOMe (in second terminal)
`/home/cmx`
initial setup of frontend "initializes"
`source setUP_FE_esr2_mv.sh`

load l1as:
`hgcal_fc.py tcds2_emu configure -if /opt/hgc_utils/etc/fc_seq/seq_l1a.yaml --write`

then capture words
`emp_capture_bx_range 200; less -S data/rx_summary.txt`
search for `aa` header marker

on DAQ PC -> decode ECOND headers



start configuring system with FE_cfg file.

econ idle patterno abcde500
the link reset changes pattern (for about 200 words)

seq_disable

seql1a sequence
load then enable
emu status
pick



HT -> header trailer
EBO -> 3





econ
global..snapshot_arm --val 1


send ocr and ecr

always 50

BCR bucket default: 1
opposite control val: 1
load val
internal counters - 2 BX counters in the econ

roc daq control starts from 1

orb sync load count - decrease by 1
to bring these values in line


fast command lpgbt ocr
emulator ocr - > used as source of fast command




sqlite Serenity.db
--> check for file name that descirbed front end setup

fastapi stuff isn't actually used - but needed to keep the run control transition commands from crashing
Initialize


regaccess is a uhal parameter access





attatch herd_dth


to initialize
fastapi
herd (lc configs)
script to send commands to herd docker
Serenity
DTH screen

start xdaq
start


opt/swamp/bin/lpgbt_control

check polarity of links:
link_check.py 50

/opt/hgc_utils/etc/

hgcal_xdq_base

have to start something when daq pc is rebooted.


on Serenity
in
/opt/hgc_utils/etc/
addrtab






----------
Milos - 2025 Feb 3

bit error rate
serenity relay to acquire data
had to source a bit file

addrtab file needs to be linked
empbutler
reg_access

dth_env
on dth14


./DTH_control_test.py
opens menu:
3 then 1

24 Gbps -- 800 kHz

750 kHz with 64 bit works

Giacomo Fedi - wrote the mattermost reservation script for serenity.


---------------
streamlit - web control
textual text interface - python package

save run info
configuration generator - for slow control application

software create instance of protocol objects
json file that describes hardware script generates yaml file
gitlab repo
sqlite3 for database

Kubernetes cluster
only for multicassette test

serenity uses arm:
vcu computer will use x86

git
config_generator repo

relay_configs

serializer after config

mqtt instance for monitoring

loader.py
o

serenityU_DB
EHF engine high density full
EHH engine high density half


com express


restful application



## Debug with Arnaud, Paul, Raghu, Milos
------------------
tar ball copied in to docker image
addr tab links are not copied to docker

1211 tgz - there are 2 versions in the directory
fw changes - didn't get packaged in to addrtab
unpacker updates wil have the updated registers - future versions of fw won't need this

change in the unpacker register. Register to say number of unpackers
daq side error.
number of links

reg_access works on pc
herd access to registers doesn't work
does regaccess work in her?

herd-start.sh
 includes a docker-run.sh

docker ps
doecker running
nothing running
opt/hgc_utils - might be to much to add to docker
connections file needs to be added to docker
directory doesn't exist in the docker

temporoary connections file to make in docker

source herd-start.sh
IOaccess not permitted messages expected after

inside docker:
opt/hgc_utils/software/bin/reg_access.py -c /tmp/connections.xml -d x1 -t
export LD_LIBRARypath:

payloaddaq after -t

`payload.daq.stat.num_lpgbt_pair`
was last edited 11 Nov 2024

inside the docker reg_access reads the correct value
access of the docker is correct

not clear why herd is breaking
reg_access.py - there is uhal logging level - downgrade from ERROR to INFO

must use emp interface
transition coldstart that is when the tgz is picked up


when running herd -
hgc-subsystem-plugin/herd.yml
herd -h
has a log-level

code access it hasn't been modified in months

~/bin/StartRelay

configuretemp.yaml

hackmd.io - beam test notes - GET from Arnaud

sedIT command is, at the moment, looking for high rate

Arnaud looking for 10kHz of L1As

one does sedit and one doesn't

FE is the 2 first layers in the beamtest

elink mapping could cause problems in the daq


look for processes

`ps -fa`
`ps -fa | grep cmx`
(on serenity)

6 bit words - 8 words

48 bytes per event - looks like a timeout


capture block configuration:
SerenityDAQconfiguration
did the front end stop responding?
are there matching headers?
ids here
same lpgbt pair
thought that the ids in the bottom capture block would be toward the end and not in the elinkgs
different here
hgcrocv3b
we are talking to the econds
340 header pattern
0x154
is tthe status of the fast command decoder block
is it getting the fast commands
154
matches a value in  the hardware descritpion file serenityU_DB/C_OO_OO_ELE_OO16/

event counter has increased in config saved at end of run
latched error
there eis a 3rd capture in configs

slink start
software

Next check cross check that the l1a is reaching the econd
polarity of fast commands

econt_configs/fcmd_count.yaml

slow_control_configuration/  directory
econ_configs/
fcmd_capture.yaml


opt/swamp/bin/econ_control
error is also going up

command_rx_inverted
locked
fc_error_fcmd_count
tmr_err_cnt_fast_ctrl_decoder:

econ reset form lpgbt_gpio_control
-F layer1.yaml
no fast command error anymore
soft reset at the end of the command

add a chipsync  to get the commands linked together
just reset the econs
l1a_fcmd_count
nzs_fcmd_count
ocr_fcmd_count


issue setting up slink quads
pcie itself an issue?
is there something with the fpga?

uhal packet corruption
packet gets dropped
address is in the firmware

uhal software itself was upgraded on the board itself
but this is in the docker

docker image prune

root user on serenity
pruned all images
docker container prune
docker image prune
docker system prune

exited docker then
docker rm herd


rx_summary.txt
receiving link resets from the econs

reloading rtx firmware

smash problems


rebooting serenity didn't work

configuration of clocks is done independently ? maybe not
normal window?
after rebooting - the sym links need to be resetup

artix reset

plugin locally
herd hgc-subsystem-plugin/herd.yml

trying to run things now without herd container
build software on local computer

cat hgc-setup-plugin

error at poweron (x2)

echo $LD_LIBRARY_PATH
hgc-subsytem-plugin/build:opt/cactus/lib:/home/cmx/ahoward/smash2/smash/core/lib:/opt/smash/lib

powerOn is the 25G firefly getting stuck

configureClockSynthss
config files were mounted in a different location in docker

DAQ PC is having a heart attack

event size is wrong now

leon tried something with PCIe - wanted to pass pcie endpoints to the docker
configuration had to be different

right now running without docker


event size
link 0: 78kHz 4 kB
link 1: 78kHz 0.048 kB (time out)

bin/ relay

spy at summary
configurations are correct
capture blocks
emp capture on the inputs - are you likely to catch a packet?
- raghu is trying


idle words: ccccff08

2 lpgbt links (for 2 layers)
00000000aa3af0a9 .... 00000000d984d86f
00000000aa3af0a9
00000000aa3af0a9
00
ffff
ffff
...
00000000d984d86f
header is the same between the 2
rx summary

aa3af0a9d984d86f

not getting picked up by the capture block
capture block counters are matching with l1as
kkkkk

check the DTH received packets
seeing packets on the disk
status 4 is timeout

relay and run number
daq pc and ls on the directory it is the last one
bin/RunDump1.exe

is there a crc error
no idle errors
event counter is increasing
could we have the

ALP spreadsheet - to enter headerword to check status

DAQPC
inter

../HgcalBeamtest2023/bin/EcondCrc.exe <econheader>

SerenityDaqStatus.yaml
SLlinkConfigurationStart.yaml
FramerConfiguration
link 50 and 51

should move to next firmware
tx summary - fw had a bug
1538
strobe invalid in fc out
capture block output 22-23
relay is not running

Alp is seeing idle errors

image.tgz -> smaillios)1347.tgz
using one link tab

fw from November that Alp used



Firefly issue


bin/RunControlHerd.exe
then gives options
option 2 allows to control the rate

latency definition- what is the cable length
80m minus 1 or 2m extension
discussion of changing the timeout value 426
for first econd packet
bunch crossing mismatches if some econd packets comethrough
iimplicit delay included in the timeout

consistent with data coming to the wrong link - but then configuration would not work
on the right lpgbt link 012 are 50 and 51

instability with uhal is fixed - not working in docker
transaction id issue has stopped
data is not coming in at the right rate on one link


in the right links, taking l1as

probe capture block input- alp will make new fw.



# DPG data taking

open ssh to serenity
open ssh to daq PC
open ssh to DTH


HGC-tb.,
cms.higgs
userdth


in herd docker on dth:  dth_plugin_files/pd.sh

on pc export LDLIBRARY PATH


link reset patterns from econs:
051aa51aa




##################################################
### 3 windows on Serenity (ssh cmx@serenity-z1p2-hnzu.dyndns.cern.ch)
- 1st tab:
--> Here we run the HERD application (to control board services, and manages run control)
 1000  cd pdauncey/
 1001  ls
 1002   export LD_LIBRARY_PATH=hgc-subsystem-plugin/build:$LD_LIBRARY_PATH
 1003  herd hgc-subsystem-plugin/herd.yml

- 2nd tab
--> Here we looked at econ data after initializing the system
--> Then we provided run control commands to the HERD application to take random trigger data (4GB files) and pedastal data
(started from 996)
  993  source env.sh
  994  source ./env.sh
  995  make -j
  996  ./run.sh
  997  cd bin
  998  l
  999  cat CandS
--> Aidan started here:
 1000  cd pdauncey/hgc-subsystem-plugin/
 1001  ls
 1002  ColdStart
 1003  Initialize
 1004  cd
 1005  pwd
 1006  source setUP_FE_beamtest_jan2025.sh
 1007  less -S data/rx_summary.txt
 1008  cd -
 1009  bin/RunControlHerd.exe

 in options for bin/RunControlHerd.exe ran

 Relay keys and types:
  0: Pedestals
  1: BeamRun
  2: RandomTriggerTest
  3: CalPulseRun
  4: CalPulseTrain
  5: CalPulseSelfTrigger
  6: HighRateTest
  7: Quit

first run did  2: RandomTriggerTest (with 10 kHz)
second run 0: Pedestals

- 3rd tab
Configured the front end with a shell script

  984  ls /opt/swamp/bin/
  985  ls
  986  rm -rf /opt/swamp
  987  sudo rm -rf /opt/swamp
  988  unzip artifacts\(25\).zip
  989  sudo rpm -i rpm_path/almalinux/9/x86_64/rpms/swamp-cpp.x86_64.rpm
  990  cd
  991  cd asteen/frontend-controller/
  992  ls
  993  source env.sh
  994  source ./env.sh
  995  make -j
--> Aidan started here:
  997  cd bin
  998  l
  999  cat CandS
 1000  cd asteen/frontend-controller/
 1001  ls
 1002  ./run.sh

(run slow control of frontend)

### 3 windows on DAQ PC (ssh daq@hgcdaqrx1)

- 1st tab:
--> Started HERD application with a config file
 981  ip neigh show
  982  dth_recv
  983  who
  984  ip neigh show
  985  arp -n
  986  ip addr show
  987  ip link show
  988  sudo iptables -L -n
  989  cat /proc/sys/net/ipv4/conf/all/arp_ignore
  990  cat /proc/sys/net/ipv4/conf/all/arp_filter
  991  sudo arp -s 192.168.1.202 50:6b:4b:0f:f6:1d
  992  ip route show
  993  exit
  994  emacs -nw ~/.ssh/known_hosts
  995  exit
--> Aidan started here:
  996  cd pdauncey/
  997  export LD_LIBRARY_PATH=build:$LD_LIBRARY_PATH
  998  herd exampleboard/newherdempty.yml
  999  jobs

- second tab:
--> Here we looked at data rates being saved to the DAQ PC (from 2 SLinks)
  979  sudo tcpdump -n -i enp44s0f1np1 arp -vvv
  980  arp --help
  981  ip neigh show
  982  dth_recv
  983  who
  984  ip neigh show
  985  arp -n
  986  ip addr show
  987  ip link show
  988  sudo iptables -L -n
  989  cat /proc/sys/net/ipv4/conf/all/arp_ignore
  990  cat /proc/sys/net/ipv4/conf/all/arp_filter
  991  sudo arp -s 192.168.1.202 50:6b:4b:0f:f6:1d
  992  ip route show
  993  exit
  994  emacs -nw ~/.ssh/known_hosts
  995  exit
--> Aidan started here:
  996  cd HgcalBeamtest2024/
  997  bin/FifoPrint.exe

- 3rd tab:
--> Unpacked some econ data and log data to check if front end was configured correctly
--> Then we looked at where the data was stored (specifically looked at the yaml log file of the relay and Run, data is in the relay directory - one for each of the 2 Slinks)
 996  cd HgcalBeamanal2024/
  997  pwd
  998  ls
  999  pwd
 1000  ls dat/Relay1739443058/Run1739443061_SerenityFramerConfigurationStop.yaml
 1001  ls -P dat/Relay1739443058/Run1739443061_SerenityFramerConfigurationStop.yaml
 1002  ls dat/Relay1739443058/Run1739443061_SerenityFramerConfigurationStop.yaml
 1003  ./bin/RunDump1.exe 1739443058 1739443061 > total.log &
 1004  less total.log
 1005  jobs
 1006  less total.log
 1007  jobs
 1008  fg
 1009  ls
 1010  ls dat
 1011  ls -ltrh dat/Relay1739443764/Run1739443767_SerenityFramerConfigurationStop.yaml
 1012  ls -ltrh dat/Relay1739443764/

RunDump1 looks at link 1


### 1 window on DTH (ssh DTH@dth-p1-v2-14.dyndns.cern.ch)

Run HERD on DTH (from inside Docker)

 1003  docker start herd_dth
 1004  docker attach herd_dth
 1005  jobs
 1006  docker ps


in docker we ran:
dth_plugin_files/pd.sh



