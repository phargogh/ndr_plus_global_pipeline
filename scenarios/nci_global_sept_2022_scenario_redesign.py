"""NCI Global NDR Scenarios.

These 8+baseline scenarios were reworked/created in late August, early
September 2022.
"""
import logging
import os
import sys
import tempfile

import numpy
import pygeoprocessing

sys.path.append(os.getcwd())

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)
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
try:
    if sys.argv[1] != '--check':
        for key, value in ECOSHARDS.items():
            if value.startswith(SHERLOCK_SCRATCH):
                assert os.path.exists(value), f'File not found: {value}'
except IndexError:
    # When index not in list
    pass

# put IDs here that need to be scrubbed, you may know these a priori or you
# may run the pipeline and see an error and realize you need to add them
SCRUB_IDS = {
    'current_bmp_n_app',
    'current_lulc_masked_n_app',
    'extensification_current_practices_bmp_n_app',
    'extensification_current_practices_n_app',
    'intensification_bmp_n_app',
    'intensification_expansion_bmp_n_app',
    'intensification_expansion_n_app',
    'intensification_n_app',
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


def detect_invalid_values(base_raster_path, rtol=0.001, max_abs=1e30):
    """Return error if an invalid value is found in the raster.

    A return value of errors are raised if there are any non-finite values, any
    values that are close to nodata but not equal to nodata, or any values that
    are just really big. If none of these are true then the function returns
    ``True``.
    """
    numpy.set_printoptions(precision=15)
    base_nodata = pygeoprocessing.get_raster_info(
        base_raster_path)['nodata'][0]
    for _, block_array in pygeoprocessing.iterblocks((base_raster_path, 1)):
        non_finite_mask = ~numpy.isfinite(block_array)
        if non_finite_mask.any():
            return (
                f'found some non-finite values in {base_raster_path}: '
                f'{block_array[non_finite_mask]}')
        if base_nodata is not None:
            close_to_nodata_mask = numpy.isclose(
                block_array, base_nodata, rtol=rtol) & ~numpy.isclose(
                block_array, base_nodata)
            if close_to_nodata_mask.any():
                return (
                    f'found some values that are close to nodata {base_nodata} '
                    f'but not equal to '
                    f'nodata in {base_raster_path}: '
                    f'{block_array[close_to_nodata_mask]}')

        large_value_mask = (numpy.abs(block_array) >= max_abs)
        if base_nodata is not None:
            large_value_mask &= ~numpy.isclose(block_array, base_nodata)
        if large_value_mask.any():
            return (
                f'found some very large values not close to {base_nodata} in '
                f'{base_raster_path}: {block_array[large_value_mask]}')

    return True


def scrub_raster(
        base_raster_path, target_raster_path, target_nodata=None,
        rtol=0.001, max_abs=1e30):
    """Scrub invalid values from base.

    Will search base raster for difficult values like NaN, +-inf, Very Large
    values that may indicate a roundoff error when being compared to nodata.

    Args:
        base_raster_path (str): path to base raster
        target_raster_path (str): path to raster created by this call with
            invalid values 'scrubbed'.
        target_nodata (numeric): if `None` then the nodata value is copied
            from base, otherwise it is set to this value.
        rtol (float): relative tolerance to use when comparing values with
            nodata. Default is set to 1-3.4e38/float32.min.
        max_abs (float): the maximum absolute value to expect in the raster
            anything larger than this will be set to nodata. Defaults to
            1e30.

    Return:
        None
    """
    LOGGER.debug(f'scrubbing {base_raster_path}')
    if (os.path.exists(target_raster_path) and
            os.path.samefile(base_raster_path, target_raster_path)):
        raise ValueError(
            f'{base_raster_path} and {target_raster_path} are the same file')
    base_raster_info = pygeoprocessing.get_raster_info(base_raster_path)
    base_nodata = base_raster_info['nodata'][0]
    if base_nodata is None and target_nodata is None:
        raise ValueError('value base and target nodata are both None')
    if (base_nodata is not None and
            target_nodata is not None and
            base_nodata != target_nodata):
        raise ValueError(
            f'base raster at {base_raster_path} has a defined nodata '
            f'value of {base_nodata} and also a requested '
            f'target {target_nodata} value')
    if target_nodata is None:
        scrub_nodata = base_nodata
    else:
        scrub_nodata = target_nodata

    non_finite_count = 0
    nan_count = 0
    large_value_count = 0
    close_to_nodata = 0

    def _scrub_op(base_array):
        nonlocal non_finite_count
        nonlocal nan_count
        nonlocal large_value_count
        nonlocal close_to_nodata

        result = numpy.copy(base_array)
        non_finite_mask = ~numpy.isfinite(result)
        non_finite_count += numpy.count_nonzero(non_finite_mask)
        result[non_finite_mask] = scrub_nodata

        nan_mask = numpy.isnan(result)
        nan_count += numpy.count_nonzero(nan_mask)
        result[nan_mask] = scrub_nodata

        large_value_mask = numpy.abs(result) >= max_abs
        large_value_count += numpy.count_nonzero(large_value_mask)
        result[large_value_mask] = scrub_nodata

        close_to_nodata_mask = numpy.isclose(
            result, scrub_nodata, rtol=rtol)
        close_to_nodata += numpy.count_nonzero(close_to_nodata_mask)
        result[close_to_nodata_mask] = scrub_nodata
        return result

    LOGGER.debug(
        f'starting raster_calculator op for scrubbing {base_raster_path}')
    pygeoprocessing.raster_calculator(
        [(base_raster_path, 1)], _scrub_op, target_raster_path,
        base_raster_info['datatype'], scrub_nodata)

    if any([non_finite_count, large_value_count, close_to_nodata]):
        LOGGER.warning(
            f'{base_raster_path} scrubbed these values:\n'
            f'\n\tnon_finite_count: {non_finite_count}'
            f'\n\tnan_count: {nan_count}'
            f'\n\tlarge_value_count: {large_value_count}'
            f'\n\tclose_to_nodata: {close_to_nodata} '
            f'\n\tto the nodata value of: {scrub_nodata}')
    else:
        LOGGER.info(f'{base_raster_path} is CLEAN')


if __name__ == '__main__':
    if sys.argv[1] == '--check':
        keys_to_check = set()
        for data_dict in SCENARIOS.values():
            for data_key in data_dict.values():
                keys_to_check.add(data_key)

        rasters_with_errors_to_try_scrubbing = set()

        n_rasters_with_errors = 0
        for data_key in sorted(keys_to_check):
            data_file = ECOSHARDS[data_key]
            if not data_file.endswith('.tif'):
                print(f"Skipping non-raster file {data_file}")
                continue

            # skip non-n_app rasters for now.
            if 'n_app' not in data_file:
                continue

            if not os.path.exists(data_file):
                print(f"File not found: {data_file}")
                continue

            print(f"Checking {data_file}")
            errors_present = detect_invalid_values(
                data_file)
            if errors_present is not True:
                print(f"ERRORS in {data_file}")
                print(errors_present)
                rasters_with_errors_to_try_scrubbing.add(data_file)

        # if no errors found in rasters, exit.
        if not rasters_with_errors_to_try_scrubbing:
            sys.exit(0)

        print("\nSeeing if scrubbing fixes errors encountered")
        # try scrubbing the rasters and see if that fixes the issue
        scrubbed_dir = tempfile.mkdtemp(prefix='scrubdir-', dir=os.getcwd())
        for data_file in rasters_with_errors_to_try_scrubbing:
            scrubbed_path = os.path.join(scrubbed_dir,
                                         os.path.basename(data_file))
            raster_info = pygeoprocessing.get_raster_info(data_file)
            if raster_info['nodata'][0] is not None:
                print(f"{data_file}: using existing nodata value")
                nodata = raster_info['nodata'][0]
            else:
                nodata = float(numpy.finfo(numpy.float32).min)

            scrub_raster( data_file, scrubbed_path, target_nodata=nodata)

            errors_present = detect_invalid_values(
                scrubbed_path)
            if errors_present is not True:
                print(f"Could not scrub file {data_file}:")
                print(errors_present)
