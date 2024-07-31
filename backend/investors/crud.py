from typing import Generic, TypeVar
from marshmallow import Schema
from investors.models import Investor

ModelType = TypeVar("ModelType", bound=Schema)

class CRUDBase(Generic[ModelType]):
    """Base class for CRUD operations on a SQLAlchemy model."""
    def __init__(self, model: ModelType):
        self.model = model

    def get(self, session, id: int):
        """Get a single record by ID"""
        return session.query(self.model).filter(self.model.id == id).first()
    
crud_investor = CRUDBase(Investor)