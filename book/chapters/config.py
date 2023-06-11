from dataclasses import dataclass
from pathlib import Path
from typing import Any, List, Union

import awkward as ak
import numpy as np
from func_adl_servicex import ServiceXSourceXAOD, SXLocalxAOD
from func_adl_servicex_xaodr21 import SXDSAtlasxAODR21
from func_adl_servicex_xaodr21 import atlas_release as atlas_release_r21
from func_adl_servicex_xaodr21 import calib_tools as calib_tools_r21
from func_adl_servicex_xaodr21.event_collection import Event as EventR21
from func_adl_servicex_xaodr22 import atlas_release as atlas_release_r22
from func_adl_servicex_xaodr22 import calib_tools as calib_tools_r22
from func_adl_servicex_xaodr22.event_collection import Event as EventR22
from func_adl_servicex_xaodr24 import atlas_release as atlas_release_r24
from func_adl_servicex_xaodr24 import calib_tools as calib_tools_r24
from func_adl_servicex_xaodr24.event_collection import Event as EventR24


@dataclass
class sample:
    "Location of a data sample"
    # Shorthand name
    name: str

    # The full rucio dataset name
    rucio_ds: Union[str, List[str]]

    # Locally where we can find it
    local_path: Path

    # Which release (21, 24)?
    release: str

    # The calibration defaults to apply (e.g. PHYS or PHYSLITE).
    default_calib: str = "PHYS"

    # Use typed access?
    typed_access: bool = True


_samples = {
    "zee_r21": sample(
        name="ds_zee",
        rucio_ds="rucio://mc16_13TeV:mc16_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.deriv.DAOD_PHYS.e3601_s3126_r10724_p5313",
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\R21\DAOD_PHYS\361106\DAOD_PHYS.30943882._001876.pool.root.1"
        ),
        release="21",
    ),
    "zee_r22": sample(
        name="ds_zee",
        rucio_ds="rucio://mc21_13p6TeV:mc21_13p6TeV.601189.PhPy8EG_AZNLO_Zee.deriv.DAOD_PHYS.e8392_e7400_s3775_r13504_r13491_p5057",
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\R22\DAOD_PHYS\DAOD_PHYS.28628223._000007.pool.root.1"
        ),
        release="22",
    ),
    "zee_r24": sample(
        name="ds_zee",
        rucio_ds="rucio://mc21_13p6TeV:mc21_13p6TeV.601189.PhPy8EG_AZNLO_Zee.deriv.DAOD_PHYS.e8392_e7400_s3775_r13504_r13491_p5057",
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\R22\DAOD_PHYS\DAOD_PHYS.28628223._000007.pool.root.1"
        ),
        release="24",
    ),
    "zee_untyped_r21": sample(
        name="ds_zee_untyped",
        rucio_ds="rucio://mc16_13TeV:mc16_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.deriv.DAOD_PHYS.e3601_s3126_r10724_p5313",
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\R21\DAOD_PHYS\361106\DAOD_PHYS.30943882._001876.pool.root.1"
        ),
        release="21",
        typed_access=False,
    ),
    "zmumu_r21": sample(
        name="ds_zmuumu",
        rucio_ds="rucio://mc16_13TeV:mc16_13TeV.361107.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zmumu.deriv.DAOD_PHYS.e3601_e5984_s3126_s3136_r10724_r10726_p4164",
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\R21\DAOD_PHYS\361107\DAOD_PHYS.23295097._000229.pool.root.1"
        ),
        release="21",
    ),
    "ztautau_r21": sample(
        name="ds_ztautau",
        rucio_ds="rucio://mc16_13TeV:mc16_13TeV.361108.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Ztautau.deriv.DAOD_PHYS.e3601_e5984_s3126_s3136_r10724_r10726_p4355",
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\R21\DAOD_PHYS\361108\DAOD_PHYS.23295108._000430.pool.root.1"
        ),
        release="21",
    ),
    "jz2_exot15_r21": sample(
        name="ds_jz3_exot15",
        rucio_ds="rucio://mc16_13TeV:mc16_13TeV.361022.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ2W.deriv.DAOD_EXOT15.e3668_s3126_r9364_r9315_p4696",
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\R21\DAOD_PHYS\361022\DAOD_EXOT15.26710681._000512.pool.root.1"
        ),
        release="21",
    ),
    "bphys_r21": sample(
        name="ds_bphys",
        rucio_ds=[
            "root://eosatlas.cern.ch//eos/atlas/user/d/daits/mc16_13TeV/DAOD_BPHY4/mc16.999031.P8BEG_23lo_ggX18p4_Upsilon1Smumu_4mu_3pt2.deriv.DAOD_BPHY4.e8304_a875_r10724_r10726_p3712_pUM999999/DAOD_BPHY4.999031._000001.pool.root.1"
        ],
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\R21\BPHYS\999031\DAOD_BPHY4.999031._000001.pool.root.1"
        ),
        release="21",
    ),
    "ttbar_r21": sample(
        name="ds_ttbar",
        rucio_ds="mc16_13TeV.410470.PhPy8EG_A14_ttbar_hdamp258p75_nonallhad.deriv.DAOD_PHYS.e6337_e5984_a875_r10724_r10726_p4355",
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\R21\DAOD_PHYS\410470\DAOD_PHYS.23597022._001158.pool.root.1"
        ),
        release="21",
    ),
    "ttbar_r22": sample(
        name="ds_ttbar",
        rucio_ds=[],
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\asg\mc_410470_ttbar.DAOD_PHYS.22.2.110.pool.root.1"
        ),
        release="22",
    ),
    "ttbar_r24": sample(
        name="ds_ttbar",
        rucio_ds=[],
        local_path=Path(
            r"C:\Users\gordo\Code\atlas\data\asg\mc_410470_ttbar.DAOD_PHYS.22.2.110.pool.root.1"
        ),
        release="24",
    ),
}


