looking at raspi: /home/HGCAL_dev/agrummer/hgc-enginev1/iic.py
the "read_lpgbt" has a "write" in the i2c mode:
line 54



- FC through optical link to the VTRX+ (connector?) then to lpgbt
IC calls for a module called uHAL or micro-hal
uHAL:
https://ipbus.web.cern.ch/doc/user/html/software/uhalQuickTutorial.html
IP-bus:
https://ipbus.web.cern.ch/
IP-bus firmware:
https://github.com/ipbus/ipbus-firmware
and software:
https://github.com/ipbus/ipbus-software