"""Base service class - abstract base for all services."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


class BaseService(ABC):
    """Abstract base service class."""

    @abstractmethod
    def create(self, **kwargs) -> Any:
        """Create a new entity."""
        pass

    @abstractmethod
    def get_by_id(self, entity_id: int) -> Optional[Any]:
        """Get entity by ID."""
        pass

    @abstractmethod
    def get_all(self) -> List[Any]:
        """Get all entities."""
        pass

    @abstractmethod
    def update(self, entity_id: int, **kwargs) -> Any:
        """Update an entity."""
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> bool:
        """Delete an entity."""
        pass

    @staticmethod
    def _validate_required_fields(data: Dict, required: List[str]) -> None:
        """Validate required fields in data."""
        missing = [field for field in required if field not in data or not data[field]]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")
