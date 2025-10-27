        utils/fpgautil -b /boot/zusys_wrapper.bit -o dtsi/trophy/trophy_pl.dtbo \
                && echo "After loading" \
                && i2cdetect -l \
                && cat /sys/class/uio/uio*/name \
                && cat /sys/class/gpio/gpiochip*/label
# I would have liked to unmount /boot, but make seems to be using it so, "nope".
#lsof +D /boot/
#umount /boot


rocchar: utils/fpgautil /boot/zusys_wrapper.bit dtsi/rocchar/rocchar_pl.dtbo uio_pdrv_genirq
        utils/fpgautil -R
        utils/fpgautil -b /boot/zusys_wrapper.bit -o dtsi/rocchar/rocchar_pl.dtbo \
                && echo "After loading" \
                && i2cdetect -l \
                && cat /sys/class/uio/uio*/name \
                && cat /sys/class/gpio/gpiochip*/label

tbtester: utils/fpgautil /home/HGCAL_dev/device-tree/tileboard-tester-v1p0.bit dtsi/tb-tester/tb-tester_pl.dtbo uio_pdrv_genirq
        utils/fpgautil -R
        utils/fpgautil -b /home/HGCAL_dev/device-tree/tileboard-tester-v1p0.bit -o dtsi/tb-tester/tb-tester_pl.dtbo \
                && echo "After loading" \
                && cat /sys/class/uio/uio*/name \

econ-t-internal_loopback: utils/fpgautil /home/HGCAL_dev/device-tree/econ-t-internal_loopback-fix-5.bit dtsi/econ-t-internal_loopback/econ-t-internal_loopback_pl.dtbo uio_pdrv_genirq
        utils/fpgautil -R
        utils/fpgautil -b /home/HGCAL_dev/device-tree/econ-t-internal_loopback-fix-5.bit -o dtsi/econ-t-internal_loopback/econ-t-internal_loopback_pl.dtbo \
                && echo "After loading" \
                && cat /sys/class/uio/uio*/name \

interposer: utils/fpgautil /home/HGCAL_dev/device-tree/interposer.bit dtsi/interposer/interposer_pl.dtbo uio_pdrv_genirq
        utils/fpgautil -R
        utils/fpgautil -b /home/HGCAL_dev/device-tree/interposer.bit -o dtsi/interposer/interposer_pl.dtbo \
                && echo "After loading" \
                && cat /sys/class/uio/uio*/name \


list:
        utils/list_devices.sh
dtsi/trophy/trophy_pl.dtbo:
        $(MAKE) $(MFLAGS) -C dtsi/trophy
dtsi/rocchar/rocchar_pl.dtbo:
        $(MAKE) $(MFLAGS) -C dtsi/rocchar
dtsi/tb-tester/tb-tester_pl.dtbo:
        $(MAKE) $(MFLAGS) -C dtsi/tb-tester
dtsi/econ-t-internal_loopback/econ-t-internal_loopback_pl.dtbo:
        $(MAKE) $(MFLAGS) -C dtsi/econ-t-internal_loopback
dtsi/interposer/interposer_pl.dtbo:
        $(MAKE) $(MFLAGS) -C dtsi/interposer
