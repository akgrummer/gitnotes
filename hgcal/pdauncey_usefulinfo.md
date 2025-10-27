
email 2025May15
Hi Aidan,
I see

Frame 0003    0001 0000000019999fe0
Frame 0004    0001 00000000033333fc
Frame 0005    0001 00000000033333fc

which are just bit shifted by a few bits. I can adjust for that for now.

You might not have seen this as the DataFramer always needs to be configured to see anything sensible in EMP capture as one word is repeated for the whole BX. The command you did yesterday

BoardCommander.exe -w VcuHybridConfiguration.yaml writeConfiguration

will configure this. I will try a few things now assuming you are done. Thanks,
            Paul





email 2025May21

Hi Aidan,
A few quick comments on one point

One module is connected to Trig East (channel 105). No modules on Trg west (but it is configured).
These three words are regular throughout ch105 data. The first word is the same throughout. The second two words rotate through ending with 048 248 448... e48 048

Reminder: there are only two elinks; the third word is the duplicated invalid word.

Anyway, the incrementing is good. The baseline noise tends to be small compared with the TC LSB so we usually get identical values for the TC energies in most BXs. Hence the changing bits are the BX counter. It is four bits, the MS bit is set to zero followed by a three-bit counter (except at BC where it sets the fourth bit to give 0b1111). The counter should be the MS four bits of the elink word. The fact that it is clearly counting means the elink is alive which is good! It also tells you how far to shift the word to align it properly. In case not clear, you need to see 0x0<blah>, 0x1<blah>, 0x2<blah> .. 0x7<blah>, 0x0<blah> .. at the top end of the elink 32 bits when it is correct. If you hit a BC0, you will see 0xf<blah> but that is obviously rare.

For the other elink. I don’t know what you have attached. Is it supposed to be two (tile?)modules, each with one elink, or one module with two elinks? If the latter, then fine; only the first has a counter so the other is likely to be constant. It does mean they are the wrong way around though, so we would need to adjust the framer configuration to correct this (see below). However, if there are two modules, both should have a counter, so there is something wrong with the other module as we don’t see it counting.

If it is two elinks from one module, then to swap the order, you could add the below into an extra yaml file and use Reconfigure to upload it when you are about to start a run. You will see just the 5 and 6 are inverted. BTW: I haven’t checked this so you should let me know if it doesn’t swap them properly! You *could* put this into the default VCU configuration file but you might want to keep that the same for both CERN and FNAL in case there are common updates needed in the future. Cheers,
              Paul

DataFramer:
  DataFramerRx:
    105:
      - Address: 0
        Shift: 0
      - Address: 1
        Shift: 0
      - Address: 2
        Shift: 0
      - Address: 3
        Shift: 0
      - Address: 4
        Shift: 0
      - Address: 6
        Shift: 0
      - Address: 5
        Shift: 0