# Base for a typed local xAOD ServiceX dataset
# (local ==> Will run on a docker container on this machine)
class xAODLocalTypedR21(SXLocalxAOD[EventR21]):
    def __init__(self, file_path: Path):
        super().__init__(
            file_path,
            item_type=EventR21,
            docker_image="gitlab-registry.cern.ch/atlas/athena/analysisbase",
            docker_tag=atlas_release_r21,
        )


class xAODLocalTypedR22(SXLocalxAOD[EventR22]):
    def __init__(self, file_path: Path):
        super().__init__(
            file_path,
            item_type=EventR21,
            docker_image="gitlab-registry.cern.ch/atlas/athena/analysisbase",
            docker_tag=atlas_release_r22,
        )


class xAODLocalTypedR24(SXLocalxAOD[EventR24]):
    def __init__(self, file_path: Path):
        super().__init__(
            file_path,
            item_type=EventR24,
            docker_image="gitlab-registry.cern.ch/atlas/athena/analysisbase",
            docker_tag=atlas_release_r24,
        )


# Make the samples available
use_local = True
sx_backend_name = "xaod_r21"


def make_ds(s: sample):
    """Create the a datasample, local or remote, as requested.

    Args:
        s (sample): The sample to create

    Returns:
        sample: The sample specification.
    """
    sx_ds_name = s.rucio_ds
    if isinstance(sx_ds_name, str):
        sx_ds_name += "?files=20&get=available"

    if use_local and not s.local_path.exists():
        raise FileNotFoundError(
            f"Data file for sample {s.name}, {s.local_path}, is not found!"
        )

    if s.typed_access:
        if use_local:
            if s.release == "21":
                ds = xAODLocalTypedR21(s.local_path)
                ds = calib_tools_r21.query_update(
                    ds, calib_config=calib_tools_r21.default_config(s.default_calib)
                )
            elif s.release == "22":
                ds = xAODLocalTypedR22(s.local_path)
                ds = calib_tools_r22.query_update(
                    ds, calib_config=calib_tools_r22.default_config(s.default_calib)
                )
            elif s.release == "24":
                ds = xAODLocalTypedR24(s.local_path)
                ds = calib_tools_r24.query_update(
                    ds, calib_config=calib_tools_r24.default_config(s.default_calib)
                )
            else:
                raise NotImplementedError(f'Release "{s.release}" is not supported.')
        else:
            ds = SXDSAtlasxAODR21(sx_ds_name, backend=sx_backend_name)
    else:
        if use_local:
            ds = SXLocalxAOD(s.local_path)
        else:
            ds = ServiceXSourceXAOD(sx_ds_name, backend=sx_backend_name)

    # TODO: If we run Overlap Removal, then we must have a PV in the event. Unfortunately,
    # we do not yet know how to filter out events without a PV in them. So we turn off OR
    # by default for now. When this is fixed, remove the warning in the calibration notebook.
    if s.release == "21":
        ds = calib_tools_r21.query_update(ds, perform_overlap_removal=False)
    elif s.release == "22":
        ds = calib_tools_r22.query_update(ds, perform_overlap_removal=False)
    elif s.release == "24":
        ds = calib_tools_r24.query_update(ds, perform_overlap_removal=False)

    assert ds is not None, "`ds` is None - which should not be possible."

    return ds


