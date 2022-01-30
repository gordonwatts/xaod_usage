# Calibrations

Discuss

- pile up and how it is run
- Sys error tool
- Point to the code that actually is run so folks can see 
- You only get the calibration file that is loaded with the release

## Pileup

MonteCarlo is generated and simulated often long before a run is complete. As a result the pileup profile is almost never correct, and given how much extra charged particles are added in the tracker and energy in the calorimeter, getting the pileup profile correct can have a real effect on the analysis result. Many corrections depend on the pileup profile as well (or $\mu$).

When running Monte Carlo the a pileup tool is run as part of the sequence, before the tool that applies the calibration.

To see how this tool is configuring pile up, see...

## Systematic Errors

List of sys errors, etc.?? How does anyone get a list of these things, since ATLAS is meant to be driven from the bottom up, rather than the top down.

### Further Information

- [ATLAS Pileup Recommendations twiki](https://twiki.cern.ch/twiki/bin/view/AtlasProtected/PileupJetRecommendations)
- [C++ Pileup Algorithm Configuration for R21](https://gitlab.cern.ch/atlas/athena/-/blob/21.2/PhysicsAnalysis/Algorithms/AsgAnalysisAlgorithms/python/PileupAnalysisSequence.py)