#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:22:56 2024

@author: ruby
"""

# =============================================================================
# Creating JWST NIRcam filters to pass to the speclite module to compute the
# apparent magnitudes of blue and red galaxies to use as the lensing galaxy
# =============================================================================

# usual imports
import numpy as np
import matplotlib.pyplot as plt
import astropy
import speclite as sl
import astropy.units as u
from speclite import filters

# let's list all the filter included with speclite to check for JWST filters

all_filters = sl.filters.filter_group_names
#print(all_filters)

# JWST NIRcam filters are not included so we have to create our own filters

# we'll create a new filter group called 'NIRcam' with specified band names
# for each filter
# data for each filter taken from http://svo2.cab.inta-csic.es/svo/theory/fps3/index.php?id=JWST/NIRCam.F444W

# GET BANDS
# wavelength is: min, centre, pivot, peak, max
NIRcam_F115W = sl.filters.FilterResponse(
    wavelength=[9975.60, 11494.31, 11623.88, 12652.00, 13058.40] * u.Angstrom,
    response = [0, 0.30, 0.32, 0.39, 0], meta=dict(group_name='NIRcam', band_name='F115W'))

NIRcam_F150W = sl.filters.FilterResponse(
    wavelength = [13041.19, 15007.44, 15010.69, 16547.90, 16948.89] * u.Angstrom,
    response =[0, 0.42, 0.425, 0.46, 0], meta=dict(group_name='NIRcam', band_name='F150W'))

NIRcam_F200W = sl.filters.FilterResponse(
    wavelength = [17249.08, 19886.48, 19920.76, 22044.00, 22596.64] * u.Angstrom,
    response = [0, 0.45, 0.457, 0.475, 0], meta=dict(group_name='NIRcam', band_name='F200W'))

NIRcam_F277W = sl.filters.FilterResponse(
    wavelength = [23673.12, 27617.40, 27762.83, 28991.30, 32203.22] * u.Angstrom,
    response = [0, 0.40, 0.405, 0.41, 0], meta=dict(group_name='NIRcam', band_name='F277W'))

NIRcam_F356W = sl.filters.FilterResponse(
    wavelength=[30732.91, 35652.16, 35683.62, 38604.70, 40801.26] * u.Angstrom,
    response = [0, 0.45, 0.455, 0.5, 0], meta=dict(group_name='NIRcam', band_name='F356W'))

NIRcam_F444W = sl.filters.FilterResponse(
    wavelength = [38039.57, 43523.20, 44043.15, 44405.49, 50995.50] * u.Angstrom,
    response = [0, 0.5, 0.47, 0.45, 0], meta=dict(group_name='NIRcam', band_name='F444W'))

# we can now load these filters using 'NIRcam-*'
NIRcam = sl.filters.load_filters('NIRcam-F115W', 'NIRcam-F150W', 'NIRcam-F200W', 'NIRcam-F277W', 'NIRcam-F356W', 'NIRcam-F444W')
sl.filters.plot_filters(NIRcam) 

# now we can save those filters in the correct format to any directory
dir_name = '/Users/ruby/Documents/Python Scripts/cGAN/Euclid-JWST/FilterInformation/'
f115w_name = NIRcam_F115W.save(dir_name)
f150w_name = NIRcam_F150W.save(dir_name)
f200w_name = NIRcam_F200W.save(dir_name)
f277w_name = NIRcam_F277W.save(dir_name)
f356w_name = NIRcam_F356W.save(dir_name)
f444w_name = NIRcam_F444W.save(dir_name)
# these filters should be saved with an 'ecsv' extension 

euclid = sl.filters.load_filters('Euclid-VIS', 'Euclid-Y', 'Euclid-H', 'Euclid-J')
sl.filters.plot_filters(euclid)
#%%
import os
# let's try and load these custom filters
f115w_n = os.path.join(dir_name, 'NIRcam-F115W.ecsv')
f150w_n = os.path.join(dir_name, 'NIRcam-F150W.ecsv')
f200w_n = os.path.join(dir_name, 'NIRcam-F200W.ecsv')
f277w_n = os.path.join(dir_name, 'NIRcam-F277W.ecsv')
f356w_n = os.path.join(dir_name, 'NIRcam-F356W.ecsv')
f444w_n = os.path.join(dir_name, 'NIRcam-F444W.ecsv')

# and pass to speclite to 'load_filters'
nircam_f115w = sl.filters.load_filter(f115w_n)
nircam_f150w = sl.filters.load_filter(f150w_n)
nircam_f200w = sl.filters.load_filter(f200w_n)
nircam_f277w = sl.filters.load_filter(f277w_n)
nircam_f356w = sl.filters.load_filter(f356w_n)
nircam_f444w = sl.filters.load_filter(f444w_n)


# works- pass this to speclite.kcorrect to get apparent magnitudes for lens galaxy










