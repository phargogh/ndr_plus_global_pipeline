"""NCI Global NDR Scenarios.

These 8+baseline scenarios were reworked/created in late August, early
September 2022.
"""
import os

BIOPHYSICAL_TABLE_IDS = {
    'nci-ndr-biophysical_table_forestry_grazing': 'ID', }

ECOSHARD_PREFIX = 'https://storage.googleapis.com/'
SHERLOCK_SCRATCH = os.environ['SCRATCH']

# ADD NEW DATA HERE
ECOSHARDS = {
    # Biophysical table:
    'nci-ndr-biophysical_table_forestry_grazing': f'{ECOSHARD_PREFIX}nci-ecoshards/nci-NDR-biophysical_table_forestry_grazing_md5_7524f2996fcc929ddc3aaccde249d59f.csv',
    # Precip:
    'worldclim_2015': f'{ECOSHARD_PREFIX}ipbes-ndr-ecoshard-data/worldclim_2015_md5_16356b3770460a390de7e761a27dbfa1.tif',

    # Data for each scenario
    'baseline_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/modifiedESA_2022_06_03_md5_7dc8402ad44251e8021f4a72559e5f32.tif',
    'baseline_fertilizer': f'{SHERLOCK_SCRATCH}/nci-ecoshards/current_n_app_md5_a7e226b3418504591095a704c2409f16.tif',

    # n application
    'current_bmp_n_app': f'{SHERLOCK_SCRATCH}/nci-ecoshards/current_bmp_n_app_md5_8e4f04e61ad34fe88746db22bf980909.tif',
    'current_lulc_masked_n_app': f'{SHERLOCK_SCRATCH}/nci-ecoshards/current_lulc_masked_n_app_md5_74af96964966f678ea1ebda3ae479afe.tif',
    'extensification_current_practices_bmp_n_app': f'{SHERLOCK_SCRATCH}/nci-ecoshards/extensification_current_practices_bmp_n_app_md5_74b02b43f4e44c1ddbb9f9a9d9732f2e.tif',
    'extensification_current_practices_n_app': f'{SHERLOCK_SCRATCH}/nci-ecoshards/extensification_current_practices_n_app_md5_0d4ba212e0048cc8256c5efff7ca098d.tif',
    'intensification_bmp_n_app': f'{SHERLOCK_SCRATCH}/nci-ecoshards/intensification_bmp_n_app_md5_cccf0befa275bc0df5c4565d2fbb559f.tif',
    'intensification_expansion_bmp_n_app': f'{SHERLOCK_SCRATCH}/nci-ecoshards/intensification_expansion_bmp_n_app_md5_014539428f6d14c75c61a553118a821c.tif',
    'intensification_expansion_n_app': f'{SHERLOCK_SCRATCH}/nci-ecoshards/intensification_expansion_n_app_md5_b39bf6f3676097e4fc5c18ffd8398bd7.tif',
    'intensification_n_app': f'{SHERLOCK_SCRATCH}/nci-ecoshards/intensification_n_app_md5_bff78058223fea7995a2ce6660e2bb66.tif',


    # LULCs
    'current_bmp_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/current_bmp_md5_0311380a884e0aa16e5a1d544419205f.tif',
    'current_lulc_masked_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/current_lulc_masked_md5_87e86777e896308c7d2e8f980f0941e6.tif',
    'extensification_current_practices_bmp_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/extensification_current_practices_bmp_md5_ca463b9ffa3ffb3452451f34a2127cee.tif',
    'extensification_current_practices_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/extensification_current_practices_md5_b4856322f2deb75fc3708bdf80d837b1.tif',
    'intensification_bmp_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/intensification_bmp_md5_222da6572f45fe187018234afb240e94.tif',
    'intensification_expansion_bmp_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/intensification_expansion_bmp_md5_947e88214ceb6646e52e25dc45b7f34f.tif',
    'intensification_expansion_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/intensification_expansion_md5_7e1be408200108d8e47cba75aa0984c9.tif',
    'intensification_lulc': f'{SHERLOCK_SCRATCH}/nci-ecoshards/intensification_md5_3fb29255988085eb595f50f98980d6f9.tif',
}

# JD sanity check to make sure these files exist.
for key, value in ECOSHARDS.items():
    if value.startswith(SHERLOCK_SCRATCH):
        assert os.path.exists(value), f'File not found: {value}'

# put IDs here that need to be scrubbed, you may know these a priori or you
# may run the pipeline and see an error and realize you need to add them
SCRUB_IDS = {
    'baseline_fertilizer',
}

SCENARIOS = {
    'current_bmp': {
        'lulc_id': 'current_bmp_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'current_bmp_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'current_lulc_masked': {
        'lulc_id': 'current_lulc_masked_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'current_lulc_masked_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'extensification_current_practices_bmp': {
        'lulc_id': 'extensification_current_practices_bmp_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'extensification_current_practices_bmp_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'extensification_current_practices': {
        'lulc_id': 'extensification_current_practices_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'extensification_current_practices_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'intensification_bmp': {
        'lulc_id': 'intensification_bmp_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'intensification_bmp_n_app',
        'biophysical_table_id': 'nci-ndr-biophysical_table_forestry_grazing',
    },
    'intensification_expansion_bmp': {
        'lulc_id': 'intensification_expansion_bmp_lulc',
        'precip_id': 'worldclim_2015',
        'fertilizer_id': 'intensification_expansion_bmp_n_app',
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

if __name__ == '__main__':
    import sys
    if sys.argv[1] == '--check':
        import numpy
        import pygeoprocessing
        keys_to_check = set()
        for data_dict in SCENARIOS.values():
            for data_key in data_dict.values():
                keys_to_check.add(data_key)

        n_rasters_with_errors = 0
        for data_key in sorted(keys_to_check):
            data_file = ECOSHARDS[data_key]
            if not data_file.endswith('*.tif'):
                print("Skipping non-raster file {data_file}")

            raster_error = False
            raster_info = pygeoprocessing.get_raster_info(data_file)
            if raster_info['nodata'][0] is None:
                print(f"{data_file} has no defined nodata")

            array = pygeoprocessing.raster_to_numpy_array(data_file)
            if numpy.sum(~numpy.isfinite(array)) > 0:
                raster_error = True
                print(f"{data_file} contains infinite values")

            if numpy.sum(numpy.isnan(array)):
                raster_error = True
                print(f"{data_file} contains nan values")

            n_rasters_with_errors += int(raster_error)

        print(f"{n_rasters_with_errors} rasters have data errors")
