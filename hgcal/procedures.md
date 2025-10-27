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

# Then using FNAL git branch (haven't determined why this is needed)
- run this (sets the drive stregth for the clock setup correctly (?)):
./setup_lpgbt.py --device zcu --mode V3_ALL
- Then reset the ROC gpios (a version of ./doSetup.sh)
- Sometimes rerun the link trick with setup lpgbt
- Set the run mode on the ROCs (with ./roc_test.py in ./initAndAlign.sh)
    - subblock 45 register 0 set to AB is used in Arnaud's config - and results in idles instead of 1s and 0s

Now get data on the TRIG links with the TRIG link capture block
But do not get data on the DAQ links with the DAQ link capture block

