from app.repositories.demo_repository import DemoPalletRepository
from app.services.repository_factory import get_repository


def test_repository_falls_back_to_demo_when_database_is_not_configured():
    get_repository.cache_clear()
    repository = get_repository()
    assert isinstance(repository, DemoPalletRepository)
