watch dogs trigger the alerts
hdr counters
hdr_count_x_0
... hdr_count_x_11
status clear the alerts
configurable clear watch dog command
clearing_fcmd_ctrl

the reset requests look for sets of alerts
reset request
there are 2 reset requests
updates with clock cycle - auto refresh after clearing watch dog alerts

header trailer mismatches
or crc mismatches
could indicate a link alignment issues or something else

update status bits with certain fast commands
capture_fcmd_ctrl - bitwise assignment (can update on more than one FCMD)


ebr - event buffer reset
all the buffers in roc and econ get reset (all the fifos. (?))
slink1 and slink2


where is bcr in fast command code?


ROC:
BX-trigger sets when to reset the BCR
BX-offset changes what number to do.




## 2025 Jun 5


BCR=3564

econ:
orbsyn_cnt_load_val 0 to 3563
bcr_bucket_default 1 to 3564

ROC
bx_trigger - parameter in the ROC when to send 9
bx_trigger set to 1 (default is 15) if set to 0 it is never sent

bx_offset (roc) 1 to 3564

rx invert on econ
ERX 0-11
invert_data


40 before is to keep data streams happy in real data taking (the packet takes precedent)

rocd reset has to be in range for the bx trigger
sends idles for 400 BXs (used to be 256)
econ takes several hundred to complete the alignment

could happen anywhere in there

low as possible
want the 9 closer to avoid latency
find a snapshot where select values are bewteen 32 and 64 (so in first word - 32 is minimum value for select)




to set the phase manually (track mode 0)
for erx
phase select channel input


cassette -prbs from econ to lpgbt (test link quality)


DEB
