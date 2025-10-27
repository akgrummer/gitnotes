Last login: Thu Nov 18 10:05:28 on ttys002
Sir, your .bashrc has been completed.
Thu Nov 18 13:37:56 CST 2021
Sir, your .bash_profile has been completed.

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
[dhcp-131-225-169-72:~] > lpc
Warning: Permanently added 'cmslpc-sl7.fnal.gov,131.225.204.176' (ECDSA) to the list of known hosts.
Last login: Fri Nov  5 14:29:30 2021 from 108.206.197.96
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

   Hostname: cmslpc162.fnal.gov          OS Release: SLF 7.9 (Nitrogen)
         IP: 131.225.189.200                 Subnet: 255.255.252.0

     Kernel: 3.10.0-1160.45.1                  Arch: x86_64
        RAM: 11.57 GiB                         Swap: 10.00 GiB
      Cores: 8                              Virtual: rhev

 SSH Logins: 2                             Load Avg: 0.08 0.04 0.05
------------------------------------------------------------------------------
  For information about computing at the LPC: http://lpc.fnal.gov/computing
------------------------------------------------------------------------------
Aidan, your .bash_profile has been completed.
[agrummer@cmslpc162 ~]$ hcalpro
Last login: Thu Nov 18 12:12:22 2021 from cmslpc172.fnal.gov
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ # pwd
/home/hcalpro
hcalpro@cmsnghcal01 ~ # ssh HGCAL_dev@192.168.1.47
HGCAL_dev@192.168.1.47's password:
Last login: Thu Nov 18 12:09:49 2021 from gateway
[HGCAL_dev@fnal-zcu102-a ~]$
[HGCAL_dev@fnal-zcu102-a ~]$
[HGCAL_dev@fnal-zcu102-a ~]$ pwd
/home/HGCAL_dev
[HGCAL_dev@fnal-zcu102-a ~]$ ls
agrummer  cookbook  fw  hexactrl  hgc-enginev1  jingyu  lib  link_capture  mkrohn  old  src  sw  test.txt  test2.txt
[HGCAL_dev@fnal-zcu102-a ~]$ cd agrummer/HexaCookbook/
[HGCAL_dev@fnal-zcu102-a HexaCookbook]$ ls
coldstart.sh
[HGCAL_dev@fnal-zcu102-a HexaCookbook]$ . coldstart.sh
[sudo] password for HGCAL_dev:
mkdir: cannot create directory '/configfs': File exists
Time taken to load DTBO is 12527.000000 Milli Seconds
DTBO loaded through zynqMP FPGA manager successfully
loaded the firmware
/home/jmmans/src/
check that the path says: /home/jmmans/src/
Press any key to continue
 Back FW 0522  Front FW 0204   Backend Status = 00700008
 Errors =     0   Unlocks =    0
     100 MHz: 100.00000000 MHz
         Ref: 148.51360000 MHz
          TX: 0.00000000 MHz
        TX40: 0.00000000 MHz
         RX0: 282.39770000 MHz
         RX1: 282.39780000 MHz
         RX2: 282.39770000 MHz
      RX0-DV: 0.00000000 MHz
      RX1-DV: 0.00000000 MHz
      RX2-DV: 0.00000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes :
   EGROUP0: (0)
   EGROUP1: (0)
   EGROUP2: (0)
   EGROUP3: (0)
 Uplink modes :
   DAQ-EGROUP0: (0)
   DAQ-EGROUP1: (0)
   DAQ-EGROUP2: (0)
   DAQ-EGROUP3: (0)
   DAQ-EGROUP4: (0)
   DAQ-EGROUP5: (0)
   DAQ-EGROUP6: (0)
   TRIGB-EGROUP0: (0)
   TRIGC-EGROUP0: (0)
