# reconfig system:

```
[agrummer@zcufnal (hgc-engine-tools)]$ ./config_aidan2.sh 
going to load fw again, press any key to continue...
loading custom firmware
Time taken to load DTBO is 12502.000000 Milli Seconds
DTBO loaded through zynqMP FPGA manager successfully
Current polarity: 5
Current polarity: 7
 Back FW 0000  Backend Status = 0177711b
 Errors =     0   Unlocks =    0  RX Polarity = 3
     100 MHz: 100.00000000 MHz
         Ref: 320.64000000 MHz
          TX: 320.64000000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.01660000 MHz
         RX1: 321.27360000 MHz
         RX2: 321.27630000 MHz
      RX0-DV: 0.00000000 MHz
      RX1-DV: 0.00000000 MHz
      RX2-DV: 0.00000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes:
   EGROUP0: (0)          FastControl
   EGROUP1: (0)          FastControl
   EGROUP2: (0)          FastControl
   EGROUP3: (0)          FastControl
does polarity == 3?, press any key to continue...
Reseting the link
 Status = 0x777119
 Back FW 0000  Backend Status = 1177701b
 Errors =     0   Unlocks =    1  RX Polarity = 3
     100 MHz: 100.00000000 MHz
         Ref: 320.64000000 MHz
          TX: 320.64000000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.64000000 MHz
         RX1: 320.64000000 MHz
         RX2: 320.01780000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 0.00000000 MHz
      RX2-DV: 0.00000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes:
   EGROUP0: (0)          FastControl
   EGROUP1: (0)          FastControl
   EGROUP2: (0)          FastControl
   EGROUP3: (0)          FastControl
is the daq RX0-40 correct?, press any key to continue...
setup VTRX:  0
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
Run the link trick
DAQ
W
E
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
Run the link trick
DAQ
E
W
 Back FW 0000  Backend Status = 7176701b
 Errors =     4   Unlocks =    1  RX Polarity = 3
     100 MHz: 100.00000000 MHz
         Ref: 320.64000000 MHz
          TX: 320.64000000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.64000000 MHz
         RX1: 320.64000000 MHz
         RX2: 320.63990000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 40.08000000 MHz
      RX2-DV: 40.08000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes:
   EGROUP0: (0)          FastControl
   EGROUP1: (0)          FastControl
   EGROUP2: (0)          FastControl
   EGROUP3: (0)          FastControl
are all clocks good?, press any key to continue...
Reading E
chipid : 4063219867 (0xf22fd09b)
000 : 00
001 : 00
002 : 00
003 : 00
004 : 00
005 : 00
006 : 00
007 : 00
033 : 00
053 : ff
054 : ff
055 : 00
056 : 00
0f9 : 00
0fa : 00
0fb : 06
150 : 90
152 : f2
155 : e2
168 : c0
169 : c0
16a : c0
16b : c0
16c : c0
16d : c0
16e : c0
1c6 : 00
1c7 : 00
1c8 : 00
1c9 : 00
1d9 : 13
1da : 00
1db : 07
1dc : 00
1dd : 01
1de : 00
1df : 00
1e8 : 00
1e9 : 00
1ea : 00
1eb : 00
EAST is the dll status good? 0x1d9 to read 13, press any key to continue...
Reading W
chipid : 3217183859 (0xbfc25473)
000 : 00
001 : 00
002 : 00
003 : 00
004 : 00
005 : 00
006 : 00
007 : 00
033 : 00
053 : ff
054 : ff
055 : 00
056 : 00
0f9 : 00
0fa : 00
0fb : 06
150 : 90
152 : f2
155 : f2
168 : c0
169 : c0
16a : c0
16b : c0
16c : c0
16d : c0
16e : c0
1c6 : 04
1c7 : 00
1c8 : 00
1c9 : 00
1d9 : 13
1da : 00
1db : 07
1dc : 00
1dd : 01
1de : 00
1df : 00
1e8 : 00
1e9 : 00
1ea : 00
1eb : 00
WEST is the dll status good? 0x1d9 to read 13, press any key to continue...
changing directories "cd ~/hgc-engine-tools" to go back, press any key to continue...
IC_SOURCE: 0
EC_SOURCE: 0
lpGBT Status
Reading daq lpgbt
chipid : 1794824059 (0x6afad77b)
000 : 00
001 : 00
002 : 00
003 : 00
004 : 00
005 : 00
006 : 00
007 : 00
033 : 00
053 : c0
054 : 00
055 : c0
056 : 00
0f9 : 00
0fa : 00
0fb : 06
150 : b2
152 : e2
155 : f2
168 : c0
169 : c0
16a : c0
16b : c0
16c : c0
16d : c0
16e : c0
1c6 : 00
1c7 : 00
1c8 : 00
1c9 : 00
1d9 : 13
1da : 05
1db : 00
1dc : 00
1dd : 01
1de : 05
1df : 00
1e8 : 05
1e9 : 00
1ea : 00
1eb : 15
Starting Reset Line Status
'EAST.PWR_EN0' => False
'EAST.HGCROC_RE_Hb0' => False
'EAST.HGCROC_RE_Sb0' => False
'EAST.PG_LDO0' => False
Come out of reset
Reset ROC
WEST Starting Reset Line Status
'WEST.PWR_EN0' => False
'WEST.HGCROC_RE_Hb0' => False
'WEST.HGCROC_RE_Sb0' => False
'WEST.PG_LDO0' => False
WEST Come out of reset
Reset ROC
EAST: Reset Line Status
'EAST.PWR_EN0' => True
'EAST.HGCROC_RE_Hb0' => True
'EAST.HGCROC_RE_Sb0' => True
'EAST.PG_LDO0' => True
'WREADY' => True
'EREADY' => True
WEST: Reset Line Status
'WEST.PWR_EN0' => True
'WEST.HGCROC_RE_Hb0' => True
'WEST.HGCROC_RE_Sb0' => True
'WEST.PG_LDO0' => True
'WREADY' => True
'EREADY' => True
 Back FW 0000  Backend Status = 7177711b
 Errors =     4   Unlocks =    1
     100 MHz: 100.00000000 MHz
         Ref: 320.64000000 MHz
          TX: 320.64000000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.64000000 MHz
         RX1: 320.64000000 MHz
         RX2: 320.64000000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 40.08000000 MHz
      RX2-DV: 40.08000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes :
   EGROUP0: (0)
   EGROUP1: (0)
   EGROUP2: (0)
   EGROUP3: (0)
Did ROC gpio cycle work? Moving to SWAMP lpbgt and ROC config next...
IC_SOURCE: 1
EC_SOURCE: 1
Namespace(lpgbt_target='daq', read_write='write', config='/home/agrummer/daq/slow_control/configs/setup_inputs_daq_lpgbt.yaml', reg=None, val=None, protocol='sct', ic_emp_channel=13)
['TOP']
configuring lpgbt
INFO     : 2023-11-27 23:24:37,006 : (lpgbt       ) :  in sc_lpgbt.configuration
INFO     : 2023-11-27 23:24:37,010 : (lpgbt       ) :  sc_lpgbt.configuration done
INFO     : 2023-11-27 23:24:37,010 : (lpgbt       ) :  read with config = {'EPRX00CHNCNTR': 2, 'EPRX01CHNCNTR': 2, 'EPRX02CHNCNTR': 2, 'EPRX03CHNCNTR': 2, 'EPRX0CONTROL': 30, 'EPRX10CHNCNTR': 10, 'EPRX11CHNCNTR': 10, 'EPRX12CHNCNTR': 10, 'EPRX13CHNCNTR': 10, 'EPRX1CONTROL': 30, 'EPRX20CHNCNTR': 10, 'EPRX21CHNCNTR': 10, 'EPRX22CHNCNTR': 10, 'EPRX23CHNCNTR': 10, 'EPRX2CONTROL': 30, 'EPRX30CHNCNTR': 2, 'EPRX31CHNCNTR': 2, 'EPRX32CHNCNTR': 2, 'EPRX33CHNCNTR': 2, 'EPRX3CONTROL': 30, 'EPRX40CHNCNTR': 10, 'EPRX41CHNCNTR': 10, 'EPRX42CHNCNTR': 10, 'EPRX43CHNCNTR': 10, 'EPRX4CONTROL': 30, 'EPRX50CHNCNTR': 10, 'EPRX51CHNCNTR': 10, 'EPRX52CHNCNTR': 10, 'EPRX53CHNCNTR': 10, 'EPRX5CONTROL': 30, 'EPRX60CHNCNTR': 2, 'EPRX61CHNCNTR': 2, 'EPRX62CHNCNTR': 2, 'EPRX63CHNCNTR': 2, 'EPRX6CONTROL': 30}
INFO     : 2023-11-27 23:24:37,041 : (lpgbt       ) :  sc_lpgbt.read done
{'EPRX0CONTROL': 30, 'EPRX1CONTROL': 30, 'EPRX2CONTROL': 30, 'EPRX3CONTROL': 30, 'EPRX4CONTROL': 30, 'EPRX5CONTROL': 30, 'EPRX6CONTROL': 30, 'EPRX00CHNCNTR': 2, 'EPRX01CHNCNTR': 2, 'EPRX02CHNCNTR': 2, 'EPRX03CHNCNTR': 2, 'EPRX10CHNCNTR': 10, 'EPRX11CHNCNTR': 10, 'EPRX12CHNCNTR': 10, 'EPRX13CHNCNTR': 10, 'EPRX20CHNCNTR': 10, 'EPRX21CHNCNTR': 10, 'EPRX22CHNCNTR': 10, 'EPRX23CHNCNTR': 10, 'EPRX30CHNCNTR': 2, 'EPRX31CHNCNTR': 2, 'EPRX32CHNCNTR': 2, 'EPRX33CHNCNTR': 2, 'EPRX40CHNCNTR': 10, 'EPRX41CHNCNTR': 10, 'EPRX42CHNCNTR': 10, 'EPRX43CHNCNTR': 10, 'EPRX50CHNCNTR': 10, 'EPRX51CHNCNTR': 10, 'EPRX52CHNCNTR': 10, 'EPRX53CHNCNTR': 10, 'EPRX60CHNCNTR': 2, 'EPRX61CHNCNTR': 2, 'EPRX62CHNCNTR': 2, 'EPRX63CHNCNTR': 2}
Namespace(lpgbt_target='trg_e', read_write='write', config='/home/agrummer/daq/slow_control/configs/setup_inputs_trg_lpgbt_east.yaml', reg=None, val=None, protocol='sct', ic_emp_channel=13)
['TOP']
configuring lpgbt
INFO     : 2023-11-27 23:24:42,368 : (lpgbt       ) :  in sc_lpgbt.configuration
INFO     : 2023-11-27 23:24:42,372 : (lpgbt       ) :  sc_lpgbt.configuration done
INFO     : 2023-11-27 23:24:42,372 : (lpgbt       ) :  read with config = {'EPRX00CHNCNTR': 2, 'EPRX01CHNCNTR': 2, 'EPRX02CHNCNTR': 2, 'EPRX03CHNCNTR': 2, 'EPRX0CONTROL': 30, 'EPRX10CHNCNTR': 2, 'EPRX11CHNCNTR': 2, 'EPRX12CHNCNTR': 2, 'EPRX13CHNCNTR': 2, 'EPRX1CONTROL': 30, 'EPRX20CHNCNTR': 2, 'EPRX21CHNCNTR': 2, 'EPRX22CHNCNTR': 2, 'EPRX23CHNCNTR': 2, 'EPRX2CONTROL': 30, 'EPRX30CHNCNTR': 10, 'EPRX31CHNCNTR': 10, 'EPRX32CHNCNTR': 10, 'EPRX33CHNCNTR': 10, 'EPRX3CONTROL': 30, 'EPRX40CHNCNTR': 2, 'EPRX41CHNCNTR': 2, 'EPRX42CHNCNTR': 2, 'EPRX43CHNCNTR': 2, 'EPRX4CONTROL': 30, 'EPRX50CHNCNTR': 10, 'EPRX51CHNCNTR': 10, 'EPRX52CHNCNTR': 10, 'EPRX53CHNCNTR': 10, 'EPRX5CONTROL': 30, 'EPRX60CHNCNTR': 2, 'EPRX61CHNCNTR': 2, 'EPRX62CHNCNTR': 2, 'EPRX63CHNCNTR': 2, 'EPRX6CONTROL': 30}
INFO     : 2023-11-27 23:24:42,403 : (lpgbt       ) :  sc_lpgbt.read done
{'EPRX0CONTROL': 30, 'EPRX1CONTROL': 30, 'EPRX2CONTROL': 30, 'EPRX3CONTROL': 30, 'EPRX4CONTROL': 30, 'EPRX5CONTROL': 30, 'EPRX6CONTROL': 30, 'EPRX00CHNCNTR': 2, 'EPRX01CHNCNTR': 2, 'EPRX02CHNCNTR': 2, 'EPRX03CHNCNTR': 2, 'EPRX10CHNCNTR': 2, 'EPRX11CHNCNTR': 2, 'EPRX12CHNCNTR': 2, 'EPRX13CHNCNTR': 2, 'EPRX20CHNCNTR': 2, 'EPRX21CHNCNTR': 2, 'EPRX22CHNCNTR': 2, 'EPRX23CHNCNTR': 2, 'EPRX30CHNCNTR': 10, 'EPRX31CHNCNTR': 10, 'EPRX32CHNCNTR': 10, 'EPRX33CHNCNTR': 10, 'EPRX40CHNCNTR': 2, 'EPRX41CHNCNTR': 2, 'EPRX42CHNCNTR': 2, 'EPRX43CHNCNTR': 2, 'EPRX50CHNCNTR': 10, 'EPRX51CHNCNTR': 10, 'EPRX52CHNCNTR': 10, 'EPRX53CHNCNTR': 10, 'EPRX60CHNCNTR': 2, 'EPRX61CHNCNTR': 2, 'EPRX62CHNCNTR': 2, 'EPRX63CHNCNTR': 2}
Namespace(lpgbt_target='trg_w', read_write='write', config='/home/agrummer/daq/slow_control/configs/setup_inputs_trg_lpgbt_west.yaml', reg=None, val=None, protocol='sct', ic_emp_channel=13)
['TOP']
configuring lpgbt
INFO     : 2023-11-27 23:24:47,705 : (lpgbt       ) :  in sc_lpgbt.configuration
INFO     : 2023-11-27 23:24:47,709 : (lpgbt       ) :  sc_lpgbt.configuration done
INFO     : 2023-11-27 23:24:47,709 : (lpgbt       ) :  read with config = {'EPRX00CHNCNTR': 2, 'EPRX01CHNCNTR': 2, 'EPRX02CHNCNTR': 2, 'EPRX03CHNCNTR': 2, 'EPRX0CONTROL': 30, 'EPRX10CHNCNTR': 10, 'EPRX11CHNCNTR': 2, 'EPRX12CHNCNTR': 2, 'EPRX13CHNCNTR': 2, 'EPRX1CONTROL': 30, 'EPRX20CHNCNTR': 2, 'EPRX21CHNCNTR': 2, 'EPRX22CHNCNTR': 2, 'EPRX23CHNCNTR': 2, 'EPRX2CONTROL': 30, 'EPRX30CHNCNTR': 10, 'EPRX31CHNCNTR': 2, 'EPRX32CHNCNTR': 2, 'EPRX33CHNCNTR': 2, 'EPRX3CONTROL': 30, 'EPRX40CHNCNTR': 2, 'EPRX41CHNCNTR': 2, 'EPRX42CHNCNTR': 2, 'EPRX43CHNCNTR': 2, 'EPRX4CONTROL': 30, 'EPRX50CHNCNTR': 2, 'EPRX51CHNCNTR': 2, 'EPRX52CHNCNTR': 2, 'EPRX53CHNCNTR': 2, 'EPRX5CONTROL': 30, 'EPRX60CHNCNTR': 2, 'EPRX61CHNCNTR': 2, 'EPRX62CHNCNTR': 2, 'EPRX63CHNCNTR': 2, 'EPRX6CONTROL': 30}
INFO     : 2023-11-27 23:24:47,739 : (lpgbt       ) :  sc_lpgbt.read done
{'EPRX0CONTROL': 30, 'EPRX1CONTROL': 30, 'EPRX2CONTROL': 30, 'EPRX3CONTROL': 30, 'EPRX4CONTROL': 30, 'EPRX5CONTROL': 30, 'EPRX6CONTROL': 30, 'EPRX00CHNCNTR': 2, 'EPRX01CHNCNTR': 2, 'EPRX02CHNCNTR': 2, 'EPRX03CHNCNTR': 2, 'EPRX10CHNCNTR': 10, 'EPRX11CHNCNTR': 2, 'EPRX12CHNCNTR': 2, 'EPRX13CHNCNTR': 2, 'EPRX20CHNCNTR': 2, 'EPRX21CHNCNTR': 2, 'EPRX22CHNCNTR': 2, 'EPRX23CHNCNTR': 2, 'EPRX30CHNCNTR': 10, 'EPRX31CHNCNTR': 2, 'EPRX32CHNCNTR': 2, 'EPRX33CHNCNTR': 2, 'EPRX40CHNCNTR': 2, 'EPRX41CHNCNTR': 2, 'EPRX42CHNCNTR': 2, 'EPRX43CHNCNTR': 2, 'EPRX50CHNCNTR': 2, 'EPRX51CHNCNTR': 2, 'EPRX52CHNCNTR': 2, 'EPRX53CHNCNTR': 2, 'EPRX60CHNCNTR': 2, 'EPRX61CHNCNTR': 2, 'EPRX62CHNCNTR': 2, 'EPRX63CHNCNTR': 2}
configuring rocs: e0
for module e0, roc: 0x08
Namespace(site='e0', roc_addr='0x08', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0809 seconds
INFO     : 2023-11-27 23:24:55,941 : (roc         ) :  roc Configured
for module e0, roc: 0x18
Namespace(site='e0', roc_addr='0x18', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0730 seconds
INFO     : 2023-11-27 23:25:04,118 : (roc         ) :  roc Configured
for module e0, roc: 0x28
Namespace(site='e0', roc_addr='0x28', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0737 seconds
INFO     : 2023-11-27 23:25:12,320 : (roc         ) :  roc Configured
configuring rocs: w0
for module w0, roc: 0x08
Namespace(site='w0', roc_addr='0x08', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0734 seconds
INFO     : 2023-11-27 23:25:20,512 : (roc         ) :  roc Configured
for module w0, roc: 0x18
Namespace(site='w0', roc_addr='0x18', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0734 seconds
INFO     : 2023-11-27 23:25:28,712 : (roc         ) :  roc Configured
for module w0, roc: 0x28
Namespace(site='w0', roc_addr='0x28', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0724 seconds
INFO     : 2023-11-27 23:25:36,895 : (roc         ) :  roc Configured
CONFIGURING SIDE SPECIFIC
for roc: 0x08
Namespace(site='e0', roc_addr='0x08', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal_east.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0731 seconds
INFO     : 2023-11-27 23:25:42,345 : (roc         ) :  roc Configured
Namespace(site='w0', roc_addr='0x08', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal_west.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0724 seconds
INFO     : 2023-11-27 23:25:47,808 : (roc         ) :  roc Configured
for roc: 0x18
Namespace(site='e0', roc_addr='0x18', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal_east.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0730 seconds
INFO     : 2023-11-27 23:25:53,259 : (roc         ) :  roc Configured
Namespace(site='w0', roc_addr='0x18', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal_west.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0737 seconds
INFO     : 2023-11-27 23:25:58,718 : (roc         ) :  roc Configured
for roc: 0x28
Namespace(site='e0', roc_addr='0x28', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal_east.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0737 seconds
INFO     : 2023-11-27 23:26:04,162 : (roc         ) :  roc Configured
Namespace(site='w0', roc_addr='0x28', read_write='write', config='/home/agrummer/daq/slow_control/configs/init_roc_fnal_west.yaml', oconfig=None, param_name=None, val=0, protocol='sct', ic_emp_channel=13)
['TOP']
will use bus 0 of lpgbt lpgbt
Elapsed time: 0.0729 seconds
INFO     : 2023-11-27 23:26:09,609 : (roc         ) :  roc Configured
Did SWAMP config work? moving to LC config next...
IC_SOURCE: 0
EC_SOURCE: 0
CTL.INVERT_RX_DATA_ORDER: 0
```
