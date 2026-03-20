"""
Arborescence and common constants configuration.
"""

from enum import Enum
from pathlib import Path


class SolidEarthModelPart(Enum):
    """
    Available model parts.
    """

    attenuation = "attenuation"
    elastic = "elastic"
    transient = "transient"
    viscous = "viscous"


DEFAULT_MODELS: dict[str, str] = {
    "elastic": "PREM",
    "attenuation": "Resovsky",
    "transient": "reference",
    "viscous": "VM7",
}
SOLID_EARTH_MODEL_PROFILES = DEFAULT_MODELS.keys()

# Contains both inputs and outputs.
DATA_PATH = Path("../common_data")

## Tests.
TEST_PATH = DATA_PATH.joinpath("tests")

## Inputs.
INPUTS_PATH = DATA_PATH.joinpath("inputs")

## Outputs.
OUTPUTS_PATH = DATA_PATH.joinpath("outputs")

### Love numbers.
LOVE_NUMBERS_PATH = OUTPUTS_PATH.joinpath("love_numbers")

### Parallel computing logs.
LOGS_PATH = OUTPUTS_PATH.joinpath("logs")


def get_love_numbers_subpath(model_id: str, n: int, period: float) -> Path:
    """
    Generates the path to save the y_i system integration results for a given model.
    """
    return (
        LOVE_NUMBERS_PATH.joinpath("INDIVIDUAL_LOVE_NUMBERS")
        .joinpath(model_id)
        .joinpath(str(n))
        .joinpath(str(period))
    )


def get_interpolated_love_numbers_subpath(periods_id: str, rheological_model_id: str) -> Path:
    """
    Gets the path for Love numbers of a given rheological model interpolated on given periods.
    """

    return (
        LOVE_NUMBERS_PATH.joinpath("INTERPOLATED_LOVE_NUMBERS")
        .joinpath(periods_id)
        .joinpath(rheological_model_id)
    )
