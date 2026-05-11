from src.config.env_loader import (
    load_env_variable,
)


def test_env_loader_default():

    value = (
        load_env_variable(
            "NON_EXISTENT_KEY",
            "default",
        )
    )

    assert (
        value
        ==
        "default"
    )
