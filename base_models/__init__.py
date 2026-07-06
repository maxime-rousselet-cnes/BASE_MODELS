"""
Base models library needed for a few scientific computing libraries.
"""

from enum import Enum

from numpy import linspace, logspace

from .database import load_base_model, load_complex_array, save_base_model, save_complex_array
from .paths import (
    DATA_PATH,
    DEFAULT_MODELS,
    DEFAULT_WORKDIR,
    LOVE_NUMBERS_PATH,
    SOLID_EARTH_MODEL_PROFILES,
    TEST_FIGURES_PATH,
    TEST_PATH,
    SolidEarthModelPart,
)
from .runge_kutta_scheme import adaptive_runge_kutta_45, non_adaptive_runge_kutta_45
from .signal import SteadyStateSignalParameters, build_steady_state_regime_signal, lagrange_order4
from .symbolic import (
    evaluate_terminal_parameters,
    fixed_timestep_integrator,
    partial_symbols,
    variation_equation,
    vector_variation_equation,
)

LOCAL_MODE = True
N_LOVE_NUMBERS_FOR_GINS = 2 if LOCAL_MODE else 10
N_PARTIAL_TESTS = 2 if LOCAL_MODE else 101
N_PERIODS_VISCOUS_INTEGRATION_TEST = 2 if LOCAL_MODE else 30
TEST_VISCOUS_PERIOD_TAB = logspace(
    -3, 5, num=N_PERIODS_VISCOUS_INTEGRATION_TEST, base=10
)  # (yr), from sub-daily to 100 kyr.
TEST_ETA_TAB = linspace(start=1e18, stop=1e19, num=N_PARTIAL_TESTS)
TEST_ALPHA_TAB = linspace(start=0.2, stop=0.3, num=N_PARTIAL_TESTS)
TEST_RHO_TAB = linspace(start=7000, stop=9000, num=N_PARTIAL_TESTS)
TEST_DELTA_TAB = linspace(start=4.0, stop=15.0, num=N_PARTIAL_TESTS)

LOVE_NUMBERS_FOR_GINS_PATH = LOVE_NUMBERS_PATH.joinpath("for_gins")
LOVE_NUMBERS_FOR_GINS_TABS = {
    "degrees": [2],
    "periods": logspace(start=-2, stop=4, num=4 * N_LOVE_NUMBERS_FOR_GINS, base=10),  # (yr).
    "alpha": linspace(start=0.15, stop=0.3, num=N_LOVE_NUMBERS_FOR_GINS),
    "Delta": logspace(start=-2, stop=1, num=10, base=N_LOVE_NUMBERS_FOR_GINS),
    "tau_m": (1 / 3.09e-4)
    * logspace(start=-1, stop=1, num=10, base=N_LOVE_NUMBERS_FOR_GINS),  # (s).
}
MODELS = {"elastic": "PREM", "attenuation": "Resovsky", "transient": "reference", "viscous": "VM7"}


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

to_import = [
    load_base_model,
    load_complex_array,
    save_base_model,
    save_complex_array,
    DATA_PATH,
    DEFAULT_MODELS,
    LOVE_NUMBERS_PATH,
    SOLID_EARTH_MODEL_PROFILES,
    TEST_FIGURES_PATH,
    TEST_PATH,
    SolidEarthModelPart,
    adaptive_runge_kutta_45,
    non_adaptive_runge_kutta_45,
    SteadyStateSignalParameters,
    build_steady_state_regime_signal,
    lagrange_order4,
    evaluate_terminal_parameters,
    fixed_timestep_integrator,
    partial_symbols,
    variation_equation,
    vector_variation_equation,
    DEFAULT_WORKDIR,
]