utils/fpgautil:
       CalibL1A:          0
      Linkreset:          0
            L1A:          0
      FC errors:          0
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:      77801
      FC errors:          0
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$ ls
__pycache__   clkRates.cpp~  clkSource.cpp~  fcSpy       fcf_clean       iic.py      interposer.cpp   readBackTest.cpp   zmq_test.py
clkRates      clkSource      econ_i2c.py     fcSpy.cpp   fcf_clean.cpp   iic.py~     interposer.cpp~  readBackTest.cpp~  zmq_test.py~
clkRates.cpp  clkSource.cpp  econ_i2c.py~    fcSpy.cpp~  fcf_clean.cpp~  interposer  readBackTest     zmq.py~
[HGCAL_dev@hexacon1 test]$ cd
[HGCAL_dev@hexacon1 ~]$ ls
bin          do_load.sh                    econ-t-internal_loopback.bit   lib          mylittledt  runFC.sh  source          test.txt
device-tree  econ-d-internal_loopback.bit  interposer_DirectDriveSCL.bit  mldt.tar.gz  oldDT       runLC.sh  te0803_pl.dtbo
[HGCAL_dev@hexacon1 ~]$ cd mylittledt/
[HGCAL_dev@hexacon1 mylittledt]$ ls
Makefile  README.md  dtsi  notes  readback.bin  rules.mk  utils
[HGCAL_dev@hexacon1 mylittledt]$ vim Makefile
[HGCAL_dev@hexacon1 mylittledt]$
[HGCAL_dev@hexacon1 mylittledt]$
[HGCAL_dev@hexacon1 mylittledt]$
[HGCAL_dev@hexacon1 mylittledt]$
[HGCAL_dev@hexacon1 mylittledt]$ cd



































"interposer_test.cxx" 42L, 781C
#include <cstdio>
#include <ctime>
#include <vector>

#include <boost/cstdint.hpp>
#include <boost/program_options.hpp>

#include <uhal/uhal.hpp>

#include "Interposer.h"

#include <boost/cstdint.hpp>
#include <boost/program_options.hpp>
#include <cstdio>
#include <ctime>
#include <vector>

#include <boost/cstdint.hpp>
#include <boost/program_options.hpp>

#include <uhal/uhal.hpp>

#include "Interposer.h"

