from functools import lru_cache

from app.core.config import settings
from app.db.session import get_session_factory
from app.repositories.base import AbstractPalletRepository
from app.repositories.demo_repository import DemoPalletRepository
from app.repositories.postgres_repository import PostgresPalletRepository


@lru_cache
def get_repository() -> AbstractPalletRepository:
    session_factory = get_session_factory()
    if settings.database_enabled and session_factory is not None:
        return PostgresPalletRepository(session_factory)
    return DemoPalletRepository()