Reseting the link
 Status = 0x700008
 Back FW 0522  Front FW 0204   Backend Status = 0177711b
 Errors =     1   Unlocks =    0
     100 MHz: 100.00000000 MHz
         Ref: 320.63990000 MHz
          TX: 320.63990000 MHz
        TX40: 40.08000000 MHz
         RX0: 321.27990000 MHz
         RX1: 320.63990000 MHz
         RX2: 321.27120000 MHz
      RX0-DV: 0.00000000 MHz
      RX1-DV: 0.00000000 MHz
      RX2-DV: 0.00000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes :
   EGROUP0: (0)
   EGROUP1: (0)
   EGROUP2: (0)
   EGROUP3: (0)
 Uplink modes :
   DAQ-EGROUP0: (0)
   DAQ-EGROUP1: (0)
   DAQ-EGROUP2: (0)
   DAQ-EGROUP3: (0)
   DAQ-EGROUP4: (0)
   DAQ-EGROUP5: (0)
   DAQ-EGROUP6: (0)
   TRIGB-EGROUP0: (0)
   TRIGC-EGROUP0: (0)
does the clock say 320?
Press any key to continue
run ./agrummer/cookbook/lpgbtColdstart.sh on the raspberry pi, HGCAL_dev@192.168.1.94
Press any key to continue
running wagonoeer
Working with wagons with SCA S/N 29416 (0x72e8) and 29366 (0x72b6)
output should be: Working with wagons with SCA S/N 29416 (0x72e8) and 29366 (0x72b6)
Press any key to continue
 Back FW 0522  Front FW 0204   Backend Status = 1177711b
 Errors =    10   Unlocks =    0
     100 MHz: 100.00000000 MHz
         Ref: 320.63990000 MHz
          TX: 320.63990000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.63990000 MHz
         RX1: 320.63990000 MHz
         RX2: 321.27030000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 0.00000000 MHz
      RX2-DV: 0.00000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes :
   EGROUP0: (0)
   EGROUP1: (0)
   EGROUP2: (0)
   EGROUP3: (0)
 Uplink modes :
   DAQ-EGROUP0: (0)
   DAQ-EGROUP1: (0)
   DAQ-EGROUP2: (0)
   DAQ-EGROUP3: (0)
   DAQ-EGROUP4: (0)
   DAQ-EGROUP5: (0)
   DAQ-EGROUP6: (0)
   TRIGB-EGROUP0: (0)
   TRIGC-EGROUP0: (0)
************************************************
Does 'RX0-DV' say about 40 Mhz?  If so, congratulations, things are up!
done with zcu setup
now log in to the hexacontroller: HGCAL_dev@192.168.1.91 or 95
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ pwd
/home/pastika/hgc-enginev1
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ls



































"l1a1000_aidan2021Nov18.sh" [New File]
./fast_control.py -- :
~
./fast_control.py -- :
~
./fast_control.py -- :
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
README.md       connections.xml  fast_control.py  gpio_control.py  iic.py               lpgbt_fecerror.py  test_result.py          zcu102_lpgbt.xml
__pycache__     daq_config.py    fmc_test.py      gpio_test.py     interposer_cfg.py    lpgbt_status.py    wagon_hdmi.xml          zcu102_wagon.xml
ber_lpgbt.py    efuse            gbt-sca-sw       ic_dump.py       io_lpgbt.py          setup_lpgbt.py     wagoneer_sca.py         zcu_multitool.py
check_lpgbt.py  efuse.py         gbtsca.xml       ic_test.py       lpgbt_eyeopening.py  test_engine.py     zcu102_fastcontrol.xml
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py -h
usage: fast_control.py [-h] [--status]
                       [--enable {orbit,calib,L1A_genA,L1A_genB,L1A_random}]
                       [--disable {orbit,calib,L1A_genA,L1A_genB,L1A_random}]
                       [--send {internaltest,linkreset,orbitcountreset,daqresync,L1A_genA,L1A_genB,calib}]
                       [--periodic {calib,L1A_genA,L1A_genB}]
                       [--prescale PRESCALE] [--bx BX] [--randoml1a RANDOML1A]

Encoder Fast Controls

