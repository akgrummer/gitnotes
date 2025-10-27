# Post cold test 1 at room temp

- initial config seemed to work
- lpgbt communication successful
- 2 weeks after initial failure
- temperature: nominal room temp

# Config output:

```
[agrummer@zcufnal (hgc-engine-tools)]$ ./config_aidan2.sh 
going to load fw again, press any key to continue...
loading custom firmware
Time taken to load DTBO is 12500.000000 Milli Seconds
DTBO loaded through zynqMP FPGA manager successfully
Current polarity: 5
Current polarity: 7
 Back FW 0000  Backend Status = 2175701b
 Errors =     0   Unlocks =    0  RX Polarity = 3
     100 MHz: 100.00000000 MHz
         Ref: 320.64020000 MHz
          TX: 320.64020000 MHz
        TX40: 40.08000000 MHz
         RX0: 321.27460000 MHz
         RX1: 319.94200000 MHz
         RX2: 320.64010000 MHz
      RX0-DV: 0.00000000 MHz
      RX1-DV: 40.08000000 MHz
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
 Back FW 0000  Backend Status = 3175701b
 Errors =     0   Unlocks =    1  RX Polarity = 3
     100 MHz: 100.00000000 MHz
         Ref: 320.64010000 MHz
          TX: 320.64010000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.64000000 MHz
         RX1: 319.94200000 MHz
         RX2: 320.64010000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 40.08000000 MHz
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
setup VTRX:  1
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
 Back FW 0000  Backend Status = 7176711b
 Errors =     4   Unlocks =    1  RX Polarity = 3
     100 MHz: 100.00000000 MHz
         Ref: 320.64010000 MHz
          TX: 320.64010000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.64010000 MHz
         RX1: 320.64010000 MHz
         RX2: 320.64000000 MHz
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
chipid : 3400716787 (0xcab2d1f3)
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
152 : e2
155 : e2
168 : c0
169 : c0
16a : c0
16b : c0
16c : c0
16d : c0
16e : c0
1c6 : 40
1c7 : 20
1c8 : 00
1c9 : 80
1d9 : 13
1da : 00
1db : 07
1dc : 00
1dd : 00
1de : 00
1df : 00
1e8 : 00
1e9 : 00
1ea : 00
1eb : 00
EAST is the dll status good? 0x1d9 to read 13, press any key to continue...
Reading W
chipid : 88199731 (0x0541d233)
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
1c6 : 20
1c7 : 20
1c8 : 00
1c9 : 02
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
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
Run the link trick
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
Run the link trick
Setup core (Mode.V3_ALL)
Setup clocks (V3_ALL)
Setup core for trig lpgbt
Setup inputs (V3_ALL)
Setup outputs (V3_ALL)
Setup gpio
 Back FW 0000  Backend Status = 7176701b
 Errors =     8   Unlocks =    1
     100 MHz: 100.00000000 MHz
         Ref: 320.64010000 MHz
          TX: 320.64010000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.64010000 MHz
         RX1: 320.64010000 MHz
         RX2: 320.64010000 MHz
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
lpGBT Status
Reading daq lpgbt
chipid : 2118439643 (0x7e44d2db)
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
152 : f2
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
1da : 00
1db : 00
1dc : 00
1dd : 01
1de : 00
1df : 00
1e8 : 05
1e9 : 00
1ea : 00
1eb : 03
Starting Reset Line Status
'EAST.PWR_EN0' => False
'EAST.HGCROC_RE_Hb0' => False
'EAST.HGCROC_RE_Sb0' => False
'EAST.PG_LDO0' => False
Come out of reset
Reset ROC
Reset Line Status
'EAST.PWR_EN0' => True
'EAST.HGCROC_RE_Hb0' => True
'EAST.HGCROC_RE_Sb0' => True
'EAST.PG_LDO0' => True
'WREADY' => True
'EREADY' => True
Setup HGCROC
 Back FW 0000  Backend Status = 7175711b
 Errors =     8   Unlocks =    1
     100 MHz: 100.00000000 MHz
         Ref: 320.64010000 MHz
          TX: 320.64010000 MHz
        TX40: 40.08000000 MHz
         RX0: 320.64010000 MHz
         RX1: 320.64010000 MHz
         RX2: 320.64000000 MHz
      RX0-DV: 40.08000000 MHz
      RX1-DV: 40.08010000 MHz
      RX2-DV: 40.08000000 MHz
        ERR0: 0
        ERR1: 0
        ERR2: 0
 Downlink modes :
   EGROUP0: (0)
   EGROUP1: (0)
   EGROUP2: (0)
   EGROUP3: (0)
POWERUP2 0x0 0x00fb 0x6 0x0
EPRX00CHNCNTR 0x2 0x00d0 0x2 0x2
EPRX01CHNCNTR 0x2 0x00d1 0x2 0x2
EPRX02CHNCNTR 0x2 0x00d2 0x2 0x2
EPRX03CHNCNTR 0x2 0x00d3 0x2 0x2
EPRX0CONTROL 0x1e 0x00c8 0x1e 0x1e
EPRX10CHNCNTR 0x2 0x00d4 0x2 0x2
EPRX11CHNCNTR 0x2 0x00d5 0x2 0x2
EPRX12CHNCNTR 0x2 0x00d6 0x2 0x2
EPRX13CHNCNTR 0x2 0x00d7 0x2 0x2
EPRX1CONTROL 0x1e 0x00c9 0x1e 0x1e
EPRX20CHNCNTR 0x2 0x00d8 0x2 0x2
EPRX21CHNCNTR 0x2 0x00d9 0x2 0x2
EPRX22CHNCNTR 0x2 0x00da 0x2 0x2
EPRX23CHNCNTR 0x2 0x00db 0x2 0x2
EPRX2CONTROL 0x1e 0x00ca 0x1e 0x1e
EPRX30CHNCNTR 0xa 0x00dc 0x2 0xa
EPRX31CHNCNTR 0xa 0x00dd 0x2 0xa
EPRX32CHNCNTR 0xa 0x00de 0x2 0xa
EPRX33CHNCNTR 0xa 0x00df 0x2 0xa
EPRX3CONTROL 0x1e 0x00cb 0x1e 0x1e
EPRX40CHNCNTR 0x2 0x00e0 0x2 0x2
EPRX41CHNCNTR 0x2 0x00e1 0x2 0x2
EPRX42CHNCNTR 0x2 0x00e2 0x2 0x2
EPRX43CHNCNTR 0x2 0x00e3 0x2 0x2
EPRX4CONTROL 0x1e 0x00cc 0x1e 0x1e
EPRX50CHNCNTR 0xa 0x00e4 0x2 0xa
EPRX51CHNCNTR 0xa 0x00e5 0x2 0xa
EPRX52CHNCNTR 0xa 0x00e6 0x2 0xa
EPRX53CHNCNTR 0xa 0x00e7 0x2 0xa
EPRX5CONTROL 0x1e 0x00cd 0x1e 0x1e
EPRX60CHNCNTR 0x2 0x00e8 0x2 0x2
EPRX61CHNCNTR 0x2 0x00e9 0x2 0x2
EPRX62CHNCNTR 0x2 0x00ea 0x2 0x2
EPRX63CHNCNTR 0x2 0x00eb 0x2 0x2
EPRX6CONTROL 0x1e 0x00ce 0x1e 0x1e
here 1
POWERUP2 0x6 0x00fb 0x0 0x6
here 2
EAST roc 5,  0 : 171
EAST roc 1,  0 : 171
EAST roc 3,  0 : 171
CTL.INVERT_RX_DATA_ORDER: 0
```