int main()
{
    uhal::setLogLevelTo(uhal::Warning());

    uhal::ConnectionManager manager( "file://address_table/connection.xml" );
    uhal::HwInterface ipbushw = manager.getDevice( "interposer" );

    Interposer itp(&ipbushw);

    itp.resetROC();
    usleep(100);
    itp.resetROCI2C();
    usleep(100);
    itp.resyncLoad();
    usleep(1000);

    itp.setAutoDelayMode(false);
    usleep(10);
    itp.setAutoDelayMode(true);

    itp.printDelays();

    itp.setReadoutPassthrough(true);

    itp.resetLinks();
    itp.alignLinks();

    itp.interalignLinks();
[HGCAL_dev@hexacon1 ~]$ ls
bin          do_load.sh                    econ-t-internal_loopback.bit   lib          mylittledt  runFC.sh  source          test.txt
device-tree  econ-d-internal_loopback.bit  interposer_DirectDriveSCL.bit  mldt.tar.gz  oldDT       runLC.sh  te0803_pl.dtbo
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$ pwd
/home/HGCAL_dev
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$ ls
bin          do_load.sh                    econ-t-internal_loopback.bit   lib          mylittledt  runFC.sh  source          test.txt
device-tree  econ-d-internal_loopback.bit  interposer_DirectDriveSCL.bit  mldt.tar.gz  oldDT       runLC.sh  te0803_pl.dtbo
[HGCAL_dev@hexacon1 ~]$ cd source/
[HGCAL_dev@hexacon1 source]$ ls
fast-control  gbt-sca-sw  hexactrl-sw  interposer  ipbus-software  link_capture  link_capture_old  test  zynq_test_fw  zynq_tset_sw
[HGCAL_dev@hexacon1 source]$ cd interposer/
[HGCAL_dev@hexacon1 interposer]$ ls
CMakeLists.txt  CMakeLists.txt~  address_table  bin  build  cmake  env.sh  env.sh~  sources
[HGCAL_dev@hexacon1 interposer]$ cd bin/
[HGCAL_dev@hexacon1 bin]$ ls
interposer_server  interposer_test
[HGCAL_dev@hexacon1 bin]$ cd ..
[HGCAL_dev@hexacon1 interposer]$ ls
CMakeLists.txt  CMakeLists.txt~  address_table  bin  build  cmake  env.sh  env.sh~  sources
[HGCAL_dev@hexacon1 interposer]$ cd sources/
[HGCAL_dev@hexacon1 sources]$ ls
main
[HGCAL_dev@hexacon1 sources]$ cd main/
[HGCAL_dev@hexacon1 main]$ ls
executables  include  src
[HGCAL_dev@hexacon1 main]$ cd executables/
[HGCAL_dev@hexacon1 executables]$ ls
interposer_server.cxx  interposer_server.cxx~  interposer_test.cxx  interposer_test.cxx~
[HGCAL_dev@hexacon1 executables]$ vim interposer_test.cxx
[HGCAL_dev@hexacon1 executables]$ cd ../
[HGCAL_dev@hexacon1 main]$ ls
executables  include  src
[HGCAL_dev@hexacon1 main]$ cd ../..
[HGCAL_dev@hexacon1 interposer]$ ls
CMakeLists.txt  CMakeLists.txt~  address_table  bin  build  cmake  env.sh  env.sh~  sources
[HGCAL_dev@hexacon1 interposer]$ cd bin/
[HGCAL_dev@hexacon1 bin]$ ls
interposer_server  interposer_test
[HGCAL_dev@hexacon1 bin]$ ./interposer_test
./interposer_test: error while loading shared libraries: libcactus_uhal_log.so.2.6: cannot open shared object file: No such file or directory
[HGCAL_dev@hexacon1 bin]$ cd ..
[HGCAL_dev@hexacon1 interposer]$ ls
CMakeLists.txt  CMakeLists.txt~  address_table  bin  build  cmake  env.sh  env.sh~  sources
[HGCAL_dev@hexacon1 interposer]$ source env.sh
[HGCAL_dev@hexacon1 interposer]$ cd bin/
[HGCAL_dev@hexacon1 bin]$ ls
interposer_server  interposer_test
[HGCAL_dev@hexacon1 bin]$ ./interposer_test
18-11-21 22:52:21.524693 [7f81212000] ERROR - No matching files for expression "address_table/connection.xml" with parent path "/home/HGCAL_dev/source/interposer/bin"
terminate called after throwing an instance of 'uhal::exception::FileNotFound'
  what():  No matching files for expression "address_table/connection.xml" with parent path "/home/HGCAL_dev/source/interposer/bin"

Aborted
[HGCAL_dev@hexacon1 bin]$ cd ..
[HGCAL_dev@hexacon1 interposer]$ ls
CMakeLists.txt  CMakeLists.txt~  address_table  bin  build  cmake  env.sh  env.sh~  sources
[HGCAL_dev@hexacon1 interposer]$ ./bin/interposer_test
terminate called after throwing an instance of 'boost::interprocess::interprocess_exception'
  what():  Permission denied
Aborted
[HGCAL_dev@hexacon1 interposer]$ sudo ./bin/interposer_test
[sudo] password for HGCAL_dev:
Sorry, try again.
[sudo] password for HGCAL_dev:
./bin/interposer_test: error while loading shared libraries: libcactus_uhal_log.so.2.6: cannot open shared object file: No such file or directory
[HGCAL_dev@hexacon1 interposer]$ sudo ./bin/interposer_test
./bin/interposer_test: error while loading shared libraries: libcactus_uhal_log.so.2.6: cannot open shared object file: No such file or directory
[HGCAL_dev@hexacon1 interposer]$ cd bin/
[HGCAL_dev@hexacon1 bin]$ ls
interposer_server  interposer_test
[HGCAL_dev@hexacon1 bin]$ sudo ./interposer_test
./interposer_test: error while loading shared libraries: libcactus_uhal_log.so.2.6: cannot open shared object file: No such file or directory
[HGCAL_dev@hexacon1 bin]$ sudo -h
sudo - execute a command as another user

usage: sudo -h | -K | -k | -V
usage: sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]
usage: sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]
usage: sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] [VAR=value] [-i|-s] [<command>]
usage: sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] file ...

