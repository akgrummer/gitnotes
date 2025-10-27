Last login: Thu Nov 18 13:37:55 on ttys000
Sir, your .bashrc has been completed.
Thu Nov 18 13:37:57 CST 2021
Sir, your .bash_profile has been completed.

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
[dhcp-131-225-169-72:~] > lpc
Warning: Permanently added 'cmslpc-sl7.fnal.gov,131.225.204.176' (ECDSA) to the list of known hosts.
Last login: Thu Nov 18 13:40:48 2021 from 131.225.169.72
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

 SSH Logins: 3                             Load Avg: 0.07 0.04 0.05
------------------------------------------------------------------------------
  For information about computing at the LPC: http://lpc.fnal.gov/computing
------------------------------------------------------------------------------
Aidan, your .bash_profile has been completed.
[agrummer@cmslpc162 ~]$ hcalpro
Last login: Thu Nov 18 13:44:30 2021 from cmslpc162.fnal.gov
hcalpro@cmsnghcal01 ~ # ssh HGCAL_dev@192.168.1.94
HGCAL_dev@192.168.1.94's password:
Linux raspberrypi 5.4.83-v7+ #1379 SMP Mon Dec 14 13:08:57 GMT 2020 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Jul 12 20:19:51 2021 from 192.168.1.251
HGCAL_dev@raspberrypi:~ $
HGCAL_dev@raspberrypi:~ $ cd agrummer/cookbook/
HGCAL_dev@raspberrypi:~/agrummer/cookbook $ ls
lpgbtColdstart_old.sh  lpgbtColdstart.sh
HGCAL_dev@raspberrypi:~/agrummer/cookbook $ . lpgbtColdstart.sh
Setup core (Mode.V2_WAGON)
Setup clocks (V2_WAGON)
Setup core for trig lpgbt
Setup inputs (V2_WAGON)
Setup outputs (V2_WAGON)
Setup gpio
Reading daq lpgbt
chipid : 1795152080
000 : 6a
001 : ff
002 : d8
003 : d0
004 : 05
005 : 00
006 : 24
007 : 27
033 : 54
034 : 54
052 : 80
053 : 24
054 : 80
055 : 24
0ed : 00
0ee : f0
0ef : 06
140 : ba
142 : d2
145 : e2
158 : c0
159 : c0
15a : c0
15b : c0
15c : c0
15d : c0
15e : c0
1af : 00
1b4 : e3
1b5 : 0c
1b6 : 00
1b7 : 00
1c7 : 12
1c8 : 20
113 : 00
check if 1c7 says '12'
Press any key to continue
Run the link trick
Setup core (Mode.V2_WAGON)
Setup clocks (V2_WAGON)
Setup inputs (V2_WAGON)
Setup outputs (V2_WAGON)
Setup gpio
Run the link trick
Run the link trick
Setup core (Mode.V2_WAGON)
Setup clocks (V2_WAGON)
Setup inputs (V2_WAGON)
Setup outputs (V2_WAGON)
Setup gpio
HGCAL_dev@raspberrypi:~/agrummer/cookbook $ client_loop: send disconnect: Broken pipe
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] > clear
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] >
[dhcp-131-225-169-72:~] > lpc
Warning: Permanently added 'cmslpc-sl7.fnal.gov,131.225.204.176' (ECDSA) to the list of known hosts.
Last login: Fri Nov 19 11:33:04 2021 from 131.225.169.72
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

 SSH Logins: 2                             Load Avg: 0.08 0.03 0.05
------------------------------------------------------------------------------
  For information about computing at the LPC: http://lpc.fnal.gov/computing
------------------------------------------------------------------------------
Aidan, your .bash_profile has been completed.
[agrummer@cmslpc117 ~]$ hcalpro
Last login: Fri Nov 19 11:36:56 2021 from cmslpc117.fnal.gov
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ #
hcalpro@cmsnghcal01 ~ # ssh HGCAL_dev@192.168.1.94
HGCAL_dev@192.168.1.94's password:
Linux raspberrypi 5.4.83-v7+ #1379 SMP Mon Dec 14 13:08:57 GMT 2020 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Jul 12 20:19:20 2021 from 192.168.1.251
HGCAL_dev@raspberrypi:~ $
HGCAL_dev@raspberrypi:~ $ cd agrummer/cookbook/
HGCAL_dev@raspberrypi:~/agrummer/cookbook $ ls
lpgbtColdstart_old.sh  lpgbtColdstart.sh
HGCAL_dev@raspberrypi:~/agrummer/cookbook $ . lpgbtColdstart.sh
Setup core (Mode.V2_WAGON)
Setup clocks (V2_WAGON)
Setup core for trig lpgbt
Setup inputs (V2_WAGON)
Setup outputs (V2_WAGON)
Setup gpio
Reading daq lpgbt
chipid : 1795152080
000 : 6a
001 : ff
002 : d8
003 : d0
004 : 05
005 : 00
006 : 24
007 : 27
033 : 54
034 : 54
052 : 80
053 : 24
054 : 80
055 : 24
0ed : 00
0ee : f0
0ef : 06
140 : ba
142 : d2
145 : e2
158 : c0
159 : c0
15a : c0
15b : c0
15c : c0
15d : c0
15e : c0
1af : 00
1b4 : e3
1b5 : 0c
1b6 : 00
1b7 : 00
1c7 : 12
1c8 : 20
113 : 00
check if 1c7 says '12'
Press any key to continue
Run the link trick
Setup core (Mode.V2_WAGON)
Setup clocks (V2_WAGON)
Setup inputs (V2_WAGON)
Setup outputs (V2_WAGON)
Setup gpio
Run the link trick
Run the link trick
Setup core (Mode.V2_WAGON)
Setup clocks (V2_WAGON)
Setup inputs (V2_WAGON)
Setup outputs (V2_WAGON)
Setup gpio
HGCAL_dev@raspberrypi:~/agrummer/cookbook $
