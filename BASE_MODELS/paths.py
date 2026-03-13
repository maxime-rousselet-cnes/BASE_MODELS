"""
Arborescence configuration.
"""

from pathlib import Path

solid_earth_model_profiles = ["elastic", "attenuation", "transient", "viscous"]

# Contains both inputs and outputs.
data_path = Path("../COMMON_DATA")

## Inputs.
inputs_path = data_path.joinpath("inputs")
### Solid Earth model descriptions.
solid_earth_model_profile_descriptions_root_path = inputs_path.joinpath(
    "solid_earth_model_profile_descriptions"
)
solid_earth_model_profile_descriptions_path: dict[str, Path] = {
    model_part: solid_earth_model_profile_descriptions_root_path.joinpath(model_part)
    for model_part in solid_earth_model_profiles
}

## Solid Earth numerical models.
solid_earth_numerical_models_root_path = data_path.joinpath("solid_earth_numerical_models")
solid_earth_numerical_models_path: dict[str, Path] = {
    model_part: solid_earth_numerical_models_root_path.joinpath(model_part)
    for model_part in solid_earth_model_profiles
}
solid_earth_full_numerical_models_path = solid_earth_numerical_models_root_path.joinpath(
    "solid_earth_full_numerical_models"
)

## Outputs.
outputs_path = data_path.joinpath("outputs")

### Love numbers.
love_numbers_path = outputs_path.joinpath("love_numbers")

### Parallel computing logs.
logs_path = outputs_path.joinpath("logs")


def get_love_numbers_subpath(model_id: str, n: int, period: float) -> Path:
    """
    Generates the path to save the y_i system integration results for a given model.
    """
    return (
        love_numbers_path.joinpath("individual_love_numbers")
        .joinpath(model_id)
        .joinpath(str(n))
        .joinpath(str(period))
    )


def get_interpolated_love_numbers_subpath(periods_id: str, rheological_model_id: str) -> Path:
    """
    Gets the path for Love numbers of a given rheological model interpolated on given periods.
    """

    return (
        love_numbers_path.joinpath("interpolated_love_numbers")
        .joinpath(periods_id)
        .joinpath(rheological_model_id)
    )
