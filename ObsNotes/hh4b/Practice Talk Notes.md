# Practice Talk
- Notes
- Marina: selection
- Anadi: one point selected away
	- changes with respect to 
	- couldn't close with these points
	- with this minor change we see quite good agreement
- event selection on bkg modeling
- event and object selection
	- btag bjet regression
- scale factor corrections
- trigger object matching
- systematic uncertainties - more details, numbers of highest
	- background systematic
	- largest ones contributed, 

Slide 2: have the paper
	- remove Luca?

Slide
Slide 3: `New Link` change
*Impacts* - takes a while to run, comment out in Note
- Self-bias needs to be updates as well
- Add a new slide - changes with respect to previous note
Slide 9 - what fraction of events are reconstructed

After slide 4: 4 resolved b, changes with respect to latest
Slide 8: label tabel
- trigger is parameterized, point to sys uncertainty

trigger 

Silde 9:
- fraction of events correctly paired
- event selection, object reco, 
- mx, my projections

Merge slide 12 with slide 9 - loose diagrams



Split 13 into 2 slides
Add all variable plots in backup

Slide 14: can you remove the peaks in the plots by dividing by bin width?

Slide 13:
 - reweighting the full plane

Slide 14-15, expand ratio plot

uncertainties
- bin by bin
- normalization
- shape

Slide 17: update plots, range and 
Do we know why we are always better? b-tagging is better
low mass the trigger threshold play a roll, why 2016 is worse than 2017 
- Compatible is the message

bbtautau - table of numbers of 
- compare 

Mass senstive 400 to 700

last slide - remove `possible`
Mention ARC


## from Marina on Presentation:

1. I think you could add a slide on Event Selection (jet selection cuts (pT, phi, IDs, etc), b-tagging requirements, b-jet regression, lepton veto if you apply, met filters that you apply, scale factors? other corrections?)
2. You mention KinFit on the Higgs mass first time in the background modeling, I think it could be added to the Slide with the Event Selection
3. Systematics: A table on the most important systematics? How do you estimate the Bkg systematics?

Some of the other comments:

Slide 7:  Fabio: could go faster, no need to specify all the cuts on the triggers, 

Changes slides
Event Sel. and Modeling Slide 9: Analysis Strategy: A bit more on objects selections
             Jaco: What fraction of events do you pair correctly? People might ask what are other ways of pairing. 
             Fabio: add a cut flow (from AN), Jaco: projections MX vs MY?
             Anadi: add a second slide on event selection             
BKG Modeling: Slide 13: too packed, split into 2
               Before and after plots of the input variables 
			   
Systemates: Slide 16: Expand on a couple of systematic uncertainties (bkg, trigger maybe? b-tagging?)
               * How do you do the shape uncertainties? (AN - visual)
               * bin-by-bin uncertainty
               * Add the impacts
Slide 17: Update limit plots, sources of better sensitivities
Slide 19: Why the worse limit on low masses  - no events there (backup)

# Analysis Note
Background Estimation section changes needed
-  Rerun - Background shape
	- /uscms/home/fravera/nobackup/DiHiggs_v2/CMSSW_10_2_5/src/bbbbAnalysis/scripts/calculateBGKshape.C

- background composition plots
	- bkg composition scripts/privateScript/StackPlots.C

- background normalization plots
	- /uscms/home/fravera/nobackup/DiHiggs_v2/CMSSW_10_2_5/src/bbbbAnalysis/scripts/MeasureBackgroundSystematic.C
	- void doMeasureNorm(std::string tagName, int year)

- BDT plots

- BKG bdt comparison
	- privateTools/RatioPlot.C
	- RatioAll(bool useKinFitVariables=true, std::string dataDrivenDatasetName="data_BTagCSV_dataDriven_kinFit")
	- compareallshapesPerGroup
	- RatioAllUnrolledPlot

- Variable Plots

- BDT KS table
	 - grabbed this from the output log file in the training step (first print out of KS test results)
- Number of Events table
	- Printed these from the `plotVars_2022Feb.py` script

Qs for Fabio
- Limits: there is an impacts option - freezing individual systematics...

- Mass groups plot
	- `PrivateTools/PlaneDivision.C`
- t-student tests (plots and table)
	- comment out
- self bias test
	- PrepareModels/runAllSelfBiasTest.sh
	- run in screen
		- after copied down to mac, `find . -name "*both.png" -exec cp "{}" /Users/agrummer/hhAnalysisNote/AN-20-080/figures/systematics/  \;`
- Overlaid mass groups limit plots
	- comment out
- 2D limit plots
		- limits/ProduceAllResults
	- PlotLimits/FromCondor
- expected versus 2016 hh
- 2D MX-MY impact plots
	- comment
- comparison vs NMSSM
- signal extraction extra plots appendix C
	- privateTools/PlotUnrolled.C
		```
		.L privateTools/PlotUnrolled.C++
		PlotAllUnrolled(2016)
		```
	 - copy the original outPlotter.root into another folder to run this (large file 2GB each)
		 - `cp VarPlots/rootHists/fullSubmission_2022Nov/2018DataPlots_2022Nov14_bJetScoreLoose_shapes2/outPlotter.root VarPlots/rootHists/fullSubmission_2022Nov/2018DataPlots_2022Nov14_bJetScoreLoose_shapes2_UNROLLED/`
		 - ./scripts/Unroll2Dplots DataPlots_fullSubmission_2018_v28/outPlotter.root data_BTagCSV_dataDriven_kinFit selectionbJets_SignalRegion HH_kinFit_m_H2_m 0 2400 0 selectionbJets_ValidationRegionBlinded
		 - `./scripts/Unroll2Dplots VarPlots/rootHists/fullSubmission_2022Nov/2016DataPlots_2022Nov14_bJetScoreLoose_shapes2_UNROLLED/ data_BTagCSV_dataDriven_kinFit selectionbJets_SignalRegion HH_kinFit_m_H2_m 0 2400 0`
		 - `./scripts/Unroll2Dplots VarPlots/rootHists/fullSubmission_2022Nov/2017DataPlots_2022Nov14_bJetScoreLoose_shapes2_UNROLLED/ data_BTagCSV_dataDriven_kinFit selectionbJets_SignalRegion HH_kinFit_m_H2_m 0 2400 0`
		 - `./scripts/Unroll2Dplots VarPlots/rootHists/fullSubmission_2022Nov/2018DataPlots_2022Nov14_bJetScoreLoose_shapes2_UNROLLED/ data_BTagCSV_dataDriven_kinFit selectionbJets_SignalRegion HH_kinFit_m_H2_m 0 2400 0`
	- using: `source ./scripts/UnrollAll.sh`
- unrolled plots
	- validation regions
	- shapes - up and down
	- privateTools/RatioPlot.C
		- CompareAllShapesPerGroup
		- RatioAllUnrolledPlots
- events tables appendix G
	- privatTools/ProduceLimitTable.C
		```
		.L privateTools/ProduceLimitTable.C++
		ProduceAllLimitTable()
		```
- limit tables appendix G
- Colors on some theory plots and 2016 plot - cyan is no good. Red hatch is not easy to see either

self bias
limit plots, and table
sig extraction and unrolled
impacts
number of events table


For Suzanne:
Antonios Agapitos
See slides 15 & 16
https://indico.cern.ch/event/1150625/contributions/4831079/attachments/2431327/4163479/B2G_workshop_New_Ideas_and_techniques_v3.pdfo

bkg composition