from dataclasses import dataclass
from pathlib import Path

from func_adl_servicex import SXLocalxAOD
from func_adl_servicex_xaodr21 import SXDSAtlasxAODR21
from func_adl_servicex_xaodr21.event_collection import Event

# rucio_zee_r21_mc = "rucio://mc15_13TeV:mc15_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.merge.DAOD_STDM3.e3601_s2576_s2132_r6630_r6264_p2363_tid05630052_00"

# # Define the local dataset (per-machine), and datatype that uses it


# local_xaod_path = Path(
#     r"C:\Users\gordo\Code\atlas\data\xAODSampleFiles\DAOD_EXOT15.26710781._000001.pool.root.1"
# )
# if not local_xaod_path.exists():
#     local_xaod_path = Path(
#         r"C:\Users\gordo\Code\atlas\xAODSampleData\DAOD_EXOT15.26710781._000001.pool.root.1"
#     )

# # Define a dataset we can use so we can import this directly
# # ds = SXDSAtlasxAODR21(rucio_zee_r21_mc, backend='dev_xaod')
# ds = xAODLocalTyped(local_xaod_path)

# # The following two lines will cause the servicex front end to ignore the cache
# # from servicex import ignore_cache
# # ic = ignore_cache()
# # ic.__enter__()


@dataclass
class sample:
    "Location of a data sample"
    # Shorthand name
    name: str

    # The full rucio dataset name
    rucio_ds: str

    # Locally where we can find it
    local_path: Path


_samples = {
    'zee': sample(
        name="ds_zee",
        rucio_ds="mc16_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.deriv.DAOD_PHYS.e3601_e5984_s3126_s3136_r10724_r10726_p4164",
        local_path=Path(r"C:\Users\gordo\Code\atlas\data\R21\DAOD_PHYS\361106\DAOD_PHYS.23294912._000216.pool.root.1"),
    ),
    'zmumu': sample(
        name="ds_zmuumu",
        rucio_ds="mc16_13TeV.361107.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zmumu.deriv.DAOD_PHYS.e3601_e5984_s3126_s3136_r10724_r10726_p4164",
        local_path=Path(r"C:\Users\gordo\Code\atlas\data\R21\DAOD_PHYS\361107\DAOD_PHYS.23295097._000229.pool.root.1"),
    ),
    'ztautau': sample(
        name="ds_ztautau",
        rucio_ds="mc16_13TeV.361108.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Ztautau.deriv.DAOD_PHYS.e3601_e5984_s3126_s3136_r10724_r10726_p4164",
        local_path=Path(r"C:\Users\gordo\Code\atlas\data\R21\DAOD_PHYS\361108\DAOD_PHYS.23295108._000430.pool.root.1"),
    ),
    'jz3_exot15': sample(
        name="ds_jz3_exot15",
        rucio_ds="mc16_13TeV.361022.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2W.deriv.DAOD_EXOT15.e3668_s3126_r9364_r9315_p4696",
        local_path=Path(r"C:\Users\gordo\Code\atlas\data\R21\DAOD_PHYS\361022\DAOD_EXOT15.26710681._000512.pool.root.1"),
    ),
    'bphys': sample(
        name="ds_bphys",
        rucio_ds="mc16.999031.P8BEG_23lo_ggX18p4_Upsilon1Smumu_4mu_3pt2.deriv.DAOD_BPHY4.e8304_a875_r10724_r10726_p3712_pUM999999",
        local_path=Path(r"C:\Users\gordo\Code\atlas\data\R21\BPHYS\999031\DAOD_BPHY4.999031._000001.pool.root.1"),
    )
}

class xAODLocalTyped(SXLocalxAOD[Event]):
    def __init__(self, file_path: Path):
        super().__init__(file_path, item_type=Event)


# Make the samples available
use_local = True

def make_ds(s: sample):
    if use_local:
        ds = xAODLocalTyped(s.local_path)
    else:
        ds = SXDSAtlasxAODR21(s.rucio_ds, backend="dev_xaod")
    return ds

ds_zee = make_ds(_samples['zee'])
ds_zmumu = make_ds(_samples['zmumu'])
ds_ztautau = make_ds(_samples['ztautau'])
ds_jz3_exot15 = make_ds(_samples['jz3_exot15'])
ds_bphys = make_ds(_samples['bphys'])
