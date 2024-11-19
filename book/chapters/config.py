from servicex import deliver, dataset

def get_dataset(jet_info_per_event):
    """Sends request for dataset to servicex backend. Pass in FuncADLQueryPHYSLITE and returns dictionary of files in dataset."""
    spec = {
        'Sample': [{
            'Name': "func_adl_xAOD",
            'Dataset': dataset.FileList(
                [
                    "root://eospublic.cern.ch//eos/opendata/atlas/rucio/mc20_13TeV/DAOD_PHYSLITE.37622528._000013.pool.root.1",  # noqa: E501
                ]
            ),
            'Query': jet_info_per_event,
            'Codegen': 'atlasr22',
        }]
    }
    files = deliver(spec, servicex_name="atlasr22")
    assert files is not None, "No files returned from deliver! Internal error"
    return files