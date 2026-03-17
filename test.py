"""
To test the package. To be called by pytest test.py.
"""

from math import erf
from typing import Optional

from numpy import array, exp, pi
from sympy import Matrix, flatten, lambdify, symbols

from base_models import (
    TEST_PATH,
    adaptive_runge_kutta_45,
    evaluate_terminal_parameters,
    fixed_timestep_integrator,
    load_base_model,
    load_complex_array,
    partial_symbols,
    save_base_model,
    save_complex_array,
    vector_variation_equation,
)

SAVE_CONSISTENCY_TOLERANCE = 1e-10
TEST_TERMINAL_PARAMETER_VALUES = {
    r"t_1": 1.0,
    r"a": 2.0,
    r"b": 3.0,
    r"y_1_0": 1.0,
    r"y_2_0": 1.0,
    r"dt": 1e-4,
}
NUMERICAL_CONSISTENCY_TOLERANCE = 1e-5


def test_save_and_load_base_model(file_name: str = "save_base_model_test_file") -> None:
    """
    Saves a base model in a (.JSON) file and verifies oconsistency when loading.
    """

    obj = {
        "a": 1,
        "b": "test",
        "c": [1, 2, 3],
    }

    save_base_model(obj=obj, name=file_name, path=TEST_PATH)
    loaded_obj = load_base_model(name=file_name, path=TEST_PATH)

    assert obj == loaded_obj


def test_save_and_load_complex_array(
    file_name: str = "save_complex_array_test_file", tolerance: float = SAVE_CONSISTENCY_TOLERANCE
) -> None:
    """
    Saves a complex array in a (.JSON) file and verifies oconsistency when loading.
    """

    obj = array([1.0 + 2.0j, 3.0 + 4.0j], dtype=complex)

    save_complex_array(obj=obj, name=file_name, path=TEST_PATH)
    loaded_obj = load_complex_array(name=file_name, path=TEST_PATH)

    assert sum(abs(obj - loaded_obj)) < tolerance


def test_variation_equation_integration(
    values: Optional[dict[str, float]] = None,
    tolerance: float = NUMERICAL_CONSISTENCY_TOLERANCE,
) -> None:
    """
    Integrates the partial derivatives of a system of known solutions and verifies consistency with
    the analytical solution.
    The system is deliberately chosen as simple as possible while being non-linear and
    non-autonomous to test the generality of the implementation.
    """

    if values is None:

        values = TEST_TERMINAL_PARAMETER_VALUES

    t_variable, a, b = symbols(r"t a b")
    state_vector_line = list(symbols(r"y_1 y_2"))
    generalized_symbolic_propagator = Matrix(
        [
            -a * t_variable * state_vector_line[0] + state_vector_line[0] * state_vector_line[1],
            -b * t_variable * state_vector_line[1],
        ]
    )
    t, y = adaptive_runge_kutta_45(
        fun=lambdify(
            args=[t_variable, state_vector_line],
            expr=flatten(
                evaluate_terminal_parameters(
                    expression=generalized_symbolic_propagator,
                    parameter_expressions={r"a": a, r"b": b},
                    terminal_parameter_values={
                        r"a": values[r"a"],
                        r"b": values[r"b"],
                    },
                ),
            ),
        ),
        t_bounds=(0.0, values[r"t_1"], values[r"dt"]),
        y_0=array(object=[values[r"y_1_0"], values[r"y_2_0"]]),
    )

    for i_parameter, parameter in enumerate([a, b]):

        partials, partials_matrix_for_parameter = partial_symbols(
            parameter=parameter, state_vector_line=state_vector_line
        )
        variation_equations = evaluate_terminal_parameters(
            expression=vector_variation_equation(
                dynamic=generalized_symbolic_propagator,
                parameter=parameter,
                partials=partials_matrix_for_parameter,
                state_vector_line=state_vector_line,
            ),
            parameter_expressions={r"a": a, r"b": b},
            terminal_parameter_values={
                r"a": values[r"a"],
                r"b": values[r"b"],
            },
        )
        numerical_partials = fixed_timestep_integrator(
            fun=lambdify(
                args=[t_variable, state_vector_line, partials],
                expr=flatten(variation_equations),
            ),
            t=t,
            y=y,
            system_dimension=2,
        ).T

        # Verifies \frac{\partial y_1}{\partial a} and \frac{\partial y_2}{\partial b}.
        assert (
            (sum((numerical_partials[i_parameter] + (t**2) / 2 * y[:, i_parameter]) ** 2) / len(t))
            ** 0.5
        ) < tolerance

    # Verifies the RK45 with adaptive step.
    assert (
        sum(
            (
                y[:, 0]
                - values[r"y_1_0"]
                * exp(
                    -values[r"a"] * t**2 / 2
                    + values[r"y_2_0"]
                    * (pi / (2 * values[r"b"])) ** 0.5
                    * array(
                        object=[erf((values[r"b"] / 2) ** 0.5 * time_scalar) for time_scalar in t]
                    )
                )
            )
            ** 2
        )
        / (2 * len(t))
    ) ** 0.5 < tolerance
    assert (
        sum((y[:, 1] - values[r"y_2_0"] * exp(-values[r"b"] * t**2 / 2)) ** 2) / (2 * len(t))
    ) ** 0.5 < tolerance