Options:
  -A, --askpass                 use a helper program for password prompting
  -b, --background              run command in the background
  -C, --close-from=num          close all file descriptors >= num
  -E, --preserve-env            preserve user environment when running command
      --preserve-env=list       preserve specific environment variables
  -e, --edit                    edit files instead of running a command
  -g, --group=group             run command as the specified group name or ID
  -H, --set-home                set HOME variable to target user's home dir
  -h, --help                    display help message and exit
  -h, --host=host               run command on host (if supported by plugin)
  -i, --login                   run login shell as the target user; a command may also be specified
  -K, --remove-timestamp        remove timestamp file completely
  -k, --reset-timestamp         invalidate timestamp file
  -l, --list                    list user's privileges or check a specific command; use twice for longer format
  -n, --non-interactive         non-interactive mode, no prompts are used
  -P, --preserve-groups         preserve group vector instead of setting to target's
  -p, --prompt=prompt           use the specified password prompt
  -r, --role=role               create SELinux security context with specified role
  -S, --stdin                   read password from standard input
  -s, --shell                   run shell as the target user; a command may also be specified
  -t, --type=type               create SELinux security context with specified type
  -T, --command-timeout=timeout terminate command after the specified time limit
  -U, --other-user=user         in list mode, display privileges for user
  -u, --user=user               run command (or edit file) as specified user name or ID
  -V, --version                 display version information and exit
  -v, --validate                update user's timestamp without running a command
  --                            stop processing command line arguments
[HGCAL_dev@hexacon1 bin]$
[HGCAL_dev@hexacon1 bin]$
[HGCAL_dev@hexacon1 bin]$ ls
interposer_server  interposer_test
[HGCAL_dev@hexacon1 bin]$ cd ..
[HGCAL_dev@hexacon1 interposer]$ ls
CMakeLists.txt  CMakeLists.txt~  address_table  bin  build  cmake  env.sh  env.sh~  sources
[HGCAL_dev@hexacon1 interposer]$ sudo --shell ./bin/interposer_test
./bin/interposer_test: error while loading shared libraries: libcactus_uhal_log.so.2.6: cannot open shared object file: No such file or directory
[HGCAL_dev@hexacon1 interposer]$ client_loop: send disconnect: Broken pipe
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] > clear
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] > krenew
[dhcp-131-225-169-72:~] > lpc
Warning: Permanently added 'cmslpc-sl7.fnal.gov,131.225.204.176' (ECDSA) to the list of known hosts.
Last login: Fri Nov 19 11:33:07 2021 from 131.225.169.72
                              NOTICE TO USERS

       This  is a Federal computer (and/or it is directly connected to a
       Fermilab local network system) that is the property of the United
       States Government.  It is for authorized use only.  Users (autho-
       rized or unauthorized) have no explicit or  implicit  expectation
       of privacy.

       Any  or  all uses of this system and all files on this system may
       be intercepted, monitored, recorded,  copied, audited, inspected,
       and  disclosed  to authorized site, Department of Energy  and law
       enforcement personnel, as  well as authorized officials of  other
       agencies,  both  domestic and foreign.  By using this system, the
       user consents to such interception, monitoring, recording,  copy-
       ing,  auditing,  inspection,  and disclosure at the discretion of
       authorized site or Department of Energy personnel.

       Unauthorized or improper use of this system may result in  admin-
       istrative  disciplinary  action and civil and criminal penalties.
       By continuing to use this system you indicate your  awareness  of
       and  consent to these terms and conditions of use.  LOG OFF IMME-
       DIATELY if you do not agree to  the  conditions  stated  in  this
       warning.

       Fermilab  policy  and  rules for computing, including appropriate
       use, may be found at http://www.fnal.gov/cd/main/cpolicy.html