optional arguments:
  -h, --help            show this help message and exit
  --status              Report the status of the encoder
  --enable {orbit,calib,L1A_genA,L1A_genB,L1A_random}
                        Enable one of the periodic generators
  --disable {orbit,calib,L1A_genA,L1A_genB,L1A_random}
                        Disable one of the periodic generators
  --send {internaltest,linkreset,orbitcountreset,daqresync,L1A_genA,L1A_genB,calib}
                        Send a single-shot command
  --periodic {calib,L1A_genA,L1A_genB}
                        Adjust settings for the given periodic generator
  --prescale PRESCALE   Set the orbit prescale for the given generator
  --bx BX               Set the BX for the specified signal
  --randoml1a RANDOML1A
                        Set the random L1A period (Log2(BX))
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --send linkreset
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --send L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --send L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ pwd
/home/pastika/hgc-enginev1
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ vim l1a1000_aidan2021Nov18.sh
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --status
Firmware Version = 0x0012 ENABLED
 Command collision errors         :          0
 Orbit sync at BX 3560   DISABLED :          0
 Orbit count reset                :          0
 Link reset count                 :          1
 DAQ Sync count                   :          0
 Internal test count              :          0
 Calibration request     DISABLED :          0
   Prescale : 0            Request BX : 1000   L1A BX : 3540
 Level-1 Accept                   :          2
   Periodic generator A  DISABLED   BX :     0  Orbit prescale : 0
   Periodic generator B  DISABLED   BX :     0  Orbit prescale : 0
   Random generator  DISABLED   Log2(Period) :     9   Average rate : 78125.0000 kHz
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --periodic L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --status
Firmware Version = 0x0012 ENABLED
 Command collision errors         :          0
 Orbit sync at BX 3560   DISABLED :          0
 Orbit count reset                :          0
 Link reset count                 :          1
 DAQ Sync count                   :          0
 Internal test count              :          0
 Calibration request     DISABLED :          0
   Prescale : 0            Request BX : 1000   L1A BX : 3540
 Level-1 Accept                   :          2
   Periodic generator A  DISABLED   BX :     0  Orbit prescale : 0
   Periodic generator B  DISABLED   BX :     0  Orbit prescale : 0
   Random generator  DISABLED   Log2(Period) :     9   Average rate : 78125.0000 kHz
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py -h
usage: fast_control.py [-h] [--status]
                       [--enable {orbit,calib,L1A_genA,L1A_genB,L1A_random}]
                       [--disable {orbit,calib,L1A_genA,L1A_genB,L1A_random}]
                       [--send {internaltest,linkreset,orbitcountreset,daqresync,L1A_genA,L1A_genB,calib}]
                       [--periodic {calib,L1A_genA,L1A_genB}]
                       [--prescale PRESCALE] [--bx BX] [--randoml1a RANDOML1A]

Encoder Fast Controls

optional arguments:
  -h, --help            show this help message and exit
  --status              Report the status of the encoder
  --enable {orbit,calib,L1A_genA,L1A_genB,L1A_random}
                        Enable one of the periodic generators
  --disable {orbit,calib,L1A_genA,L1A_genB,L1A_random}
                        Disable one of the periodic generators
  --send {internaltest,linkreset,orbitcountreset,daqresync,L1A_genA,L1A_genB,calib}
                        Send a single-shot command
  --periodic {calib,L1A_genA,L1A_genB}
                        Adjust settings for the given periodic generator
  --prescale PRESCALE   Set the orbit prescale for the given generator
  --bx BX               Set the BX for the specified signal
  --randoml1a RANDOML1A
                        Set the random L1A period (Log2(BX))
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --enable L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --status
Firmware Version = 0x0012 ENABLED
 Command collision errors         :          0
 Orbit sync at BX 3560   DISABLED :          0
 Orbit count reset                :          0
 Link reset count                 :          1
 DAQ Sync count                   :          0
 Internal test count              :          0
 Calibration request     DISABLED :          0
   Prescale : 0            Request BX : 1000   L1A BX : 3540
 Level-1 Accept                   :      42902
   Periodic generator A   ENABLED   BX :     0  Orbit prescale : 0
   Periodic generator B  DISABLED   BX :     0  Orbit prescale : 0
   Random generator  DISABLED   Log2(Period) :     9   Average rate : 78125.0000 kHz
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --enable L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --enable L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --status
Firmware Version = 0x0012 ENABLED
 Command collision errors         :          0
 Orbit sync at BX 3560   DISABLED :          0
 Orbit count reset                :          0
 Link reset count                 :          1
 DAQ Sync count                   :          0
 Internal test count              :          0
 Calibration request     DISABLED :          0
   Prescale : 0            Request BX : 1000   L1A BX : 3540
 Level-1 Accept                   :     169566
   Periodic generator A   ENABLED   BX :     0  Orbit prescale : 0
   Periodic generator B  DISABLED   BX :     0  Orbit prescale : 0
   Random generator  DISABLED   Log2(Period) :     9   Average rate : 78125.0000 kHz
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py -h
usage: fast_control.py [-h] [--status]
                       [--enable {orbit,calib,L1A_genA,L1A_genB,L1A_random}]
                       [--disable {orbit,calib,L1A_genA,L1A_genB,L1A_random}]
                       [--send {internaltest,linkreset,orbitcountreset,daqresync,L1A_genA,L1A_genB,calib}]
                       [--periodic {calib,L1A_genA,L1A_genB}]
                       [--prescale PRESCALE] [--bx BX] [--randoml1a RANDOML1A]

