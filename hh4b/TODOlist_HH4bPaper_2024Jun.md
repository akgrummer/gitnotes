# TO DO list for the paper

- mX=650 points in limit plots...
- (for combination)send table of limits to Alexandra
- NMSSM version , probably ok! version 5.6.2 only goes down to 900 GeV - which is now where we are sensitive - was aimed at the boosted analysis.

- add feynman figure to paper.
- add BDT variable plots: mX, mY
- Put high mass region cuts on the 2D distribution plots
- Background composition plots for mY=90, range around mY=90, ratio of ZH in 3b to 4b, ratio of bkg in 3b to 4b.
- Email John Alison ask about Z+jets samples, cross sections, if it is negligable...


- move to el9 jobs submissions (copy method from GoF example)





Trigger efficiency systematic: larger on the diagonal. May need further explanation.
The larger effect on the diagonal is because it is in the least boosted region and
the trigger efficiency determiniation is performed closest to the trigger turn on curves.

Dominant source in background with a percentage

Move the exact percentage contributions for signal in to the explanation paragraph (2nd paragraph)


Get dataset name from DAS on firefox:
dataset=/NMSSM_XToYHTo4b_MX-700_*_13TeV-madgraph-pythia8/*18*/NANOAODSIM
search dataset name to
https://cms-pdmv-prod.web.cern.ch/mcm/
for smallest PREPID (no premix/miniaod/nanoaod in the name) select "Get setup command"
from here use the
SCRAM_ARCH info
and CMSSW version to run the command on lpc:
from directory:
/uscms/home/agrummer/nobackup/DiHiggs_v2/

```
cmsrel <CMSSW-version>
cd <CMSSW-version>
# cmsenv # but it didn't work, probably dont need it
scram tool info pythia8
# found scram command from :
# https://github.com/cernopendata/opendata.cern.ch/issues/2511
```

2016 dataset:
HIG-RunIISummer15GS-03164
Name : pythia8
Version : 226-ddibom8

2017:
HIG-RunIIFall17GS-00169
Name : pythia8
Version : 230-ghjeda5

2018:
HIG-RunIIFall18GS-00081
Name : pythia8
Version : 230-gnimlf5




new:
details on the MC simulations:
lines 97-98, 107-109

reshuffling of information in the systematics section:
impacted lines: 202-204, 209-212, 214, 226-227


