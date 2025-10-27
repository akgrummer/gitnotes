readback from CERN_PC - errors still here
lpgbt_control -F /root/agrummer/config_generator/hwcfg_fnal_cernvcu.yaml -L 3 -l daq -f  /root/agrummer/config_generator/serenityU_DB/C_00_00_ELE_0016/init_C_00_00_ELE_0016-daq.yaml -r 0 -c 1
2025-05-22 18:37:34.991 [info] read back configuration =
DPDATAPATTERN3: 170
DPDATAPATTERN2: 170
DPDATAPATTERN1: 170
DPDATAPATTERN0: 170
ULDATASOURCE0: 0
ULDATASOURCE1: 0
ULDATASOURCE2: 0
ULDATASOURCE3: 0
ULDATASOURCE4: 0
POWERUP0: 0
POWERUP1: 0
POWERUP2: 0
EPRXECCHNCNTR: 1
EPRX60CHNCNTR: 10
EPRX50CHNCNTR: 10
EPRX40CHNCNTR: 10
EPRX30CHNCNTR: 10
EPRX20CHNCNTR: 10
EPRX10CHNCNTR: 10
EPRX0CONTROL: 29
EPRX1CONTROL: 29
EPRX2CONTROL: 29
EPRX3CONTROL: 29
EPRX4CONTROL: 29
EPRX5CONTROL: 29
EPRX6CONTROL: 29
EPRXECCONTROL: 16
EPRX00CHNCNTR: 10
EPTX00CHNCNTR: 7
EPTX01CHNCNTR: 7
EPTX02CHNCNTR: 0
EPTX03CHNCNTR: 0
EPTX10CHNCNTR: 7
EPTX11CHNCNTR: 0
EPTX12CHNCNTR: 0
EPTX13CHNCNTR: 0
EPTX20CHNCNTR: 7
EPTX21CHNCNTR: 7
EPTX22CHNCNTR: 0
EPTX23CHNCNTR: 0
EPTX30CHNCNTR: 7
EPTX31CHNCNTR: 7
EPTX32CHNCNTR: 0
EPTX33CHNCNTR: 0
EPTX01_00CHNCNTR: 0
EPTX03_02CHNCNTR: 0
EPTX11_10CHNCNTR: 0
EPTX13_12CHNCNTR: 0
EPTX21_20CHNCNTR: 7
EPTX23_22CHNCNTR: 7
EPTX31_30CHNCNTR: 0
EPTX33_32CHNCNTR: 0
EPCLK27CHNCNTRH: 25
EPCLK27CHNCNTRL: 0
EPCLK28CHNCNTRH: 44
EPCLK28CHNCNTRL: 0
EPTXDATARATE: 255
EPTXCONTROL: 13
EPTX10ENABLE: 19
EPTX32ENABLE: 51
EPTXECCHNCNTR: 225
EPCLK25CHNCNTRH: 44
EPCLK25CHNCNTRL: 0
EPCLK21CHNCNTRH: 44
EPCLK21CHNCNTRL: 0
EPCLK22CHNCNTRH: 44
EPCLK22CHNCNTRL: 0
EPCLK19CHNCNTRH: 44
EPCLK19CHNCNTRL: 0
EPCLK6CHNCNTRH: 44
EPCLK6CHNCNTRL: 0
EPCLK4CHNCNTRH: 44
EPCLK4CHNCNTRL: 0
EPCLK1CHNCNTRH: 25
EPCLK1CHNCNTRL: 0
CHIPCONFIG: 0
EQCONFIG: 24
EQRES: 0
LDCONFIGH: 96
LDCONFIGL: 0
PSDLLCONFIG: 0
CLKGCONFIG0: 232
CLKGCONFIG1: 56
CLKGPLLRES: 34
CLKGPLLINTCUR: 153
CLKGPLLPROPCUR: 153
CLKGCDRPROPCUR: 85
CLKGCDRINTCUR: 85
CLKGCDRFFPROPCUR: 102
CLKGFLLINTCUR: 85
CLKGFFCAP: 27
CLKGCNTOVERRIDE: 0
CLKGOVERRIDECAPBANK: 0
CLKGWAITTIME: 136
CLKGLFCONFIG0: 143
CLKGLFCONFIG1: 255
FAMAXHEADERFOUNDCOUNT: 255
FAMAXHEADERFOUNDCOUNTAFTERNF: 255
FAMAXHEADERNOTFOUNDCOUNT: 255
2025-05-22 18:37:34.992 [info] ********Config Differences**************
2025-05-22 18:37:34.992 [info] Register                            | Expected     | Read Back
2025-05-22 18:37:34.992 [info] -----                               | -----        | -----
2025-05-22 18:37:34.992 [info] EPTX21_20CHNCNTR                    | 0x0          | 0x7
2025-05-22 18:37:34.992 [info] EPTX23_22CHNCNTR                    | 0x0          | 0x7
2025-05-22 18:37:34.992 [info] FAMAXHEADERFOUNDCOUNT               | 0x10         | 0xFF
2025-05-22 18:37:34.992 [info] FAMAXHEADERFOUNDCOUNTAFTERNF        | 0x10         | 0xFF
2025-05-22 18:37:34.992 [info] FAMAXHEADERNOTFOUNDCOUNT            | 0x10         | 0xFF
2025-05-22 18:37:34.992 [error] expected and read back configuration DON'T match
[2025-05-22 18:37:34.992] [error] expected and read back configuration DON'T match





