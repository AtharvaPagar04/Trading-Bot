from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
)
from sqlalchemy.orm import (
    sessionmaker,
)

DATABASE_URL = (
    "sqlite:///trading_system.db"
)

engine = create_engine(
    DATABASE_URL,
    echo=False,
)

SessionLocal = sessionmaker(
    bind=engine,
)

Base = declarative_base()