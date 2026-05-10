def exceeds_position_limit(
    position_size: float,
    max_position_size: float,
):

    return (
        position_size
        >
        max_position_size
    )
