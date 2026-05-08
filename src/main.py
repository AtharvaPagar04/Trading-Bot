import typer

from src.core.config import load_settings
from src.utils.logger import get_logger

app = typer.Typer()

logger = get_logger()


@app.command()
def start():
    settings = load_settings()

    logger.info(
        "bot_initialized",
        app_name=settings.app.name,
        mode=settings.app.mode,
        symbol=settings.trading.symbol,
        timeframe=settings.trading.timeframe,
    )

    print("Grid Trading Bot v3 initialized successfully")


if __name__ == "__main__":
    app()