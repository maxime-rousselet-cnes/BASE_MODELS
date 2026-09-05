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
MODELS = {"elastic": "PREM", "attenuation": "uniform", "transient": "reference", "viscous": "VM7"}
SOLID_EARTH_MODEL_PROFILES = DEFAULT_MODELS.keys()

# Contains both inputs and outputs.
DATA_PATH_TXT_PATH = Path("..")
ROOT_PATH = Path(
    "".join(
        (
            line.strip()
            for line in open(DATA_PATH_TXT_PATH.joinpath("data_path.txt"), "r").readlines()
        )
    )
)
DATA_PATH = ROOT_PATH.joinpath("common_data")
TEST_PATH = DATA_PATH.joinpath("tests")
FIGURES_PATH = DATA_PATH.joinpath("figures")