Encoder Fast Controls

optional arguments:
  -h, --help            show this help message and exit
  --status              Report the status of the encoder
  --enable {orbit,calib,L1A_genA,L1A_genB,L1A_random}
                        Enable one of the periodic generators
  --disable {orbit,calib,L1A_genA,L1A_genB,L1A_random}
                        Disable one of the periodic generators
  --send {internaltest,linkreset,orbitcountreset,daqresync,L1A_genA,L1A_genB,calib}
                        Send a single-shot command
  --periodic {calib,L1A_genA,L1A_genB}
                        Adjust settings for the given periodic generator
  --prescale PRESCALE   Set the orbit prescale for the given generator
  --bx BX               Set the BX for the specified signal
  --randoml1a RANDOML1A
                        Set the random L1A period (Log2(BX))
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --disable L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --status
Firmware Version = 0x0012 ENABLED
 Command collision errors         :          0
 Orbit sync at BX 3560   DISABLED :          0
 Orbit count reset                :          0
 Link reset count                 :          1
 DAQ Sync count                   :          0
 Internal test count              :          0
 Calibration request     DISABLED :          0
   Prescale : 0            Request BX : 1000   L1A BX : 3540
 Level-1 Accept                   :     818044
   Periodic generator A  DISABLED   BX :     0  Orbit prescale : 0
   Periodic generator B  DISABLED   BX :     0  Orbit prescale : 0
   Random generator  DISABLED   Log2(Period) :     9   Average rate : 78125.0000 kHz
import zmq
from time import sleep

class Interposer_ctrl:
    def __init__(self, ip="192.168.23.60", port="7000"):
        context = zmq.Context()
        self.ip=ip
        self.port=port
        self.socket = context.socket( zmq.REQ )
        self.socket.connect("tcp://"+str(ip)+":"+str(port))
        self._options = ["reset", "resetROC", "resetROCI2C", "resyncLoad", "setAutoDelayMode", "printDelays", "setReadoutPassthroughTrue", "setReadoutPassthroughFalse", "resetLinks", "alignLinks", "interalignLinks", "activatePseudoECONd"]

    def __getattr__(self, name):
        if(name in self._options):
            self.socket.send_string(name)
            rep = self.socket.recv_string()
            print(rep)
        else:
            raise AttributeError("Object has no attribute \""+ name+"\"")


if __name__ == "__main__":
    itp = Interposer_ctrl("192.168.23.60", "7000")

    itp.reset
    itp.resetROC
    itp.resetROCI2C
    itp.resyncLoad
    sleep(0.0001)
    itp.setAutoDelayMode
    itp.printDelays
