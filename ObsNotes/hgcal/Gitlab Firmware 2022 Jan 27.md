## how to create the bitstream file for the ZCU102 following the CERN workflow
#### Meeting with Michael and Zoltan
#### 2022 Jan 27
for ber measurement: 
j
https://gitlab.cern.ch/cms-hgcal-firmware/enginev2_zcu

#### instruction from Jon to Michael:
clone enginev2_zcu, with the --recursive flag so it clones the submodules, too.  
 Then make a new branch, so that you are not doing development directly on master. `git checkout -b develop` or some similar name.  
 Then navigate to the link_capture directory `cd shared/ip_repo/link_capture`  
 From that directory, check out the `develop` branch of link_capture `git checkout develop`  
 Then go back to the enginev2_zcu directory, and add the update of the submodule to the changes to be committed `git add shared/ip_repo/link_capture`
 Commit the change with an appropriate message git commit, and finally push the new develop branch `git push --set-upstream origin develop`


 dtbo


 as long as you are pushin to cms-hgcal-firmware the firmware should be compiled



sm8 pair accept trigger
trinze - if sees data, ignore idle patterns 
new chips
new modules


store ns location of event - 16 bins
save in fifo
readout fifo into cpu - write to file
- need to pick out a computer
- need to read data on the zcu
