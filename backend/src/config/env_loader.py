import os


def load_env_variable(
    key: str,
    default=None,
):

    return os.getenv(
        key,
        default,
    )
