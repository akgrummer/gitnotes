# Powering

Paul A. : interesting to do 0 point tests on voltage with two trains at FNAL.

# ESR2

Cassettes:
identify - 
can we invoke the right behavior of the chips
not does the chip have the functionality.

at ESR2
- we want to have a list that says we demonstrated X
- then split it up by which institute does it. 


produced by FSU - 

# with Katja, Fabian, Arnaud, Antoine

- functional tests - bit error rates, checking slow control working
resets are behaving as they should
    - soft reset rocs - should not see data coming out
    - once out of soft reset - should be in same state as before
    - hard reset - should not do i2c, should be power on configuration
    - power cycle the ROC, validation action of software and firmware
    - power on default should be checked.
    - except for a few registers are state machine registers - dynamic, might change
    - LDOs and DCDC
    - ALDO resets work?
    - GPIO control lines power enable
    - specific order needed (for mattias)
    - ADC of GBTSCA 
    - probeDC line of ROCs are routed to ADC
    - enable something in ROC so analague signal to ADC 
    - band gap voltage for calibrating the ADC of GBTSCA
        - can only be done with newer systems
    - calibration DAQ
        - sipm roc, this is changed for ROCv3b
- cosmics for tileboard
- mechanics for cassette
- correlation between multiple motherboards
    - one tileboard with flex lead
    - one with longest flex lead (type A)
    - multiple mechanical configurations

- ADC of GBTSCA

- Econ T - I2C to econ still works when 
slow control to check that the resets on econ is still fine
does i2c still work during soft reset
transmitting data should not work


- Minnesota intrest(?):
DCS applications

- LED calibration.
DAC of the lpGBT to an opAMP

Maybe beyond ESR2 reports
- Including B12 tests
- Final like power supply and cables?

