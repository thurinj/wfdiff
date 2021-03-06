#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test suite for the wfdiff visualizations.

Run with pytest.

:copyright:
    Lion Krischer (krischer@geophysik.uni-muenchen.de), 2015
:license:
    GNU General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""
import inspect
import matplotlib.pyplot as plt
from matplotlib.testing.compare import compare_images as mpl_compare_images
import os


# Most generic way to get the data folder path.
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe()))), "data")

# Baseline images for the plotting test.
IMAGE_DIR = os.path.join(os.path.dirname(DATA_DIR), "baseline_images")


def reset_matplotlib():
    """
    Reset matplotlib to a common default.
    """
    # Force agg backend.
    plt.switch_backend('agg')
    import locale
    locale.setlocale(locale.LC_ALL, str('en_US.UTF-8'))


reset_matplotlib()


def images_are_identical(image_name, temp_dir, dpi=None):
    """
    Partially copied from ObsPy. Used to check images for equality.
    """
    image_name += os.path.extsep + "png"
    expected = os.path.join(IMAGE_DIR, image_name)
    actual = os.path.join(temp_dir, image_name)

    if dpi:
        plt.savefig(actual, dpi=dpi)
    else:
        plt.savefig(actual)
    plt.close()

    assert os.path.exists(expected)
    assert os.path.exists(actual)

    print(actual)

    # Use a reasonably high tolerance to get around difference with different
    # freetype and possibly agg versions. matplotlib uses a tolerance of 13.
    result = mpl_compare_images(expected, actual, 5, in_decorator=True)
    if result is not None:
        print(result)
    assert result is None