- performed both writes before reading (note, secon write should be redundant)
```
/root/rshukla/lpgbt_test/bin/ic_write /root/HgcalFirmware/connections.xml F 84 0x70 0xae 0x7:0x7:0x0:0x0:0x7:0x0:0x0:0x0:0x7:0x7:0x0:0x0:0x7:0x7:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0:0x0

/root/rshukla/lpgbt_test/bin/ic_write /root/HgcalFirmware/connections.xml F 84 0x70 0xc2 0x0:0x0

/root/rshukla/lpgbt_test/bin/ic_read /root/HgcalFirmware/connections.xml F 84 0x70 0xc2 2
GBTx addr : 0x70
 | addr  : 0x0c2 | value : 0x8020c200 |
 | addr  : 0x0c3 | value : 0x8020c300 |

/root/rshukla/lpgbt_test/bin/ic_read /root/HgcalFirmware/connections.xml F 84 0x70 0xae 24
GBTx addr : 0x70
 | addr  : 0x0ae | value : 0x8180ae07 |
 | addr  : 0x0af | value : 0x8180af07 |
 | addr  : 0x0b0 | value : 0x8180b000 |
 | addr  : 0x0b1 | value : 0x8180b100 |
 | addr  : 0x0b2 | value : 0x8180b207 |
 | addr  : 0x0b3 | value : 0x8180b300 |
 | addr  : 0x0b4 | value : 0x8180b400 |
 | addr  : 0x0b5 | value : 0x8180b500 |
 | addr  : 0x0b6 | value : 0x8180b607 |
 | addr  : 0x0b7 | value : 0x8180b707 |
 | addr  : 0x0b8 | value : 0x8180b800 |
 | addr  : 0x0b9 | value : 0x8180b900 |
 | addr  : 0x0ba | value : 0x8180ba07 |
 | addr  : 0x0bb | value : 0x8180bb07 |
 | addr  : 0x0bc | value : 0x8180bc00 |
 | addr  : 0x0bd | value : 0x8180bd00 |
 | addr  : 0x0be | value : 0x8180be00 |
 | addr  : 0x0bf | value : 0x8180bf00 |
 | addr  : 0x0c0 | value : 0x8180c000 |
 | addr  : 0x0c1 | value : 0x8180c100 |
 | addr  : 0x0c2 | value : 0x8180c207 |
 | addr  : 0x0c3 | value : 0x8180c307 |
 | addr  : 0x0c4 | value : 0x8180c400 |
 | addr  : 0x0c5 | value : 0x8180c500 |
```



2025-05-23 15:32:08.567 [info] ********Config Differences**************
2025-05-23 15:32:08.567 [info] Register                            | Expected     | Read Back
2025-05-23 15:32:08.567 [info] -----                               | -----        | -----
2025-05-23 15:32:08.567 [info] FAMAXHEADERFOUNDCOUNT               | 0x10         | 0xFF
2025-05-23 15:32:08.567 [error] expected and read back configuration DON'T match
[2025-05-23 15:32:08.567] [error] expected and read back configuration DON'T match

2025-05-23 15:42:04.740 [info] ********Config Differences**************
2025-05-23 15:42:04.740 [info] Register                            | Expected     | Read Back
2025-05-23 15:42:04.740 [info] -----                               | -----        | -----
2025-05-23 15:42:04.740 [info] DPDATAPATTERN3                      | 0x0          | 0x12
2025-05-23 15:42:04.740 [info] DPDATAPATTERN2                      | 0x0          | 0x34
2025-05-23 15:42:04.740 [info] DPDATAPATTERN1                      | 0x0          | 0x56
2025-05-23 15:42:04.740 [info] DPDATAPATTERN0                      | 0x0          | 0x78
2025-05-23 15:42:04.740 [info] PIOOUTH                             | 0x0          | 0xC0
2025-05-23 15:42:04.740 [info] FAMAXHEADERFOUNDCOUNT               | 0x10         | 0xFF
2025-05-23 15:42:04.740 [info] VREFTUNE                            | 0x0          | 0x80


