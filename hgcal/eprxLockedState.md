
In the table Value one is when:
ROC subaddress 45, reg 0  = 0x0B
and value 2 is when:
ROC subaddress 45, reg 0  = 0xAB
for this roc reg ("TOP TABLE")
bit 5: In_inv_cmd_rx
bit 1: RunL
bit 0: RunR

expect data from ROCs on Trig elinks 3,4,5,6
and Data elinks 4,5

----------------------------------------------------------------------------------
| name        |   register     | DAQ val 1 | DAQ val 2 | TRIG val 1 | TRIG val 2 | 
----------------------------------------------------------------------------------
| EPRX0Locked |   0x152        |  0xe2     |   0xe2    |    0xe2    |    0xe2    |
| EPRX1Locked |   0x155        |  0xe2     |   0xe2    |    0xe2    |    0xe2    |
| EPRX2Locked |   0x158        |  0xe2     |   0xe2    |    0xe2    |    0xe2    |
| EPRX3Locked |   0x15b        |  0xe2     |   0xe2    |    0xe2    |    0xf2    |
| EPRX4Locked |   0x15e        |  0xe2     |   0xf2    |    0xe2    |    0xf2    |
| EPRX5Locked |   0x161        |  0xe2     |   0xf2    |    0xe2    |    0xf2    |
| EPRX6Locked |   0x164        |  0xf2     |   0xf2    |    0xe2    |    0xf2    |
----------------------------------------------------------------------------------




Files that were compared:
Saw ones and idles on TRIG links (3,4,5,6) only

ROC subaddress 45, reg 0  = 0x0B:
daq_2023Sep27_2023Sep28_captureOnesAndZeros.txt
ROC subaddress 45, reg 0  = 0xAB:
daq_2023Sep27_2023Sep28_captureIdles.txt  

ROC subaddress 45, reg 0  = 0x0B:
trig_2023Sep27_2023Sep28_captureOnesAndZeros.txt
ROC subaddress 45, reg 0  = 0xAB:
trig_2023Sep27_2023Sep28_captureIdles.txt

