from servicex import deliver, dataset as servicex_dataset
import awkward as ak

def get_files(query, dataset):
    """Sends request for data to servicex backend.
    
    Args:
        query: FuncADLQueryPHYSLITE
        dataset: String of dataset location

    Returns:
        List of files returned from servicex backend
    
    """
    spec = {
        'Sample': [{
            'Name': "func_adl_xAOD",
            'Dataset': servicex_dataset.FileList(
                [ dataset ]
            ),
            'Query': query,
            'Codegen': 'atlasr22',
        }]
    }
    files = deliver(spec, servicex_name="atlasr22")['func_adl_xAOD']
    assert files is not None, "No files returned from deliver! Internal error"
    return files


def get_files_physlite(query):
    """Sends request for data to servicex backend using a specific PHYSLITE dataset.
    
    Args:

        query: FuncADLQueryPHYSLITE

    Returns:
        List of files returned from servicex backend
    
    """
    dataset = "root://eospublic.cern.ch//eos/opendata/atlas/rucio/mc20_13TeV/DAOD_PHYSLITE.37622528._000013.pool.root.1"
    return get_files(query,dataset)


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

    delta = delta_eta ** 2 + delta_phi ** 2

    # TODO: remove anything larger that 0.2*0.2
    best_match = ak.argmin(delta, axis=2)

    return ak.Record(
        {
            "eta": to_match_eta[best_match],
            "phi": to_match_phi[best_match],
            "pt": to_match_pt[best_match],
        }
    )