from src.core.session_builder import (
    create_trading_session,
)

session = create_trading_session(
    starting_capital=2000
)

print(session)