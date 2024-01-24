# Diving deeper into Strong Gravitational Lensing with cGANs 

[![DOI](https://zenodo.org/badge/690453944.svg)](https://zenodo.org/badge/latestdoi/690453944)

Supporting materials for Euclid strong lensing working group meeting Bologna February 2024.
This repository contains notebooks and additional files for getting filter response curves for JWST NIRcam imaging, simulating strong gravitational lenses for JWST and Euclid observation configuration and the source code for the cGAN. Each notebook gives a walkthrough and detailed explanation of how to use the code provided. 

## Data Preparation for the cGAN
The strong gravitational lenses dataset was simulated using lenstronomy: [here](https://lenstronomy.readthedocs.io/en/latest/). Note that only NIRcam F200W and F356W are supported by lenstronomy in the observation configuration file for JWST. To simulate strong gravitational lenses as observed by JWST NIRcam, you will have to use:

> JWST_Config.py

To simulate the strong gravitational lenses as observed by both JWST NIRcam and Euclid-VIS, Euclid-NISP, you can follow:

This returns the simulated lenses with a *.fits* extension of size 64x64. More information is given in the notebook.

## The Network
<img width="560" alt="image" src="https://github.com/RubyPC/Anomaly_Detection_with_cGANs/assets/106536925/cf6becbd-7dd4-4ae7-87d6-39ab19fa8e7a">

To use the cGAN, follow:

> cGANs_JWST.ipynb

The data fed to the cGAN is loaded from each individual waveband file.

## Results after Training
The cGAN predicts the strong gravitational lenses as observed by the long wavelength filters of JWST NIRcam to a high accuracy. We also test whether the cGAN can predict long wavelength JWST NIRcam data from Euclid-VIS and Euclid-NISP data. Below shows examples of results produced by the network.
<img width="441" alt="Output1" src="https://github.com/RubyPC/cGAN_Strong_Lensing/assets/106536925/987a46a9-b18d-478c-81b1-6e322da04c74">

Further results showing each individual filter prediction and Euclid to JWST predictions are given in the cGAN jupyter notebook.

## Some Useful Links
* [JWST User Documentation](https://jwst-docs.stsci.edu/)
* [JWST NIRcam Imaging Information](https://jwst-docs.stsci.edu/jwst-near-infrared-camera)
* [Euclid Red Book](https://arxiv.org/abs/1110.3193)
* [Euclid VIS and NISP Insruments](https://www.euclid-ec.org/public/mission/vis/)

### References
* [Lenstronomy](https://arxiv.org/abs/1803.09746)
* [Detecting Strong Gravitational Lenses with CNNs](https://arxiv.org/abs/2202.127760)
* [Image-to-Image Translation with conditionl Adversarial Networks](https://doi.org/10.48550/arXiv.1611.07004)
* [Generative Adversarial Networks](https://doi.org/10.48550/arXiv.1406.2661)
* [Using cGANs for Anomaly Detection in JWST Imaging](https://arxiv.org/abs/2310.09073)
