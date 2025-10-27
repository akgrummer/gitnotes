power distribution in the cassettes
- power distribution and grounding

Latto 

MIP fire TOA in Scintillator section?
set TOA threshold in a meaningful way to avoid fakes or ringing or coupling of channels

tileboards with ROCv3b? part with the right substrate.

packaged rocv3b packaged but haven't been tested.

not to do mip timing after 
nead a higher amplitude for setting toa reasonably.

compare timing of two TOAs with stacked 
resolution will be bad
electormagnetic showers  - not ready for ESR2.

VCU118 has the infrastructer for EMP usage
CERN working to port EMP to high tech global
QSFP mezzanines 
VCU is half cost of high tech global

hadronic cassette.

real serenity.
VCU118 is already supported.
EMP wrapper
not completely different from final system

mini serenity zcu102 working as Kria - connected to big fpga
software point of view would be identical - but fw burden comes at a bigger cost.

high tech global cannot syncronyze all mezzanines.
fw backend meeting 

bootstrap clock synth in high tech global
all 4 of them accepting an external clock.
VCU118 - may not be so different.

Raghu - VCU118 fw is setup, EMP fw is working with VCU118

AXI chip to chip.
EMP libraries is transparent to protocol underneath.


IP bus over udp - same as with high tech global.
x86 and pcie
use the arm?
VCU118 for ceh cassette -  more adaptive.
or for high tech global. (uses VU13p) - has 72/3

FW for both options

we nee 8 engines 24 GTYs
vcu118 6 QSFP+ 11k 

fmc module should have a clock generator for input ports on that fmc
external 

frequency - clock embedded on it. 

pcie express

slow control for pcie 
fw or sw will not give the rate you expect out of the box.
spilt pcie bandwidth.
direct axi link.

QSFP

s-link receiver.
FMC+ with 24 works for CEH



6 port QSFP28
Si5341i
6 cages use the 

clock generator for FMC
would like a syncronous clock 
high tech global 940 RFV 1.0 schematic.

VCU118 mezzanine that has clock syncronyzer
these banks are driven by the mezzanine clock

clock input or something.


