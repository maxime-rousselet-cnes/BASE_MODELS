"""
Arborescence and common constants configuration.
"""

from enum import Enum
from pathlib import Path


class SolidEarthModelPart(Enum):
    """
    Available model parts.
    """

    ATTENUATION = "attenuation"
    ELASTIC = "elastic"
    TRANSIENT = "transient"
    VISCOUS = "viscous"


DEFAULT_MODELS = {
    "elastic": "PREM",
    "attenuation": "uniform",
    "transient": "reference",
    "viscous": "uniform",
}
MODELS = {"elastic": "PREM", "attenuation": "Resovsky", "transient": "reference", "viscous": "VM7"}
SOLID_EARTH_MODEL_PROFILES = DEFAULT_MODELS.keys()

# Contains both inputs and outputs.
DATA_PATH = Path("../common_data")
DEFAULT_WORKDIR = DATA_PATH.parent.joinpath("alna")

## Tests.
TEST_PATH = DATA_PATH.joinpath("tests")

### Test figures.
TEST_FIGURES_PATH = TEST_PATH.joinpath("figures")

## Inputs.
INPUTS_PATH = DATA_PATH.joinpath("inputs")

## Love numbers.
LOVE_NUMBERS_PATH = DATA_PATH.joinpath("love_numbers")
LOVE_NUMBERS_FOR_GINS_PATH = LOVE_NUMBERS_PATH.joinpath("for_gins")
