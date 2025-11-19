# linux install for labc2

CERN instructions: https://linux.web.cern.ch/almalinux/alma9/stepbystep/
OTS DAQ instructions from Lorenzo: https://gitlab.cern.ch/otsdaq/otsdaq_cmstracker
FNAL RPMS: https://linux-mirrors.fnal.gov/linux/fermilab/el/9/notes.html
actuall used: https://linux-mirrors.fnal.gov/linux/fermilab/almalinux/9/notes.html

- got MAC address from photo of sticker on ethernet port (now notice that MAC address also appears in alma linux install options under "Network&Host Name"
- added to DHCP server on labc1
- also turned on network stack and enabled ipv4 in the ASUS BIOS. Not sure if this had an impact. network was only reached after booting from the USB image.
- for adding the CERN repo in installation source - selected "Auto-detected instalation media (and not "On the network" like in CERN instructions ) and added the repourl as instructed with 9.5: `linuxsoft.cern.ch/cern/alma/9.5/CERN/x86_64/`
    - only after this configuration did CERN Workstation appear.

used this repo instead (webpage points to el/9 instead of almalinux/9):
sudo yum install https://linux-mirrors.fnal.gov/linux/fermilab/almalinux/9/yum-conf-fermilab.rpm
used(could have added a -y flag, but only needed to say yes a few times):
yum group install fermilab
instead of this:
sudo yum install --setopt=install_weak_deps=False fermilab-base_on-site



groupadd -g 5063 us_cms
useradd -g us_cms -u 58219 -d /home/agrummer agrummer
useradd -g us_cms -u 15485 -d /home/sculac sculac
useradd -g us_cms -u 43188 -d /home/dauncey dauncey
useradd -g us_cms -u 45508 -d /home/pastika pastika


ssh-copy-id -i .ssh/id_ed25519.pub agrummer@labc2

useradd -g us_cms -u 43203 -d /home/zgecse zgecse
passwd zgecse
passwd agrummer
normal hgcal password

uid=13816(calvarez)
useradd -g us_cms -u 13816 -d /home/calvarez calvarez

useradd -g us_cms -u 59735 -d /home/jwang jwang
passwd jwang

useradd -g us_cms -u 1001 -d /home/hgcal_dev hgcal_dev
passwd hgcal_dev

useradd -g us_cms -u 24293 -d /home/gmachado gmachado
passwd gmachado

useradd -g us_cms -u 56472 -d /home/wterrill wterrill
passwd wterrill


can proxyjumb from labc1 to labc2:
add public key from laptop to .ssh/authorized_keys of labc2
add Identity file (to the key that exists on laptop) to .ssh/config setting for labc2 (that has the ProxyCommand through labc1)


## vivado install
install 2022.2 from Xilinx website
selected Vitis install
all types were selected by default - kria, series7, Ultrascale+, Versal..., kept all of them selected
total space required by end of download says: 131 GB.


UG973 needed for driver install on linux
will need: https://docs.amd.com/r/en-US/ug973-vivado-release-notes-install-license/Installing-Cable-Drivers

## remote desktop login
(skipped for labc3)

using "Window's App" on mac to connect to linux machine
installed xrdp on linux (as root user)
https://www.server-world.info/en/note?os=AlmaLinux_9&p=desktop&f=3

-> install from EPEL
[root@dlp ~]# dnf --enablerepo=epel -y install xrdp
[root@dlp ~]# systemctl enable xrdp --now
[root@dlp ~]# firewall-cmd --add-port=3389/tcp
success
[root@dlp ~]# firewall-cmd --runtime-to-permanent
success

sudo systemctl enable xrdp
sudo systemctl restart xrdp

windows app didn't accept user

this page says user cannot be logged in elsewhere


https://serenity.web.cern.ch/serenity/emp-fwk/software/install.html


## Vivado install

failed in last step: "Generating installed device list"
Installed Vivado_labs first - there are some prerequisites installed here first:
installLibs.sh
worked after this. but also also did this(probably needed, found when setting up cern pcvcu1):
yum install ncurses-compat-libs
also it was mentioned in online forums that libtinfo5 was needed to get past this issue.


## uhal and emp install

haven't done EMP toolbox install yet

git clone --recurse-submodules https://:@gitlab.cern.ch:8443/p2-xware/software/emp-toolbox.git -b v0.9.4
cd emp-toolbox
make

authentication failure

acually probably need this:
https://gitlab.cern.ch/p2-xware/software/serenity-toolbox
https://gitlab.cern.ch/p2-xware/software/serenity-toolbox#build-instructions


## secure boot

try to turn secure boot off
https://www.youtube.com/watch?v=tnOHi0w77bU
probably already off


## emp-toolbox install

sudo cp docs/yum-dependencies/*.repo /etc/yum.repos.d/

directory: docs/yum-dependencies/
had two files:
cactus-build-utils.repo  ipbus-sw.repo
-> ipbus repo file is very similar to one used for previous install. just points to $releasever instead of having 9 (for el9) hard codded


sudo yum install boost-devel pugixml-devel python36-devel cactuscore-uhal-* cactuscore-build-utils-0.2.9 tkinter

python36-devel
and
tkinter
didn't install

sudo python3.6 -m pip install --upgrade click==8.0.4 click_didyoumean==0.3.0 pytest==7.0.1 python-dateutil==2.8.2 pyyaml==5.1.2 colorama==0.4.5
python -m pip install --upgrade click click_didyoumean pytest python-dateutil pyyaml colorama

## update bios:


https://www.youtube.com/watch?v=Ndnpw8sflpg
https://www.reddit.com/r/buildapc/comments/17g1t36/does_intel_14th_and_b760_motherboards_work_out_of/
https://www.reddit.com/r/intel/comments/17bk2h7/will_the_new_i514600k_get_to_the_motherboard_bios/

installed BIOS from windows VM on mac
https://www.asus.com/us/motherboards-components/motherboards/prime/prime-b760-plus/helpdesk_bios?model2Name=PRIME-B760-PLUS

save folder to USB drive (using a windows computer)
connect USB to linux computer
in bios update using advanced menu >> tool >> ez flash 3 utility

## pcie checks

secure boot?
https://superuser.com/a/1734334
mokutil --sb-state
dmesg | grep -E 'secure'


dmidecode --type 9
or equivelently
dmidecode --type slot
https://superuser.com/a/693999

and lspci
https://superuser.com/a/930778

for xilinx device:
`/sbin/lspci -d 10ee:`

check for mod
lsmod | grep xdma; echo $?


(not complete yet):
xdma install was with (need to copy rules and sh file to /etc/udev
https://github.com/Xilinx/dma_ip_drivers/tree/master/XDMA/linux-kernel
Raghu seems to have taken /etc/udev/rules.d rules and sh file from here:
https://github.com/RHSResearchLLC/XilinxAR65444/tree/master/Linux/Xilinx_Answer_65444_Linux_Files



## install swamp-cpp


### old notes see labc3 install md:
https://gitlab.cern.ch/asteen/swamp-cpp

hiredis install seemed to work as in here:
https://gitlab.cern.ch/asteen/swamp-cpp#pre-requisite

redis-plus-plus didn't work as expected though

needed to install libidn11 library, installed libidn and libidn12
linked to libidn.so.12 as here:
https://askubuntu.com/a/1483305

then the libid11 missing library was solved. it is in /usr/lib64/

Next issue was missing redisEnableKeepAliveWithInterval
Determining if the redisEnableKeepAliveWithInterval exist failed with the following output:

noticed cmake was using Vitis installed cmake
so installed cmake3.30 from source
https://idroot.us/install-cmake-almalinux-9/

cmake version <3.5 will not be supported in future versions - so this was indeed probably the problem

note in arnaud's page says   "Library installed in `/usr/lib64` on x86_64 and in `/usr/local/lib` on aarch64. With the latter case, it was needed to add `/usr/local/lib` in LD_LIBRARY_PATH"
but redis library seems to be in `/usr/local/lib64`

so just using this:
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:/usr/local/lib64
there was already a cmake installed:
/usr/bin/
cmake version 3.26.5
after make and make install of cmake-3.30.0-rc4
cmake version 3.30 is in:
/usr/local/bin/
can add to path as:

    `export PATH=/usr/local/bin:$PATH`

also compiled spdlog - but may not be needed since arnaud notes that it was only installed manually for aarch64

when using cmake for  Arnaud's swamp-cpp
got warning:
The FindBoost module is removed. and some policy messages
boost seems to be located in the messages that follow - so moving on


## uninstall redis

ran yum remove redis
and then cleaned up a few more places:
https://askubuntu.com/a/971207

## install redict
open source version of redis

dnf install redict
systemctl enable redict
systemctl start redict
systemctl status redict

## install of slow control


* which slow control?
* which run control
https://gitlab.cern.ch/hgcal-daq-sw/serenity-daq
* which repos are important?
https://gitlab.cern.ch/hgcal-daq-sw/serenity-daq
- swamp-cpp
- run_control_cpp
slow_control_collector
hgcal_xdaq_executer
hgcal_xdaq_base
run_control_textual
docker_images
- frontend-controller
config_generator
slow_control_configuration
hgc-run-control
hgcal_xdaq_model
slow_control_cpp
aligner_cpp
kubernetes-setup
hgc-run-data-reader
run_control
state_machine
slow_control
dummyRestFastAPI

* what is your workflow for rpm development?

* this version of cmsos?
baseurl=https://cmsos.web.cern.ch/repo/development/core/master/alma9/x86_64/RPMS/

* Install slow control: How to get these packages for slow control:
https://gitlab.cern.ch/hgcal-daq-sw/serenity-daq/frontend-controller/-/blob/production/Makefile?ref_type=heads#L41-51
**in serenity:
alma base image:
https://gitlab.cern.ch/hgcal-daq-sw/serenity-daq/docker_images/-/blob/production/ci/images/base/almalinux/9/x86_64/Dockerfile?ref_type=heads
**hgcal image built on top of base:
https://gitlab.cern.ch/hgcal-daq-sw/serenity-daq/docker_images/-/blob/production/ci/images/hgcal/almalinux/9/x86_64/Dockerfile?ref_type=heads

* xdaq is started here (with run.sh):
https://gitlab.cern.ch/hgcal-daq-sw/serenity-daq/frontend-controller/-/blob/production/run.sh?ref_type=heads#L31
** what sends commands to xdaq?
** where to get this package of Paul's:
pdauncey/hgc-subsystem-plugin/
setUP_FE_beamtest_jan2025.sh

* Alignment which script does this?
* where is hgcal_fc.py?
https://gitlab.cern.ch/hgcal-daq-sw/serenity-daq/frontend-controller/-/blob/production/src/common/FrontendController.cc?ref_type=heads#L127
and
** setEnv from hgc_utils?

* how to install herd?
- for fast commands
- ask Paul for HERD plugins
tcds2_emu block in the fw
arnauds ver in aligner-cpp other branch


hardware_configs - generator configs go here
sqlite DN from config-generator loader.py



collector saves cache of configs
type of run
and config of relay

run control to HERD fastAPI
run registry provider through clara
slink
10G links using UDP
UDP receiver PC

enable regular l1a capture data with emp butler


emp_
1aa econ when sees resetreset

ccccff08
emp_capture_bx_range

Textual gui to control the



xdaq is in docker container

mfDefs.hgcal
include/frontend-controller/version.h

nfs_shared where the sqlite database is
nfs server - being mounted to multiple places

running docker compose

## install xdaq  and frontend-controller
--> put the follwing in /etc/yum.repos.d/cmsos.repo
[cmsos-core]
name=cmsos-core
baseurl=https://cmsos.web.cern.ch/repo/development/core/master/alma9/x86_64/RPMS/
gpgcheck=0
enabled=1

dnf groupinstall -y cmsos_core
dnf install -y libuuid-devel
dnf clean all

dnf install -y sqlite

--> put both of these in /etc/yum.repos.d/hgcal-daq-sw.repo
[hgcal-daq-sw]
name=HCGAL-DAQ-SW
baseurl=https://hgc-online-sw.web.cern.ch/hgc-online-sw/hgcal-daq-sw/almalinux/9/x86_64/
gpgcheck=0
enabled=1
cost=2
metadata_expire=1m

[hgcal-daq-sw-test]
name=HCGAL-DAQ-SW
baseurl=https://hgc-online-sw.web.cern.ch/hgc-online-sw/hgcal-daq-sw-test/almalinux/9/x86_64/
gpgcheck=0
enabled=0
cost=1
metadata_expire=1m


then
dnf install -y cmsos-hgcal-xdaqbase* --enablerepo=hgcal-daq-sw
(or --enablerepo=hgcal-daq-sw-test)
(to use production version or latest version

then:
dnf clean all


then from swamp-cpp can run
`make install`
swamp library will be installed in /opt/swamp/lib. Header files will be installed in /opt/swamp/include

(then need mfDefs.hgcal in the parent directory of frontend-controller)
https://gitlab.cern.ch/hgcal-daq-sw/serenity-daq/docker_images/-/blob/production/resources/mfDefs.hgcal?ref_type=heads

then in `frontend-controller` directory run make (successful)


config file for redis, redict (sets IP address)
/etc/redict/redict.conf



loader,pyy with deep option


offset of module number and bus number is now in effect - to match the engine schematics


Move to the NEW ENGINE


emq

mosquitto
mqtt broker
dnf install mosquitto
systemctl start mosquitto
systemctl enable mosquitto
systemctl status mosquitto


run it as a service

phase training on econ
messages output of alignment


sqlitebrowser

mqtt brocker takes info from alignment etc (asic parameters) from frontend-controller. that output can be send to things like grafana



install mosquitto

## start sqlite database


python generator.py -i fnal_10deg_sil.json -o hwcfg_fnal_10deg_sil.yaml
then had to edit to point to correct connections file, emp device, and emp channel

from tarball serenityU_DB
copied to temp dir in frontend-controller

need to load with recursive (all files in directory) and deep (include children directories)
python loader.py temp/serenityU_DB -r -f -d -db temp/serenityU_DB.db

cat Scheme.sql | sqlite3 temp/serenityU_DB.db
python loader.py temp/serenityU_DB -r -d -db temp/serenityU_DB.db
python loader.py hwcfg_fnal_10deg_sil.yaml -db temp/serenityU_DB.db

from frontend-controller/
-> make sure the correctdb file is in yaml/profile.yml
-> make sure the correct hostname and mqtt brocker application is in yaml/profile.yml
./run.sh

from another window
the hardware config file name is the one in the sqlite databoas, entered with loader.py - without the hwcfg in name
hwcfg_fnal_10deg_sil.yaml becomes:  fnal_10deg_sil

curl -X POST http://0.0.0.0:8080/fcontroller/coldstart -d '{"hardware_cfg" : "fnal_10deg_sil"}'
curl -X POST http://0.0.0.0:8080/fcontroller/initialize -d '{}'

## reset software emp trasactor

when swamp freezes, sometimes need to reset emptransactor dev
rm -f /dev/shm/sem.labc2-fnal-gov:emptransactor0

## textual interface

in swamp_env pyvenv
pip install textual textual-dev
pip install pytz httpx

## make changes to hgcal xdaq base

make; make rpm
rpm --reinstall rpm/cmsos-hgcal-xdaqbase*

then have to make frontendcontroller again



# New VCU fw

hgcal_fc

* where is hgcal_fc.py?
o
HERD

## debug motherboard

- write registers, new values, read back
- write whole yaml files
- break down steps, repeat tests




## learning to load fw from command line
localhost:3121/xilinx_tcf/Digilent/210308B3AC58
210308B3AC58
{target_ctx jsn-JTAG-SMT2NC-210308B3AC58 level 0 node_id 1 is_open 1 is_active 1 is_current 0 name
    {Digilent JTAG-SMT2NC 210308B3AC58} jtag_cable_name
    {Digilent JTAG-SMT2NC 210308B3AC58} state
    {} jtag_cable_manufacturer Digilent jtag_cable_product JTAG-SMT2NC jtag_cable_serial 210308B3AC58}

{target_ctx jsn-JTAG-SMT2NC-210308B3AC58-14b31093-0 level 1 node_id 2 is_open 1 is_active 1 is_current 1 name xcvu9p jtag_cable_name
    {Digilent JTAG-SMT2NC 210308B3AC58} state
    {} jtag_cable_manufacturer Digilent jtag_cable_product JTAG-SMT2NC jtag_cable_serial 210308B3AC58 idcode 14b31093 irlen 18 is_fpga 1}


for xsct
installed xlsclients
 * Waiting in queue...
 * Loading list of packages....
The following packages have to be installed:
 libXxf86dga-1.1.5-8.el9.x86_64	X.Org X11 libXxf86dga runtime library
 libdmx-1.1.4-12.el9.x86_64	X.Org X11 DMX runtime library
 xorg-x11-utils-7.5-40.el9.x86_64	X.Org X11 X client utilities



https://docs.amd.com/r/2022.1-English/ug1400-vitis-embedded/fpga
https://docs.amd.com/r/2022.1-English/ug1400-vitis-embedded/Running-an-Application-in-Non-Interactive-Mode
https://wiki.analog.com/resources/eval/user-guides/ad-fmcdaq3-ebz/quickstart/vcu118
https://docs.amd.com/r/2021.2-English/ug1400-vitis-embedded/Running-Tcl-Scripts

## build top_lpgbt_hgc firmware


yum -y install yamllint
inside ippb venv
pip install lxml



## install influxdb and grafana

sudo yum install influxdb2
sudo yum install influxdb2-cli


service influxdb start
service influxdb status

started installing grafana from webpage too - but was already installed (with hgcal repo?)

sudo systemctl start grafana-server

to start it at boot:
sudo systemctl enable grafana-server.service



## update emp-toolbox

install pybind11
https://pybind11.readthedocs.io/en/stable/basics.html

This was installed when emptoolbox local was built and worked (not sure it is needed though)
build pybind11 (with cmake3 which is cmake3.26)
mkdir build
cd build
cmake3 ..
make check -j 4
make install

emp-toolbox:
https://gitlab.cern.ch/p2-xware/software/emp-toolbox/-/tree/tcds2-configure-wait-for-clock-lock-callback?ref_type=heads
git hash:
967b946abd1944ca47751b806ad5f3f80db46e1d

compile in
/home/agrummer/emp-local-build/emp-toolbox/
needed to have --recursive submmodule - which had a pybind11 dir
then it worked

Didn't use this (wasn't building anyway - missing Python.h file:) and I deleted the directory
compile ipbus software:
https://github.com/ipbus/ipbus-software.git


## pcvcu at CERN 2025 May13


followed swamp-cpp readme instructions to install the following packages (also installed cmake 3.26 with yum install cmake)

used cmake3 in place of cmake for all compilations

redict (not redis)
(and enabled and started)
hiredis
redis-plus-plus
export LDLIBRARY
spdlog (also ran make install at the end of spdlog)


git clone https://gitlab.cern.ch/hgcal-daq-sw/serenity-daq/swamp-cpp.git

instructions above for installing xdaq:
/etc/yum.repos.d/cmsos.repo
/etc/yum.repos.d/hgcal-daq-sw.repo

## make changes to hgcal xdaq base

(must source env.sh first)
make; make rpm
rpm --reinstall rpm/cmsos-hgcal-xdaqbase*

then have to make frontendcontroller again

have to add the mfDefs.hgcal file to the directory above


## install cvmfs:

https://cvmfs.readthedocs.io/en/stable/cpt-quickstart.html

yum install -y https://cvmrepo.s3.cern.ch/cvmrepo/yum/cvmfs-release-latest.noarch.rpm
yum install -y cvmfs
ls /etc/auto.master.d/cvmfs.autofs
which cvmfs_config
cvmfs_config setup
ls -l /etc/auto.cvmfs
systemctl status autofs
nvim /etc/cvmfs/default.local # grabbed defaults from lxplus
cvmfs_config probe
ls /cvmfs/
ls /cvmfs/cms.cern.ch/
source /cvmfs/cms.cern.ch/cmsset_default.sh


contents of:
/etc/cvmfs/default.local

CVMFS_DNS_MIN_TTL='300'
CVMFS_QUOTA_LIMIT='67370'
CVMFS_CLIENT_PROFILE=single
CVMFS_CACHE_BASE='/var/lib/cvmfs'
CVMFS_REPOSITORIES='cms.cern.ch'

### adding SITECONF
https://twiki.cern.ch/twiki/bin/view/Main/RobinGitlabCICMSSW

need to set the site-local-config.xml file
"This XML file contains instructions about proxies and how to resolve input filenames at a given site."
add
export CMS_LOCAL_SITE=T1_US_FNAL
to /etc/cvmfs/default.local
this will set the sym link
/cvmfs/cms.cern.ch/SITECONF/local/ -> T1_US_FNAL
this should exist now:
/cvmfs/cms.cern.ch/SITECONF/local/JobConfig/site-local-config.xml
check symlink
ls -l /cvmfs/cms.cern.ch/SITECONF/local
if needed restart autofs with:
systemctl restart autofs

or
work around here:
https://github.com/reanahub/reana-workflow-controller/issues/238
or we grab the
site-local-config.xml
from
/cvmfs/cms.cern.ch/SITECONF/T1_US_FNAL/JobConfig/site-local-config.xml
put it in a local directory
and after cmsenv command change this to:
export CMS_PATH=<local directory>
(might have to have JobConfig directory inside local directory

note, this variable seems to be specific to the cvmfs configuration - not global to bash:
$CMS_LOCAL_SITE
(echo $CMS_LOCAL_SITE doesn't show anything on lpc)

## to reload and include GRID in config needed this:

super useful for reseting the cvmfs:
cvmfs_config reload

this is an old setup script...:
source /cvmfs/grid.cern.ch/etc/profile.d/setup-cvmfs-ui.sh
this was probably not right:
voms-proxy-init was missing a library after setting up grid
--> old, probably dont do: dnf install libnsl
(had to be run in a fresh terminal)


you need grid.cern.ch in
/etc/cvmfs/default.local
CVMFS_REPOSITORIES='cms.cern.ch,grid.cern.ch'

then
cvmfs_config reload
cvmfs_config setup
cvmfs_config probe
systemctl status autofs
systemctl restart autofs

The rest of grid is setup with bash script:

```
export GRID_UI=/cvmfs/grid.cern.ch/alma9-ui-current

# Set up UI executables
export PATH=$GRID_UI/usr/bin:$GRID_UI/usr/sbin:$PATH

# Ensure libraries are found
export LD_LIBRARY_PATH=$GRID_UI/usr/lib64:$GRID_UI/usr/lib:$LD_LIBRARY_PATH

# Optional: man pages
export MANPATH=$GRID_UI/usr/share/man:$MANPATH

# Use CVMFS certificates and VOMS data
export X509_CERT_DIR=/cvmfs/grid.cern.ch/etc/grid-security/certificates
```

and grid certificate in .globus directory
PKS#12 format requires password everytime the the grid cert (pem key) is used
PKS#1 format does not require password
The grid cert is called when running voms-proxy-init, and also for xrdcp (will request a new proxy if one does not exist)
proxy in /tmp/x509up_u<userID>
each user probably needs their own proxy


could use pass and gpg to renew the grid cert with a cron job
didn't actual us this option tho (using PKS#1 instead):
dnf install pass gnupg

created a setup grid file to run as a cron job:
```bash
# id for hgcal_dev: 1001
ids=(0 58219)
# gid=5063(us_cms)

for id in "${ids[@]}"; do
    voms-proxy-init --rfc --voms cms -hours 72 --vomses /cvmfs/grid.cern.ch/etc/grid-security/vomses --vomsdir /cvmfs/grid.cern.ch/etc/grid-security/vomsdir --out "/tmp/x509up_u${id}"
    if (( id > 0 )); then
        chown "${id}:5063" "/tmp/x509up_u${id}"
    fi
done
```

### cron jobs
to edit cronjobs:
crontab -e
to list cron jobs:
crontab -l

the shell file is here: /root/cronGrid/setupGridProxies.sh

check the proxies:
ls -l /tmp/x509up_u*

if errors occur they will go to the mail file:
`/var/spool/mail/root`
check the mail by reading the file or interactively with the mail command:
mail


# snmp install on labc2

dnf install net-snmp net-snmp-utils
systemctl status snmpd
also copy the MIB file to
WIENER-CRATE-MIB.txt
/usr/share/snmp/mibs


# DQM install:

how to use:
https://hgcaldocs.web.cern.ch/RawDataHandling/dqm_sysval/

virtual machine install instructions:
https://github.com/cms-DQM/dqmgui_prod_deployment/wiki/Deployment-on-OpenStack

hgcal notes from 2024 beam test:
https://github.com/CMS-HGCAL/hgc-dqmgui?tab=readme-ov-file

## dependecies
list of required packages:
https://raw.githubusercontent.com/cms-DQM/dqmgui_prod_deployment/main/os_packages.txt

the packages that are not already installed:
R-RInside-devel R-Rcpp-devel R-devel avahi-compat-libdns_sd-devel boost-python3-devel cfitsio-devel fftw-devel ftgl-devel gcc-gfortran glew-devel graphviz-devel gsl-devel jemalloc-devel mesa-libGL-devel mesa-libGLU mesa-libGLU-devel openldap-devel perl perl-Env perl-Switch protobuf-devel

removed
xrootd-client (should already be available from cvmfs)
and
python38 python38-devel (failed on alma 9)


from ~/workspace/dqm:
dryrun:
yum install --assumeno $(cat packagesThatWereNotPreviouslyInstalled.txt)
--> 461 Packages
Total download size: 416 M
Installed size: 815 M

actual install:
yum install -y $(cat packagesThatWereNotPreviouslyInstalled.txt)

most of the download of dependencies seems to be latex...


trying root version 6.36
yum install root


HGCal install notes from 2024 beam test:
https://github.com/CMS-HGCAL/hgc-dqmgui?tab=readme-ov-file

## trying to use podman instead...

podman search alma8
podman pull docker.io/cern/alma8-base

podman was already installed
but have to install podman-compose
dnf install podman-compose -y

No match for argument: cfitsio-devel
No match for argument: ftgl-devel
No match for argument: jemalloc-devel
Package python38-3.8.17-2.module_el8.9.0+3633+e453b53a.x86_64 is already installed.
No match for argument: xrootd-client


need:
curl -L https://xrootd.web.cern.ch/xrootd.repo -o /etc/yum.repos.d/xrootd.repo


split the docker build into several steps - all requirements seemt to install now

adduser dqm
mkdir -p /data/srv
chown -R dqm /data/srv
su dqm
mkdir -p /dqmdata/dqm
chown -R dqm /dqmdata

cant get: Compatibility standard C++ libraries
compat-libstdc++-33
with dnf install...

move to fnal worker node docker
avahi-compat-libdns_sd-devel boost-python3-devel glew-devel graphviz-devel protobuf-devel
perl-Switch

-C is for use the cache rather than check
don't check gpg (the xrootd is having trouble for root installed package access for dqm user)
-C --nogpgcheck

add `-C --nogpgcheck`
in
/home/dqm/dqmgui_deployment/deploy_dqmgui.sh
line 83


need to add:
python -m ensurepip --upgrade

python -m venv pyvenv
source pyvenv/bin/activate

export LC_ALL=C.UTF-8
or export LC_ALL=en_US.UTF-8

limit number of cpus for root build
taskset -c 0-10 bash /home/dqm/dqmgui_deployment/deploy_dqmgui.sh do_preliminary_checks=0


## download

curl -L https://github.com/cms-DQM/dqmgui_prod_deployment/releases/download/python_3.8_deployment_HG2402b_dqmgui_10.0.1_root_v6-28-10/dqmgui_python_3.8_deployment_HG2402b_dqmgui_10.0.1_root_v6-28-10.tar.gz --output /tmp/dqmgui_installation_package.tar.gz

change the check in
"/data/srv/HG2501a/config/dqmgui/manage"
check() {
  echo "skip md5sum check"
  # CHECK=$(echo "$1" | md5sum | awk '{print $1}')
  # if [ $CHECK != 94e261a5a70785552d34a65068819993 ]; then
    # echo "$0: cannot complete operation, please check documentation." 1>&2
    # exit 2
  # fi
}

also:
source /data/srv/current/apps/dqmgui/128/etc/profile.d/env.sh
source /data/srv/HG2501a/sw/venv/bin/activate

/data/srv/current/config/dqmgui/manage status
/data/srv/current/config/dqmgui/manage -f online start "I did read documentation"


http://localhost:8070/dqm/online-dev/session/

vm=labc2-fnal-gov; visDQMUpload http://${vm}.cern.ch:8070/dqm/online-dev DQM_V0001_HGCAL_R000400006.root

exit podman without stopping it:
ctrl-p ctrl-q

used --server host
and --privileged

### copy a podman between accounts
https://www.redhat.com/en/blog/podman-transfer-container-images-without-registry

podman image scp root@localhost::IMAGE USER@localhost::
podman image scp root@localhost::localhost/dqmserver hgcal_dev@localhost::

had to:
dnf install systemd-container

copy a local image:
#### As root
export TMPDIR=/home/hgcal_dev/tmp
podman image save -o /home/hgcal_dev/tmp/myimage.tar my-image-name

#### Give access to user
chown hgcal_dev: /home/hgcal_dev/tmp/myimage.tar

#### As user
export TMPDIR=/home/hgcal_dev/tmp
podman image load -i /home/hgcal_dev/tmp/myimage.tar


# CMSSW install

release CMSSW_15_1_0_pre4 was planned for el8, but we are on el9

# Nvim configuration

Lazy nvim configuration
`scp -r ~/.config/nvim labc2_dev:~/.config/`
might have to mkdir ~/.local/share/nvim
then open
nvim for packages to be installed


# install singularity:

dnf install apptainer

# update grafana:

rpm --import https://rpm.grafana.com/gpg.key

sudo dnf clean all

actually needed this:
sudo dnf clean all
sudo rm -rf /var/cache/dnf
sudo dnf makecache

add /etc/yum.repos.d/grafana.repo
with:
```
[grafana]
name = grafana
baseurl = https://rpm.grafana.com
repo_gpgcheck = 1
enabled = 1
gpgcheck = 1
gpgkey = https://rpm.grafana.com/gpg.key
sslverify = 1
sslcacert = /etc/pki/tls/certs/ca-bundle.crt
```


then:
systemctl status grafana-server
systemctl enable grafana-server
systemctl start grafana-server
