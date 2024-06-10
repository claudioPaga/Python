import numpy as np
from astropy.io import fits
import os

def cross_section(ctipixel_best_fit):
    """
    Derive the physical trap cross section from the best fit par in CtiPixel
    
    From equation in CtiPixel.java code:
        
    ctiPixel_Cross_Section * Ts = Ts * sigma * vth * SWFC^Beta/2Vg, where
    
    Ts = Serial transfer, 1E-7 s
    sigma = cross section in cm2 units
    vth = thermal velocity of electrons, 1.21E-7cm/s
    SFWC = Serial Full Well Capacity, 400k electrons
    Vg = Geometric volume of Gaia pixels, 2.25 E-10cm3
    
    The equation allows to derive sigma, the trap cross section in cm2.
    This is done in the calculation below
     
    Parameters:
    - ctipixel_best_fit: Best fit value from CtiPixel LMA fits
    """

    vth = 1.21E+7
    stime = 1.E-7
    sfwc = 400000.
    svg = 2.25E-10

    cross_section = 2.0 * ctipixel_best_fit  * svg / (vth * sfwc**0.5)

    print(f"Cross section = {cross_section:.3e} cm2")

    
    
cross_section(1000000)