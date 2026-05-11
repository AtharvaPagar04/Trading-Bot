from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
)
from sqlalchemy.orm import (
    sessionmaker,
)

DATABASE_URL = (
    "sqlite:///data/trading_system.db"
)
engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(
    bind=engine,
)

Base = declarative_base()