------------------------------------------------------------------------------
                     ..::Powered by CMS-LPC::..

   Hostname: cmslpc117.fnal.gov          OS Release: SLF 7.9 (Nitrogen)
         IP: 131.225.189.98                  Subnet: 255.255.252.0

     Kernel: 3.10.0-1160.45.1                  Arch: x86_64
        RAM: 11.57 GiB                         Swap: 10.00 GiB
      Cores: 8                              Virtual: rhev

 SSH Logins: 3                             Load Avg: 0.08 0.03 0.05
------------------------------------------------------------------------------
  For information about computing at the LPC: http://lpc.fnal.gov/computing
------------------------------------------------------------------------------
Aidan, your .bash_profile has been completed.
[agrummer@cmslpc117 ~]$ hcalpro
Last login: Fri Nov 19 11:36:58 2021 from cmslpc117.fnal.gov
hcalpro@cmsnghcal01 ~ # ssh HGCAL_dev@192.168.1.95
HGCAL_dev@192.168.1.95's password:
Last login: Thu Nov 18 19:42:33 2021 from gateway
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$ pwd
/home/HGCAL_dev
[HGCAL_dev@hexacon1 ~]$ ls
bin          do_load.sh                    econ-t-internal_loopback.bit   lib          mylittledt  runFC.sh  source          test.txt
device-tree  econ-d-internal_loopback.bit  interposer_DirectDriveSCL.bit  mldt.tar.gz  oldDT       runLC.sh  te0803_pl.dtbo
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$ pwd
/home/HGCAL_dev
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$
[HGCAL_dev@hexacon1 ~]$ cd mylittledt/
[HGCAL_dev@hexacon1 mylittledt]$ ls
Makefile  README.md  dtsi  notes  readback.bin  rules.mk  utils
[HGCAL_dev@hexacon1 mylittledt]$ sudo make interposer
[sudo] password for HGCAL_dev:
rmmod uio_pdrv_genirq && insmod /lib/modules/4.19.0-xilinx-v2019.2/kernel/drivers/uio/uio_pdrv_genirq.ko of_id="linux,uio-pdrv-genirq"
lsmod
Module                  Size  Used by
uio_pdrv_genirq        16384  0
xt_conntrack           16384  3
nf_conntrack          106496  1 xt_conntrack
nf_defrag_ipv6         20480  1 nf_conntrack
nf_defrag_ipv4         16384  1 nf_conntrack
utils/fpgautil -R
utils/fpgautil -b /home/HGCAL_dev/device-tree/interposer.bit -o dtsi/interposer/interposer_pl.dtbo \
	&& echo "After loading" \
	&& cat /sys/class/uio/uio*/name \

mkdir: cannot create directory '/configfs': File exists
Time taken to load DTBO is 3107.000000 Milli Seconds
DTBO loaded through zynqMP FPGA manager successfully
After loading
axi-pmon
axi-pmon
axi_to_ipif_mux
AXI_Full_IPIF
axi_to_ipif_mux
link_capture_AXI
AXI_Full_IPIF
axi_to_ipif_mux
link_capture_AXI
axi_to_ipif_mux
fastcontrol_axi
fastcontrol_recv_axi
axi-pmon
gpio
axi_to_ipif_mux
axi-pmon
AXI_Full_IPIF
AXI_Full_IPIF
axi_to_ipif_mux
link_capture_AXI
axi_to_ipif_mux
link_capture_AXI
[HGCAL_dev@hexacon1 mylittledt]$
[HGCAL_dev@hexacon1 mylittledt]$
[HGCAL_dev@hexacon1 mylittledt]$ pwd
/home/HGCAL_dev/mylittledt
[HGCAL_dev@hexacon1 mylittledt]$
[HGCAL_dev@hexacon1 mylittledt]$
[HGCAL_dev@hexacon1 mylittledt]$
[HGCAL_dev@hexacon1 mylittledt]$ cd ..
[HGCAL_dev@hexacon1 ~]$ ls
bin          do_load.sh                    econ-t-internal_loopback.bit   lib          mylittledt  runFC.sh  source          test.txt
device-tree  econ-d-internal_loopback.bit  interposer_DirectDriveSCL.bit  mldt.tar.gz  oldDT       runLC.sh  te0803_pl.dtbo
[HGCAL_dev@hexacon1 ~]$ cd source/test/
[HGCAL_dev@hexacon1 test]$ ls
__pycache__   clkRates.cpp~  clkSource.cpp~  fcSpy       fcf_clean       iic.py      interposer.cpp   readBackTest.cpp   zmq_test.py
clkRates      clkSource      econ_i2c.py     fcSpy.cpp   fcf_clean.cpp   iic.py~     interposer.cpp~  readBackTest.cpp~  zmq_test.py~
clkRates.cpp  clkSource.cpp  econ_i2c.py~    fcSpy.cpp~  fcf_clean.cpp~  interposer  readBackTest     zmq.py~
[HGCAL_dev@hexacon1 test]$ sudo ./interposer
0:      112       88
1:      135       72
2:      397       96
3:      362       88
4:      244       96
5:      271       88
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   c1c1c1c1
      OrbitSync:    1663341
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          0
      FC errors:   76644769
