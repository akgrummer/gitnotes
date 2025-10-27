# Goals 
## Jan
goals - 
*understand the problem:*
- run combine to get the Goodness of Fit stats
- compare the limits between validation and control regions
    + run some points that are bad in the validation limits for CR
    - run all points - for both control and validation region
- compare the limits to new sigma plots 
    + produce sigma plot for validation region, CR
    + 1d for a mX bins(?)
    - produce plots for all points
- run the limits and the sigma plots with different bins

train the BDT with a grid search of hyper parameters 
 - use condor submission for this?
 - optimze the classifier bdt as well?


error bars 
lines
limits

for the plots - want to match the bin for the sigma plot 


plan - run the Validation limits for the orig binning and rebinned outplotters (make sure you don't overwrite the orig binnning...)
 - also run the CR limits with the new binning

- Jan 26:
validation and control region limit plots
regular bins and rebinned

## Feb 4
- train BDT on a single mass point
- compare 3b and 4b for all mass related variables
	- what binning to use for b quarks? Need to look at the ntuple root file with TBrowser
- Anadi's questions about H background and QCD sculpting

## Open To Do list:

1) retrain the BDT with only mX and mY, and without mX and mY - compare limits to original training (for just one mass point)
2) plot tt and QCD separately in mX-mY plane
3) produce the relevant limit values using the lower/upper control (validation) regions only
4) produce the relevant limit values using events with higher value of the b jet pt
5) compare 3b and 4b data for all mass related variables
	- what binning to use for b quarks? Need to look at the ntuple root file with TBrowser
6) why do we have a 2nd peak in the MC mx vs mY?
7) Why is the region at low mX (300) bad for both the CR and VR? For larger mX the agreement is ok in the CR.
	- The VR are instead unstable, but only till mX=1200, for heavier resonances the problem seems less present?


- Also, look at 1D KS test of unfoldered mX, mY distributions


1d distributions of mX and mY for the BDT trainings (with different input variabels)
QCD, ttbar distributions
right or left side of the validation regions
smaller portions of the validation regions (is there a dependence in one direction)
limits table vs 1d ks test of unrolled 

## Mar 22
1) Make the unrolled distribution comparisons in the CR (same as was done in the VR)
	- Check the unrolled plots with ttbar overlayed – can the problem still be in ttbar?
2) Try re-ordering the bins in the unrolled distributions - look for trends in the 3b Scaled-4b ratio and rerun the limits
	- Look at top signal bins- what is the ratio in 4b/3b
	- Can reorder the bins based highest signal
	- alternatively,  on the highest 4b bins or randomly ordered bins
3) Identify the location of the >=3 sigma ratios from the unrolled plots
	- Plot the ratio in 2d with a threshold – where are the highest values?
	- rerun the limits without the 3 sigma ratio bins
	- rerun the limits for just a good section of the unrolled plots
4) produce the relevant limit values using the lower/upper control (validation) regions only
5) produce the relevant limit values using events with higher value of the b jet pt
6) Perform the same ttbar closure test on QCD
7) Construct a test comparing 2b to 3b?
8) Sanity check: provide combine the same background distributions for the model and the target. Confirm the observed lies on top of the expected
9) Inject signal into the background model - how much signal is required to get the observed and expected discrepencies


Other things we have talked about in the past:
1) compare 3b and 4b data for all mass related variables (maybe include them in the BDT)
2) why do we have a 2nd peak in the MC mX vs mY?
3) Why is the region at low mX (300) bad for both the CR and VR? For larger mX the agreement is ok in the CR.
	- The VR are instead unstable, but only till mX=1200, for heavier resonances the problem seems less present?

## Apr 4
1) try changing the systematics - see if limits are imporoved: (limits were improved - the Expected increased faster than observed)
	- double, x5, x10, the uncertainty in the unrolled script
	- if this is the issue - we need to understand where the missing systematic is originating (BDT? how to assign uncertainty as a function of weight)
2) rerun the limits - excluding the first bins - probably not that important( since we excluded bins based on sigma)
3) understand the generic constraints - these were the zero bins
	- verbose output on combine
