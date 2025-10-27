
Dear Arne, all,

Thank you for your reply!

We've added chi2 test results to the plots. The chi2 results for the 2d hists are computed by hand (i.e. not with a root function).
These are computed using the stat uncertainty of the data and the stat uncertainty of the model added in quadrature.
The chi2 results show improvement between the background and model after cuts are applied on the bjet pT and HT variables.

The KS test results (comparing the shape only) are also included in the plots. These results do not seem to agree with the clear improvements seen with chi2 and the pulls. I've been spending time trying to understand the output of the KS test root function - but I do not trust the numbers.

The unrolled plots were produced using the full machinery of the analysis (and use the output from Combine). I was trying to perform this study quickly using a subset of the analysis hists. It will take longer to remake these plots again (with the many labels and pads) if we need to look at these before proceeding. Could we make a decision on the new event selection cuts to use before going back to the full analysis chain?

It seems that cutting at 90% efficiency of the turn on curve for all bjet pt and HT is the most conservative approach.
Please let us know how you would like us to proceed.

Updated plots are here:
https://cernbox.cern.ch/s/f36qMCmZ8DE8abm

Kind regards,
Fabio and Aidan


