from typing import Generic, TypeVar
from marshmallow import Schema
from investors.models import Investor, Commitment, AssetClassEnum

ModelType = TypeVar("ModelType", bound=Schema)

class CRUDBase(Generic[ModelType]):
    """Base class for CRUD operations on a SQLAlchemy model."""
    def __init__(self, model: ModelType):
        self.model = model

    def get(self, session, id: int):
        """Get a single record by ID"""
        return session.query(self.model).filter(self.model.id == id).first()
    
    def get_all(self, session):
        """Get all records"""
        return session.query(self.model).all()
    
    def create_without_commit(self, session, data: dict):
        """Create a new record"""
        instance = self.model(**data)
        session.add(instance)
        session.flush()
        return instance
    
class CRUDInvestor(CRUDBase):
    def get_commitment_summary(self, session, id: int):
        """Get the total commitment of an investor"""
        investor_summary = self.get(session, id)
        commitments = investor_summary.commitments

        asset_class_dict = {}
        for asset_class in AssetClassEnum:
            asset_class_dict[asset_class] = {"class_total": 0, "commitments": []}

        for commitment in commitments:
            asset_class_dict[commitment.asset_class]["class_total"] += commitment.amount
            asset_class_dict[commitment.asset_class]["commitments"].append(commitment)

        commitment_summary = {
            "investor_id": id,
            "total_commitment": investor_summary.total_commitment,
            "hedge_funds": asset_class_dict[AssetClassEnum.HEDGE_FUNDS],
            "private_equity": asset_class_dict[AssetClassEnum.PRIVATE_EQUITY],
            "real_estate": asset_class_dict[AssetClassEnum.REAL_ESTATE],
            "infrastructure": asset_class_dict[AssetClassEnum.INFRASTRUCTURE],
            "natural_resources": asset_class_dict[AssetClassEnum.NATURAL_RESOURCES]
        }

        return commitment_summary

crud_investor = CRUDInvestor(Investor)
crud_commitment = CRUDBase(Commitment)