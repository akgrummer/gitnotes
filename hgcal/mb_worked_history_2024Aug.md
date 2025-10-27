285  sudo fw-loader load zcu102-scintmb-r1
286  pwd
287  ls
288  cd hgc
289  ls
290  cd
291  cd mb-sw/
292  ls
293  vim startup_scint.sh
294  vim setup_train_scint.py
295  ./hgc/zcu_multitool.py --status
296  ./hgc/zcu_multitool.py --setrefclk
297  ./hgc/zcu_multitool.py --resetlink
298  ./hgc/zcu_multitool.py --status
299  ./uhal_backend_v3.py -b backend-transceiver-right-0 --node CTL.RX_POLARITY --val 1024
300  ./uhal_backend_v3.py -b backend-transceiver-right-0 --node CTL.TX_POLARITY --val 256
301  ./hgc/zcu_multitool.py --resetlink
302  ./hgc/zcu_multitool.py --status
303  ls
304  python setup_train_scint.py
305  ./enableSwamp.sh
306  python setup_train_scint.py
307  ls
308  ./startup_scint.sh
309  ./enableEngine.sh
310  ./startup_scint.sh
311  ./hgc/zcu_multitool.py --status
312  jobs
313  ls
314  vim roc_configure.py
315  cd swamp
316  ls
317  git branch
318  cd
319  ls
320  cd cass-sw/swamp/
321  ls
322  vim roc_control.py



Notes for successful startup:
- power to MB/TB is off, system is taken apart and reassembled.
- fw is loaded, ref clk is set, polarizations set, link is reset
- power to MB/TB is turned on
- link is reset
- clock to DAQ is good in zcu status
- run: source startup_scint.sh
- clock to TRIG is good as well as DAQ
- ./sca_check.py - gives SCA serial number and temperature
- (sca_check.py is copied from roc_configure.py, removing the roc bits)
output from sca_check.py:
SC Interface initialized
INFO    : Using reply address: 1 - /home/agrummer/mb-sw/swamp/gbtsca_transport.py:141
INFO    : Using broadcast address: 2 - /home/agrummer/mb-sw/swamp/gbtsca_transport.py:146
INFO    : Using SCA address: 0 - /home/agrummer/mb-sw/swamp/gbtsca_transport.py:148
setup transport
reset transport
set sca transport
S/N 49976   Internal temperature reference: 26.3 C



