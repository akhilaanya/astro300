#Akhila Anya Pisupati
#ASTR 300 HW Gaia Data
#Jan 20, 2026

import numpy as np
from astropy.table import QTable
from astroquery.gaia import Gaia

query_circle = """
SELECT TOP 1000
source_id, ra, dec, phot_g_mean_mag, parallax, bp_rp
FROM gaiadr3.gaia_source.lite
WHERE DISTANCE ( POINT(291.79, -26.95), POINT (ra, dec) ) < 1
AND phot_g_mean_mag < 14.0
AND parallax > 1
AND bp_rp IS NOT NULL
ORDER BY bp_rp ASC
"""
print(query_circle)
