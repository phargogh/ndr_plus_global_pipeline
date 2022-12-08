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

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
BIOPHYSICAL_TABLE_IDS = {
    'nci-ndr-biophysical_table_forestry_grazing': 'ID', }
ECOSHARD_PREFIX = 'https://storage.googleapis.com/'
SHERLOCK_SCRATCH = os.environ['SCRATCH']
ECOSHARDS = {
    'nci-ndr-biophysical_table_forestry_grazing': f'{SHERLOCK_SCRATCH}/nci-ecoshards/nci-NDR-biophysical_table_forestry_grazing_md5_fbd7364c71c6fe45b45d1db428f05600.csv',
    'worldclim_2015': f'{SHERLOCK_SCRATCH}/nci-ecoshards/worldclim_2015_md5_16356b3770460a390de7e761a27dbfa1.tif',
    'baseline_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/modifiedESA_2022_06_03_md5_7dc8402ad44251e8021f4a72559e5f32.tif',
    'baseline_fertilizer': f'{SHERLOCK_SCRATCH}/nci-ecoshards/current_n_app_md5_a7e226b3418504591095a704c2409f16.tif',
}

# put IDs here that need to be scrubbed, you may know these a priori or you
# may run the pipeline and see an error and realize you need to add them
# TODO: fix the n application pipeline to not produce nans and others that must
# be scrubbed.
SCRUB_IDS = {
    'baseline_fertilizer',
}

with open(os.environ['NCI_SCENARIO_LULC_N_APP_JSON']) as lulc_scenarios_json:
    ECOSHARDS.update(json.load(lulc_scenarios_json))

SCENARIOS = {
    'current_bmp': {
        'lulc_id': 'current_bmps_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'current_bmps_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'current_lulc_masked': {
        'lulc_id': 'current_lulc_masked_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'current_lulc_masked_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'extensification_current_practices_bmp': {
        'lulc_id': 'extensification_current_practices_bmps_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'extensification_current_practices_bmps_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'extensification_current_practices': {
        'lulc_id': 'extensification_current_practices_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'extensification_current_practices_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'intensification_bmp': {
        'lulc_id': 'intensification_bmps_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'intensification_bmps_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'intensification_expansion_bmp': {
        'lulc_id': 'intensification_expansion_bmps_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'intensification_expansion_bmps_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'intensification_expansion': {
        'lulc_id': 'intensification_expansion_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'intensification_expansion_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'intensification': {
        'lulc_id': 'intensification_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'intensification_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'baseline': {
        'lulc_id': 'baseline_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'baseline_fertilizer',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
}
