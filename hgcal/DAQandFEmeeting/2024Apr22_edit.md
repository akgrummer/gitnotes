

KIT: 
    Fabian:
    - Got econs running in the tileboard setup!
    - aligned \\roc to econt\\ and \\econt to serenity\\
    - successful configuration of front end chips. Repurposed existing software.
    - tested link from serentiy to daq PC. DAQ PC, unpacker, serenity
    - Helping student get setup with ZCU setup. Some scripts to test some simple cases in swamp
    - Aiming at continuous integration tests with a standalone ZCU setup
    - econD emulator to be added will employ help from Raghu

DESY:
    Katja, Mathias, Antoine, Jia-Hao
    -
    - climate chamber tests are ongoing
    - two boards with HGCROCv3b are being tested
    - Kria studies haven't started yet

    Mathias has questions about pins connecting to Kria board
    - The fw pin outs need to match before tests can begin
    - Joe: has maps for Kria to hexacontroller or through Jeremy's adapters. Will to send to Mathias.
    - Mathias will compare to mapping and may require an updated fw version

    Question (Antoine, Mathias): Tileboard test requires recompiling software?
    - Arnaud: from v3 to v3b - no fw difference needed. C++ software should work, but will see data corruption

    discussion with Arnaud:
    - HGCROC V3b header is a bit different
    - RPM for ROCv3b is available - can download on PC and send to tileboard if needed
    - Can recompile on tileboard tester
    - Kria image comes with some firewall. Maybe this will allow DESY to have Kria's on internet?

    - Jia-Hao adds that he will continue working on LED control in software
    - Mathias (question from Zoltan) : tileboards arrived at CERN

CERN:
    Arnaud:
    - adapting software for Kria, setting up pipeline for alma 9 and centos 7 on both x86 64 and arch64
    - yum setup and rpm repo is behaving strangly...
    - website doesn't properly update without manual intervention
    - help is welcome

    - Updating software for ROCv3b
    - small suprise: some names of registers have changed, logical meaning is the same.
    - some config files for SWAMP won't work anymore (designed with v3a)

    - 43 hexaboards with ROCv3b have arrived at CERN
        - QC test of hexaboards is ready...
        - will start testing hexaboards tomorrow.
        - tests include slow control and pedestal readout
        - to be added later:
        - dont test if econ pins are functioning well
        - fast command and clock not being tested in hexaboard tests...

    Pavel P.: 
    - prettier diff of register differences - to be added to cass-sw repo in a new branch
    - to work on manual interventions to debug why west lpGBT clock doesn't set properly

    Leon joined the team - Technical student at CERN.
    - working on XDAQ


FNAL: 
    Danny:
    - Econ user manual is being developed.
    - O(1k) Econ chips arriving in a few weeks

    Aidan:
    - Working out bugs in data collection on ZCU for single and multi-engine fw designs
    - Continuing to use GUI for configuration. Every system seems to require unique setup procedures

    Zoltan:
    - Cold room is ready
    - Cassette stations setup PC, rack, powersupplies
    - Four stations for preseries cassette work
    - pre-series tests can keep going.

    Joe:
    - waiting for tileboard to keep debugging FW.

    Devin:
    - Refining testing infrastructure for wagon and engine production
    - Organizational progress to report: bins for parts, more shelving, etc.

CERN (Alp and Martim join the convo)
    Alp:
    - working on full DAQ FW backend
    - includes 54 minidaqs and amoung other blocks
    - Martim is helping with readout blocks to S-link stream

    Zoltan asks Martim about High Tech Global progress: 
    - still some "question marks" regaring hightech global board...
    - main questions: tweaks for EMP to work for miniserenity, 
    - TDC data to miniserenity is still a question mark

    Arnaud:
    - Miniserenity to interface with external clock?
    - Martim: If you want to emulate a serenity need TTC stream..
    - but available bit file would allow single mini-serenity tests
    - Arnaud says he will work on this testing if time allows.



