"""
Numerical constants.
"""

from enum import Enum
from typing import Optional

import numpy

from .paths import SolidEarthModelPart


class Direction(Enum):
    """
    Love numbers directions.
    """

    VERTICAL = 0
    TANGENTIAL = 1
    POTENTIAL = 2


class BoundaryCondition(Enum):
    """
    Love numbers boundary conditions.
    """

    LOAD = 0
    SHEAR = 1
    POTENTIAL = 2


# Earth mean radius (m).
EARTH_RADIUS = 6.371e6


# Default hyper parameters.
DEFAULT_MODELS: dict[Optional[SolidEarthModelPart], Optional[str]] = {
    SolidEarthModelPart.ELASTICITY: "PREM",
    SolidEarthModelPart.LONG_TERM_ANELASTICITY: "uniform",
    SolidEarthModelPart.SHORT_TERM_ANELASTICITY: "uniform",
    None: None,
}
DEFAULT_SPLINE_NUMBER = 10

# Other low level parameters.
ASYMPTOTIC_MU_RATIO_DECIMALS = 5
LAYER_DECIMALS = 5

# (cm/yr) -> (mm/yr).
GRACE_DATA_UNIT_FACTOR = 10

EMPIRICAL_INTERPOLATION_TIEMOUT_FACTOR = 5e3