~
~
~
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --enable L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --disable L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --status
Firmware Version = 0x0012 ENABLED
 Command collision errors         :          0
 Orbit sync at BX 3560   DISABLED :          0
 Orbit count reset                :          0
 Link reset count                 :          1
 DAQ Sync count                   :          0
 Internal test count              :          0
 Calibration request     DISABLED :          0
   Prescale : 0            Request BX : 1000   L1A BX : 3540
 Level-1 Accept                   :     895845
   Periodic generator A  DISABLED   BX :     0  Orbit prescale : 0
   Periodic generator B  DISABLED   BX :     0  Orbit prescale : 0
   Random generator  DISABLED   Log2(Period) :     9   Average rate : 78125.0000 kHz
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ls
README.md       connections.xml  fast_control.py  gpio_control.py  iic.py               lpgbt_fecerror.py  test_result.py          zcu102_lpgbt.xml
__pycache__     daq_config.py    fmc_test.py      gpio_test.py     interposer_cfg.py    lpgbt_status.py    wagon_hdmi.xml          zcu102_wagon.xml
ber_lpgbt.py    efuse            gbt-sca-sw       ic_dump.py       io_lpgbt.py          setup_lpgbt.py     wagoneer_sca.py         zcu_multitool.py
check_lpgbt.py  efuse.py         gbtsca.xml       ic_test.py       lpgbt_eyeopening.py  test_engine.py     zcu102_fastcontrol.xml
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ pwd
/home/pastika/hgc-enginev1
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ls
README.md       connections.xml  fast_control.py  gpio_control.py  iic.py               lpgbt_fecerror.py  test_result.py          zcu102_lpgbt.xml
__pycache__     daq_config.py    fmc_test.py      gpio_test.py     interposer_cfg.py    lpgbt_status.py    wagon_hdmi.xml          zcu102_wagon.xml
ber_lpgbt.py    efuse            gbt-sca-sw       ic_dump.py       io_lpgbt.py          setup_lpgbt.py     wagoneer_sca.py         zcu_multitool.py
check_lpgbt.py  efuse.py         gbtsca.xml       ic_test.py       lpgbt_eyeopening.py  test_engine.py     zcu102_fastcontrol.xml
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ vim interposer_cfg.py
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ client_loop: send disconnect: Broken pipe
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] > lpc
Warning: Permanently added 'cmslpc-sl7.fnal.gov,131.225.204.176' (ECDSA) to the list of known hosts.
Last login: Wed Sep 29 15:58:03 2021 from 131.225.168.224
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

 SSH Logins: 1                             Load Avg: 0.0 0.01 0.05
------------------------------------------------------------------------------
  For information about computing at the LPC: http://lpc.fnal.gov/computing
------------------------------------------------------------------------------
Aidan, your .bash_profile has been completed.
[agrummer@cmslpc117 ~]$
[agrummer@cmslpc117 ~]$
[agrummer@cmslpc117 ~]$ pwd
/uscms/home/agrummer
[agrummer@cmslpc117 ~]$
[agrummer@cmslpc117 ~]$
[agrummer@cmslpc117 ~]$
[agrummer@cmslpc117 ~]$ hcalpro
Last login: Thu Nov 18 15:13:22 2021 from cmslpc114.fnal.gov
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ # pwd
/home/hcalpro
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ # pwd
/home/hcalpro
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ # ssh HGCAL_dev@192.168.1.47
HGCAL_dev@192.168.1.47's password:
Last login: Thu Nov 18 13:42:40 2021 from gateway
[HGCAL_dev@fnal-zcu102-a ~]$
[HGCAL_dev@fnal-zcu102-a ~]$
[HGCAL_dev@fnal-zcu102-a ~]$ pwd
/home/HGCAL_dev
[HGCAL_dev@fnal-zcu102-a ~]$ ls
agrummer  cookbook  fw  hexactrl  hgc-enginev1  jingyu  lib  link_capture  mkrohn  old  src  sw  test.txt  test2.txt
[HGCAL_dev@fnal-zcu102-a ~]$
[HGCAL_dev@fnal-zcu102-a ~]$
[HGCAL_dev@fnal-zcu102-a ~]$
[HGCAL_dev@fnal-zcu102-a ~]$
[HGCAL_dev@fnal-zcu102-a ~]$
[HGCAL_dev@fnal-zcu102-a ~]$ cd agrummer/HexaCookbook/
[HGCAL_dev@fnal-zcu102-a HexaCookbook]$ ls
coldstart.sh
[HGCAL_dev@fnal-zcu102-a HexaCookbook]$ . coldstart.sh
[sudo] password for HGCAL_dev:
mkdir: cannot create directory '/configfs': File exists
Time taken to load DTBO is 12525.000000 Milli Seconds
DTBO loaded through zynqMP FPGA manager successfully
loaded the firmware
/home/jmmans/src/
check that the path says: /home/jmmans/src/
Press any key to continue
 Back FW 0522  Front FW 0204   Backend Status = 00700008
 Errors =     0   Unlocks =    0
     100 MHz: 100.00000000 MHz
         Ref: 148.51370000 MHz
          TX: 0.00000000 MHz
        TX40: 0.00000000 MHz
         RX0: 282.40880000 MHz
         RX1: 282.40880000 MHz
         RX2: 282.40880000 MHz
      RX0-DV: 0.00000000 MHz
      RX1-DV: 0.00000000 MHz
      RX2-DV: 0.00000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes :
   EGROUP0: (0)
   EGROUP1: (0)
   EGROUP2: (0)
   EGROUP3: (0)
 Uplink modes :
   DAQ-EGROUP0: (0)
   DAQ-EGROUP1: (0)
   DAQ-EGROUP2: (0)
   DAQ-EGROUP3: (0)
   DAQ-EGROUP4: (0)
   DAQ-EGROUP5: (0)
   DAQ-EGROUP6: (0)
   TRIGB-EGROUP0: (0)
   TRIGC-EGROUP0: (0)
