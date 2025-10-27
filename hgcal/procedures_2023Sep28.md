# if zcu  does not have right readings on TX zcu status output start here
sudo fw-loader load active
./zcu_multitool.py --setrefclk
./zcu_multitool.py --resetlink

# if zcu already has right readings TX, can start here
sudo fw-loader load active
# need to apply polarity first it seems
./zcu_multitool.py --polarity 1 --olink 1
./zcu_multitool.py --polarity 0 --olink 2
# polarity should read 3 (after zcu_multitool status)
./zcu_multitool.py --status
./zcu_multitool.py --setrefclk
./zcu_multitool.py --status
./setup_lpgbt.py --linktrick --protocol AUTO --daqonly
# now RX40 is correct
./zcu_multitool.py --status
./setup_lpgbt.py --vtrx
# VTRX version 1 is output, one or more of RX1-40 and RX2-40 are correctly set now
./zcu_multitool.py --status
###
# TRYING: - this works for getting the clocks - but the data doesn't come through on the Trig links at the end
./setup_lpgbt.py
./setup_lpgbt.py --mode V3_ALL
###
# instead of using the DLL hack (needed to get lpgbt register 0x1d9 to read 13)
./setup_lpgbt.py
setup_lpgbt.py (with DLL Hack set to true)
###  
./lpgbt_status.py --mode V3 -t E --old
./zcu_multitool.py --status
./setup_lpgbt.py --linktrick --protocol AUTO

# Now all clocks are set up correctly.

I have some other procedures for getting to data on the trigger elinks which are not as reliable - but with enough time I am able to see the idles and data packets.
For this I use some of the scripts on branch engineSetup_FNAL.
I use mode V3_ALL in  setup_lpgbt.py and sometimes the link trick. I reset the gpois and set the run bits on the rocs. 

At the moment I am dumping the lpgbt registers for both the DAQ and East TRIG lpgbts thoughout the process to see where things get hung up


