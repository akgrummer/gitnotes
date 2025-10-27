# talk 2025 Feb 17

slide 3
takes 1 day for technicians to build cassette
which sets 1 hr for testing cassettes
1 hr is an upper limit

single module testing use Kria zynq based
switching to serenity like system
ik
can we fit



review number of cassettes
504 CEH
156 CEE

many varieties
o


Missing context
need to present the plan
also show the new schedule (from Karl's talk)

Mid may anual review and P2UG review
Starting pre-production in MidMay

Need cassette tester by begginign of april -

cassette
one month to make it work
need a working system


24 cassettes
pre-production

time contraints slide
reception testing of module with KRIA
warm test with VCU
Cold room tests with Serenity.

Thinkgin to extend Kria's to cassette level - now thinking to use serenity like
CAF
2 per day to fit in a year
one day for tech to build cassette



what tests happen at cassette
shedule - time
one hour to test cassett

connect to entire cassettee and read all modules simultaneously
must go in parallel
Need VCU instead of ZCU

need a convenient GUI interface
user friendly by Sept. Oct.


How do we reach these goals?


need to establish a group of experts
participate in developement of cassette tester
being available to test cassette
teach students to test cassettes

familiarize eveyone with test beam setup
allows to learn the system
analyze and monitor quality

make concrete plans for what shape the single cassette tester
how to do what we envision
eveyone picks something up and works on the development

Slide on VCU hardware status

Arnaud's slide



Power supply interface
VCCOA
safety
zemans PLC kingdom
used cernwise
group that is developing
vincc
control environment
cern develops drivers in communication with makers
wincc

OPC server
Jacob framework
winccoi
Jacob is a group at CERN
JCOPfw

com with backend - has to done separately
PLC parts
CERN in the past helped in developing - was easier to take and add to


CAEN BV and CAEN HV
trigger pannels

DSS and DCS that interacts with the DSS.
Can things be added to DCS? - things in PLCs can be configured, but new parts cannot be added

Thresholds, disable,
will not only be CMS wide  - it will be JCOP wide

DCS to DSS, based on a common block
relays are built
bitwise
group of actions - size of words, on windows PC, or size of words in PLC.

Power Supply Discussion:
MPOD Weiner parameter for trip time max current:
outputTripTimeMaxCurrent




###

Raghu:
- Why is local readout different from what has already been developed? it is not. Poor language use on Aidan's slide.

Jeremy:
- Need a list of tests
- Do you need to readout trains modules individually?
- You have a resister on the wagon that can be used to identify the wagon that is connected.

Arnaud:
- power profile will tell you if configuration worked well
    - discussion that this could be incorporated into GUI

Andre:
- How many testers will we have? (four in each CAF)
- Is 10 cassettes/2weeks for CE-E an acceleration plan? A from Maksym: yes, nominal value is 6, max is 10.
- Understand the 30 min window for testing - is this 30 min total throughout day?
    - Karl suggests to define this number from the bottom up instead of top down constraint...
- IV curves - do you really need to do this? Zoltan says we can monitor things individually
- The call for people wasn't in the title
- Development suggestion - configuration visualization (website/GUI). Needed and could last longer than cassette assembly.


###
sipm on tile session


trimming of ROC parameters
need to store temperature at the time too
-> trimming settings need to be checked upon reload (after they are stored)

current draw in QC?
readout of power in QC will be added at a later stage.

30 min per board



https://lpgbt.web.cern.ch/lpgbt/v0/registermap.html#x0c3-eptx33-32chncntr