Reseting the link
 Status = 0x700008
 Back FW 0522  Front FW 0204   Backend Status = 0177711b
 Errors =     1   Unlocks =    0
     100 MHz: 100.00000000 MHz
         Ref: 320.64000000 MHz
          TX: 320.64000000 MHz
        TX40: 40.08000000 MHz
         RX0: 321.27560000 MHz
         RX1: 320.68950000 MHz
         RX2: 321.27150000 MHz
      RX0-DV: 0.00000000 MHz
      RX1-DV: 0.00000000 MHz
      RX2-DV: 0.00000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes :
   EGROUP0: (0)
   EGROUP1: (0)
   EGROUP2: (0)
   EGROUP3: (0)
 Uplink modes :
   DAQ-EGROUP0: (0)
   DAQ-EGROUP1: (0)
   DAQ-EGROUP2: (0)
   DAQ-EGROUP3: (0)
   DAQ-EGROUP4: (0)
   DAQ-EGROUP5: (0)
   DAQ-EGROUP6: (0)
   TRIGB-EGROUP0: (0)
   TRIGC-EGROUP0: (0)
does the clock say 320?
Press any key to continue
run ./agrummer/cookbook/lpgbtColdstart.sh on the raspberry pi, HGCAL_dev@192.168.1.94
Press any key to continue
running wagonoeer
Working with wagons with SCA S/N 29416 (0x72e8) and 29366 (0x72b6)
output should be: Working with wagons with SCA S/N 29416 (0x72e8) and 29366 (0x72b6)
Press any key to continue
 Back FW 0522  Front FW 0204   Backend Status = 1177711b
 Errors =    10   Unlocks =    0
     100 MHz: 100.00000000 MHz
         Ref: 320.64000000 MHz
          TX: 320.64000000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.64000000 MHz
         RX1: 320.64010000 MHz
         RX2: 321.27160000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 0.00000000 MHz
      RX2-DV: 0.00000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes :
   EGROUP0: (0)
   EGROUP1: (0)
   EGROUP2: (0)
   EGROUP3: (0)
 Uplink modes :
   DAQ-EGROUP0: (0)
   DAQ-EGROUP1: (0)
   DAQ-EGROUP2: (0)
   DAQ-EGROUP3: (0)
   DAQ-EGROUP4: (0)
   DAQ-EGROUP5: (0)
   DAQ-EGROUP6: (0)
   TRIGB-EGROUP0: (0)
   TRIGC-EGROUP0: (0)