def __getattr__(name: str) -> Any:
    """Look to see if we can find a dataset that they are asking for

    * Name must start with `ds_`
    * Name must be in the list of known datasets (see `_samples`).
    * Otherwise, raise an `AttributeError`

    Args:
        name (str): The name of the dataset to look for

    Raises:
        AttributeError: The dataset is not found.

    Returns:
        Any: The dataset object.
    """
    if not name.startswith("ds_"):
        raise AttributeError(f"Dataset {name} is not defined.")
    if name[3:] not in _samples:
        raise AttributeError(f"Dataset {name} is not defined.")
    return make_ds(_samples[name[3:]])


# Turns out the muon events don't all have a primary vertex, which is
# required to do overlap removal. So for now we'll turn that off until
# we understand what the proper thing to do here is.
# ds_zmumu = calib_tools.query_update(
#     make_ds(_samples["zmumu_r21"]), perform_overlap_removal=False
# )

# To demonstrate some features of jets, we need an older R21 sample (which contains
# topo clusters). Default calibration is different for this guy.
# ds_jz2_exot15_r21 = calib_tools.query_update(
#     make_ds(_samples["jz2_exot15_r21"]),
#     jet_collection="AntiKt4EMTopoJets",
#     jet_calib_truth_collection="AntiKt4TruthJets",
#     perform_overlap_removal=False,
# )


def match_eta_phi(jets, jets_to_match) -> ak.Record:
    """Match `jets_to_match` to the `jets` given. There will always be
    at least one jet found.

    The awkward array needs to have leaves called `pt`, `eta`, and `phi`.

    Args:
        jets (_type_): Source jets
        jets_to_match (_type_): Jets to match to `jets`

    Returns:
        _type_: Matched jets 1:1 in `jets` from `jets_to_match`.
    """

    to_match_pt = jets_to_match.pt
    to_match_eta = jets_to_match.eta
    to_match_phi = jets_to_match.phi
    jet_eta = jets.eta
    jet_phi = jets.phi

    pair_eta = ak.cartesian([jet_eta, to_match_eta], axis=1, nested=True)
    pair_phi = ak.cartesian([jet_phi, to_match_phi], axis=1, nested=True)

    delta_eta = np.abs(pair_eta[:, :, :]["0"] - pair_eta[:, :, :]["1"])
    # TODO: Missing wrap around fro phi
    delta_phi = np.abs(pair_phi[:, :, :]["0"] - pair_phi[:, :, :]["1"])

    delta = delta_eta**2 + delta_phi**2

    # TODO: remove anything larger that 0.2*0.2
    best_match = ak.argmin(delta, axis=2)

    return ak.Record(
        {
            "eta": to_match_eta[best_match],
            "phi": to_match_phi[best_match],
            "pt": to_match_pt[best_match],
        }
    )
