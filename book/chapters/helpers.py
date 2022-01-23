import awkward as ak
import numpy as np

def match_objects(main_objects, objects_to_match):
    '''Match, by eta/phy, objects from `main_objects` to `objects_to_match`.
    Return a list of the matched objects.

    All arguments (and the return) are assumed to be event-by-event records.

    NOTE: There is currently no:
    - Wrap around calculation for phi
    - If nothing is close in `objects_to_match`, then something will get returned anyway.

    Args:
        main_objects (ak.Record): The main objects, with a `eta` and `phi` field.
        objects_to_match (ak>Record): The objects to find a match from, with `eta`, `phi`, and `pt`.

    Returns:
        [type]: [description]
    '''

    to_match_pt = objects_to_match.pt
    to_match_eta = objects_to_match.eta
    to_match_phi = objects_to_match.phi
    eta = main_objects.eta
    phi = main_objects.phi

    pair_eta = ak.cartesian([eta, to_match_eta], axis=1, nested=True)
    pair_phi = ak.cartesian([phi, to_match_phi], axis=1, nested=True)

    delta_eta = np.abs(pair_eta[:, :, :]["0"] - pair_eta[:, :, :]["1"])
    # TODO: Missing wrap around fro phi
    delta_phi = np.abs(pair_phi[:, :, :]["0"] - pair_phi[:, :, :]["1"])

    delta = delta_eta**2 + delta_phi**2

    # TODO: remove anything larger that 0.2*0.2
    best_match = ak.argmin(delta, axis=2)

    return ak.Record({"eta": to_match_eta[best_match], "phi": to_match_phi[best_match], "pt": to_match_pt[best_match]})