************************************************
Does 'RX0-DV' say about 40 Mhz?  If so, congratulations, things are up!
done with zcu setup
now log in to the hexacontroller: HGCAL_dev@192.168.1.91 or 95
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ pwd
/home/pastika/hgc-enginev1
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ pwd
/home/pastika/hgc-enginev1
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ls
README.md       connections.xml  fast_control.py  gpio_control.py  iic.py               lpgbt_fecerror.py  test_result.py          zcu102_lpgbt.xml
__pycache__     daq_config.py    fmc_test.py      gpio_test.py     interposer_cfg.py    lpgbt_status.py    wagon_hdmi.xml          zcu102_wagon.xml
ber_lpgbt.py    efuse            gbt-sca-sw       ic_dump.py       io_lpgbt.py          setup_lpgbt.py     wagoneer_sca.py         zcu_multitool.py
check_lpgbt.py  efuse.py         gbtsca.xml       ic_test.py       lpgbt_eyeopening.py  test_engine.py     zcu102_fastcontrol.xml
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py -h
usage: fast_control.py [-h] [--status]
                       [--enable {orbit,calib,L1A_genA,L1A_genB,L1A_random}]
                       [--disable {orbit,calib,L1A_genA,L1A_genB,L1A_random}]
                       [--send {internaltest,linkreset,orbitcountreset,daqresync,L1A_genA,L1A_genB,calib}]
                       [--periodic {calib,L1A_genA,L1A_genB}]
                       [--prescale PRESCALE] [--bx BX] [--randoml1a RANDOML1A]

Encoder Fast Controls

optional arguments:
  -h, --help            show this help message and exit
  --status              Report the status of the encoder
  --enable {orbit,calib,L1A_genA,L1A_genB,L1A_random}
                        Enable one of the periodic generators
  --disable {orbit,calib,L1A_genA,L1A_genB,L1A_random}
                        Disable one of the periodic generators
  --send {internaltest,linkreset,orbitcountreset,daqresync,L1A_genA,L1A_genB,calib}
                        Send a single-shot command
  --periodic {calib,L1A_genA,L1A_genB}
                        Adjust settings for the given periodic generator
  --prescale PRESCALE   Set the orbit prescale for the given generator
  --bx BX               Set the BX for the specified signal
  --randoml1a RANDOML1A
                        Set the random L1A period (Log2(BX))
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --send L1A_genB
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ pwd
/home/pastika/hgc-enginev1
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ls
README.md       connections.xml  fast_control.py  gpio_control.py  iic.py               lpgbt_fecerror.py  test_result.py          zcu102_lpgbt.xml
__pycache__     daq_config.py    fmc_test.py      gpio_test.py     interposer_cfg.py    lpgbt_status.py    wagon_hdmi.xml          zcu102_wagon.xml
ber_lpgbt.py    efuse            gbt-sca-sw       ic_dump.py       io_lpgbt.py          setup_lpgbt.py     wagoneer_sca.py         zcu_multitool.py
check_lpgbt.py  efuse.py         gbtsca.xml       ic_test.py       lpgbt_eyeopening.py  test_engine.py     zcu102_fastcontrol.xml
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --send L1A_genB
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --send linkreset
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --periodic L1A_genB
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --enable L1A_genB
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --disable L1A_genB
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --status
Firmware Version = 0x0012 ENABLED
 Command collision errors         :          0
 Orbit sync at BX 3560   DISABLED :          0
 Orbit count reset                :          0
 Link reset count                 :          1
 DAQ Sync count                   :          0
 Internal test count              :          0
 Calibration request     DISABLED :          0
   Prescale : 0            Request BX : 1000   L1A BX : 3540
 Level-1 Accept                   :     292986
   Periodic generator A  DISABLED   BX :     0  Orbit prescale : 0
   Periodic generator B  DISABLED   BX :     0  Orbit prescale : 0
   Random generator  DISABLED   Log2(Period) :     9   Average rate : 78125.0000 kHz
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --enable L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --disable L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --enable L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --disable L1A_genA
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --send linkreset
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$ ./fast_control.py --send linkreset
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
[HGCAL_dev@fnal-zcu102-a hgc-enginev1]$
