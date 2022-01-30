# Data Samples

ATLAS data comes in many flavors. Because the complete data is so large, ATLAS makes a number of different samples that are slimmed down in various ways. The consequences of this can be far reaching: if a derivation removes attributes necessary to perform a calibration for muons, then accessing calibrated muons will fail.

In general, we'll be accessing DAOD_PHYS datasets (more information about them can be found [here](https://twiki.cern.ch/twiki/bin/viewauth/AtlasProtected/DerivationProductionTeam)). These are complete, with all objects, though they have some rather severe object cuts that makes them useless for a number of physics final states (for example, no tracks less than $p_T$ 10 GeV are included).

## R21 (Run 2)

For Run 2, software release R21, we use the following datasets:

| Name         | Events | Dataset     |
|--------------|-|-------------|
| `ds_Zee`     | 69,734,200 | mc16_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.deriv.DAOD_PHYS.e3601_e5984_s3126_s3136_r10724_r10726_p4164 |
| `ds_Zmumu`   | 292,915,100 | mc16_13TeV.361107.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zmumu.deriv.DAOD_PHYS.e3601_e5984_s3126_s3136_r10724_r10726_p4164 |
| `ds_jz2_exot15` | 15989500 | mc16_13TeV.361022.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2W.deriv.DAOD_EXOT15.e3668_s3126_r9364_r9315_p4696 |

You can find the datasets like `ds_Zee` defined in the `config.py` file as follows:

The datasets were picked on advice from experts in ATLAS and then using the [AMI dataset finder](https://ami.in2p3.fr/), which is a very useful way to scan for datasets you already know must exist.

## R22 (Run 3)
