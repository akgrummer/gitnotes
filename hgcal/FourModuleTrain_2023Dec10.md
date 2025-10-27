# Four Module train setup 

EAST 0 Module:
trig links 11,12,13
daq links: 4

EAST 1 Module:
trig links 7,8,9,10
daq links 5,6

WEST 0 Module:
trig links: 0, 1, 2
daq links: 2




# ROC config errors:

DEBUG    : 2023-12-10 13:56:12,003 : (roc         ) :  block: DigitalHalf, blockId: 0, param: L1Offset,  R0: 46, R1: 11, value to write 25
DEBUG    : 2023-12-10 13:57:39,960 : (roc         ) :  block: Top, blockId: 0, param: RunR,  R0: 160, R1: 5, value to write 1


Timeout while waiting for I2C master to finish (status:0x00)
INFO     : 2023-12-10 14:47:41,147 : (roc         ) :  block: Top, blockId: 0, param: in_inv_cmd_rx,  R0: 160, R1: 5, value to write 1



data not making it to some LC links on L1A (links not aligned with modules). only configured LCs once. then tried to reconfig inv_cmd_rx parameters on ROCs. Got the timeout error for every roc. Then data seen on all LCs

! OK - timeout is probably meaning - IC_source is not set correctly.

# add logging info

- from fw reload
saw 1 module I2C crash at idle pattern reading for pairs setup
- gpio cyle for all modules didn't help
- gpio cycle for single module, followed by second reset fixed the first ROC
- 1 roc came back, second 2 didn't. On the inv_cmd parameter setting the third roc was successful. on second config attemp all rocs were back

New proceedure if a module doesn't config: 
power cycle rocs
reset twice
reset I2C masters
then config

Would still be good to see an i2c failure during config write (to check if debug code working)

# reset clocks after successful config and all data on LC was good
didn't power of ROC with GPIOs


number of I2C reads: 182, number of partial registers: 199

don't mask tot, toa
now read 34 of 51 regis
number of I2C reads: 34, number of partial registers: 51

# testing the speed of i2c
time between pair setup and roc configured (ie. just the writing )
setting 1
1.2sec




