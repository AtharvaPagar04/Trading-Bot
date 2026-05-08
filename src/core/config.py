from pathlib import Path

import yaml
from pydantic import BaseModel


class AppConfig(BaseModel):
    name: str
    mode: str


class TradingConfig(BaseModel):
    symbol: str
    timeframe: str


class RiskConfig(BaseModel):
    max_drawdown_pct: float
    max_open_grids: int


class FeeConfig(BaseModel):
    maker_fee_pct: float
    taker_fee_pct: float
    spread_pct: float


class Settings(BaseModel):
    app: AppConfig
    trading: TradingConfig
    risk: RiskConfig
    fees: FeeConfig


def load_settings() -> Settings:
    config_path = Path("config/settings.yaml")

    with open(config_path, "r") as file:
        raw_config = yaml.safe_load(file)

    return Settings(**raw_config)