[HGCAL_dev@hexacon1 test]$ sudo ./clkRates

Clock rates
---------------------------------
       External clk.:   320.6102 MHz
          Master 320:   320.6101 MHz
           Master 40:    40.0763 MHz
          System 160:   160.3050 MHz
           System 40:    40.0763 MHz
          ECON-t 160:   160.3050 MHz

PLL unlock counters
---------------------------------
External pll unlocks:          0
  Master pll unlocks:          0

[HGCAL_dev@hexacon1 test]$ sudo ./clkSource
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:    1663341
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          0
      FC errors:   76644769
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 1
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:    7070707
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          0
      FC errors:          0
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:    7070707
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          0
      FC errors:        159
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   1c1c1c1c
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          0
      FC errors:        318
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   1c1c1c1c
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          0
      FC errors:        478
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          1
      FC errors:        638
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:    7070707
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          1
      FC errors:        799
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:    7070707
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          1
      FC errors:        958
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:    7070707
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          2
      FC errors:       1119
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          2
      FC errors:       1278
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   c1c1c1c1
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:          2
      FC errors:       1437
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:          2
      FC errors:       1596
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   c1c1c1c1
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:          2
      FC errors:       1756
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   1c1c1c1c
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:          2
      FC errors:       1915
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:    7070707
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:          2
      FC errors:       2075
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   1c1c1c1c
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:      62881
      FC errors:       2235
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:      97879
      FC errors:       2395
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   1c1c1c1c
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     292986
      FC errors:       2555
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     292986
      FC errors:       2715
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   c1c1c1c1
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     292986
      FC errors:       2875
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:    7070707
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     292986
      FC errors:       3036
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   1c1c1c1c
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     292986
      FC errors:       3196
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     292986
      FC errors:       3355
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   c1c1c1c1
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     357023
      FC errors:       3515
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     357023
      FC errors:       3674
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     408201
      FC errors:       3834
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   c1c1c1c1
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     430021
      FC errors:       3994
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   1c1c1c1c
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:     451108
      FC errors:       4153
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 1
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   70707070
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          0
      FC errors:          0
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   1c1c1c1c
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          0
            L1A:          0
      FC errors:        159
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   c1c1c1c1
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:          0
      FC errors:        318
[HGCAL_dev@hexacon1 test]$ sudo ./clkSource 2
           RSTB:  1 1 1
       RSTB I2C:  1 1 1
    Resync load:  0 0 0
     Pwr Enable:  1 1 1
       Pwr good:  1 0 0
        ROC err:  0 0 0
   External Clk:  1
     fw version:          6
    pattern spy:   1c1c1c1c
      OrbitSync:          0
            OCR:          0
          Calib:          0
       CalibL1A:          0
      Linkreset:          1
            L1A:          0
      FC errors:        479
[HGCAL_dev@hexacon1 test]$
