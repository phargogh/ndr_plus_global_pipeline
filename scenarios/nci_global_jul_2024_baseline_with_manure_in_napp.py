"""NCI Global NDR Scenarios

These scenarios were created in late August/early September 2022.  In December,
2022 we started to put them together into a single pipeline that could be run
in sequence.

The major change in this scenario implementation is how we're passing filenames
from one pipeline component to the next: via JSON files rather than defining
them here all in one big dictionary.
"""

import json
import logging
import os
import sys

# Log to stdout, including the date/time format to match the logs produced by
# the pipeline.
BIOPHYSICAL_TABLE_IDS = {
    'nci-ndr-biophysical_table_forestry_grazing': 'ID', }
ECOSHARD_PREFIX = 'https://storage.googleapis.com/'
SHERLOCK_SCRATCH = os.environ['SCRATCH']
ECOSHARDS = {
    'nci-ndr-biophysical_table_forestry_grazing': f'{SHERLOCK_SCRATCH}/nci-ecoshards/nci-NDR-biophysical_table_forestry_grazing_md5_fbd7364c71c6fe45b45d1db428f05600.csv',
    'worldclim_2015': f'{SHERLOCK_SCRATCH}/nci-ecoshards/worldclim_2015_md5_16356b3770460a390de7e761a27dbfa1.tif',
    'baseline_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/modifiedESA_2022_06_03_md5_7dc8402ad44251e8021f4a72559e5f32.tif',

    # This is the N applied per pixel, including N from manure.  This is
    # calculated by:
    #    AppliedNperharvestedha2015_Gerberetal_Scaledto2015_ConstNUE_CropGridsArea_nomanure.tif
    #    multiplied by
    #    Harvestedha_WithNapplication2015_Gerberetal_Scaledto2015_ConstNUE_CropGridsArea_nomanure.tif
    #    plus
    #    ManNitProCrpRd_yy2014_ext.tif multiplied by the pixel area in km^2.
    'baseline_fertilizer': f'{SHERLOCK_SCRATCH}/nci-ecoshards/2024-07-23_n_load_with_crop_yields_and_manure.tif',
}

# put IDs here that need to be scrubbed, you may know these a priori or you
# may run the pipeline and see an error and realize you need to add them
# TODO: fix the n application pipeline to not produce nans and others that must
# be scrubbed.
SCRUB_IDS = {
    'baseline_fertilizer',
}

try:
    with open(os.environ['NCI_SCENARIO_LULC_N_APP_JSON']) as lulc_scenarios_json:
        loaded_json_data = json.load(lulc_scenarios_json)
        ECOSHARDS.update(loaded_json_data)

        # Assume n_app rasters need to be scrubbed, not the LULCs.
        for key in loaded_json_data.keys():
            if 'n_app' in key:
                SCRUB_IDS.add(key)
except KeyError:
    # Not necessarily an issue; we might be just listing out the scenarios in
    # order to define the jobs to run.
    pass

SCENARIOS = {
    'baseline': {
        'lulc_id': 'baseline_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'baseline_fertilizer',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
}
