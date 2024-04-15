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

    # Marconi and Rosa 2024.  Source data: https://zenodo.org/records/10517721
    # The source dataset is 2020_synthetic_nitrogen_tonnes.h5, converted to a
    # GeoTiff using the script at https://github.com/phargogh/2021-nci-ndr-sherlock/blob/main/oneoff-scripts/2024-01-22-assume-raster-is-wgs84.sh
    # Resampled to the resolution of our current lulc raster using the script
    # at https://github.com/phargogh/2021-nci-ndr-sherlock/blob/experiment/2024-01-25-try--marconi-and-rosa-2024-fertilizer-application/oneoff-scripts/2024-01-25-resample-marconi-and-rosa-2024.sh
    'marconi_and_rosa_2024': f'{SHERLOCK_SCRATCH}/nci-ecoshards/marconi_and_rosa_2024_2020_synthetic_nitrogen_tonnes_bilinear.tif',
}

# put IDs here that need to be scrubbed, you may know these a priori or you
# may run the pipeline and see an error and realize you need to add them
SCRUB_IDS = set()

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
        'lulc_id': 'current_lulc_masked_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'marconi_and_rosa_2024',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
}