4) produce the relevant limit values using the lower/upper control (validation) regions only
5) produce the relevant limit values using events with higher value of the b jet pt
6) Perform the same ttbar closure test on QCD
7) Sanity check combine - run the limits with a statistical generated dataset
8) Sanity check: provide combine the same background distributions for the model and the target. Confirm the observed lies on top of the expected
9) Inject signal into the background model - how much signal is required to get the observed and expected discrepencies


##  Apr 8

1) how to apply an uncertainty to the BDT weights - thinking task
	- can you expand the region? 
	- can you segment the cr and train progressivly towards the VR?
	- uncertainties on the hyperparamter choices?
	- uncertainty on the input variables?
2) narrow down systematic corrections to the bin by bin uncertainty on the BKG (3b) - maybe not that important
3) run the BDT classifier on the validation region reweighted 3b vs 4b - previously only did this for control region - we already have the KS test
4) produce the relevant limit values using the lower/upper control (validation) regions only
5) produce the relevant limit values using events with higher value of the b jet pt
6) Perform the same ttbar closure test on QCD
7) Sanity check combine - run the limits with a statistical generated dataset
8) Sanity check: provide combine the same background distributions for the model and the target. Confirm the observed lies on top of the expected
9) Inject signal into the background model - how much signal is required to get the observed and expected discrepencies


## Goals Apr 15
1) read ATLAS paper
2) looking at full 2D plane of sigma (4b,3b) in mX and mY
3) run multiple seeds
4) random datasets training
5) 

## Goals - 
- add a comparison of all limits:
	- expected - observed / sigma
	should expect a gaussian centered at 0
	maybe with long tails	

validation region - 
- replot the (obs - exp) / sigma
- id the problem bins in the unrolled in the VR and see if there is an issue in the same bins in the CR
- possible to see if the bins are the same moving to regions closer to the SR (split the VR)


- in Val, out Val - 
- MC check
	- distributions
	- number of yields table
		- look for an accumulation of the yields in a given process
- exclude outer halfs of CR and rerun
- ratios/uncertainty 
- plot distributions of data before reweighting
- vector moson to jet
- W 


the peaks structure is different in the years?

# May 25
1) sigma plots
2) MC plots (using scripts/privatescripts/stackplots.c )
3) some MC plots
4) pT cut on 2016 - does it impact the peaks in the unrolled?

# May 27
- look at the events in the individual peaks 
	- plot the variables
- look at the bins and the btag score - 
	- maybe cut on the 3b btag scores at the skim


- apply the inner CR to the inner and outer validation region
- capture number of events in the tail
 - 1 sig, 2 sig, 3 sig

Run the combine limits

# Jun 22
- rerun limits for half region splittings with btag score requirements
	- suspect quarter splitting is too limited by statistics (need to look at the stats)
- rerun limits with higher pt cuts on the jets
- ttbar corrections?
- run all mass points again?
- BDT systematics studies?
- look at variable distributions for different regions

questions
- loose btag cuts are large - investigate a lower cut?
	- Is it ok to use loose b-jets for the 4th jet? Should we really veto loose bjets?
- uncertainties - kinfit up and kinfit down BDT training


# Jul 6
1) Rerun BKG normalization freeze without loose b-tag requirement
2) Look at Combine post fit distributions
3) Train BDT without mass window selection (apply to same mass window point)
4) Look at all mass points

- use difference between 3b and data for bkg shape definitions
- train BDT on shapes and simply provide bkg norm from 3b/4b ratio (allow bkg to float in Combine)

- apply stonger b-tag cuts.

# Jul 15

- is the normalization in low and high mass regions the issue now?
- 2D plots in 16, 17, 18 - are the ratios worse in low mass
	- in different selections - for different btag selections
- Run the BDT in different mass groups?

# Aug 5
- signal in the signal region
- 2d hists sigma, as a 3d lego plot
- rmax -30 to 30 -parameter in combine. make them smaller for high masspoints. start with one high mass point to understand the range.
	- maybe it should be from 0 to 30
	- empty bins in high mass?
	- rebinning help?


# Sep 23
- Normalization uncertainty an issue?
- mx - my cut label
- zoom in on full BDTs mass range
- complete studies of multiple hyper parameters (talk to Daniel?)
- cut out low mX mass points