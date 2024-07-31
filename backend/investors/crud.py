from typing import Generic, TypeVar
from marshmallow import Schema
from investors.models import Investor, Commitment

ModelType = TypeVar("ModelType", bound=Schema)

class CRUDBase(Generic[ModelType]):
    """Base class for CRUD operations on a SQLAlchemy model."""
    def __init__(self, model: ModelType):
        self.model = model

    def get(self, session, id: int):
        """Get a single record by ID"""
        return session.query(self.model).filter(self.model.id == id).first()
    
    def create_without_commit(self, session, data: dict):
        """Create a new record"""
        instance = self.model(**data)
        session.add(instance)
        session.flush()
        return instance
    
crud_investor = CRUDBase(Investor)
crud_commitment = CRUDBase(Commitment)