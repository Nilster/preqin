from investors.app import db
from datetime import datetime, timezone
import enum

class InvestoryTypeEnum(enum.Enum):
    ASSET_MANAGER = "asset manager"
    BANK = "bank"
    FUND_MANAGER = "fund manager"
    WEALTH_MANAGER = "wealth manager"

class AssetClassEnum(enum.Enum):
    HEDGE_FUNDS = "Hedge Funds"
    INFRASTRUCTURE = "Infrastructure"
    NATURAL_RESOURCES = "Natural Resources"
    PRIVATE_DEBT = "Private Debt"
    PRIVATE_EQUITY = "Private Equity"
    REAL_ESTATE = "Real Estate"

class Investor(db.Model):
    __tablename__ = 'investors'
    __table_args__ = {
        "info": {"alembic_key": "investments"}
    }

    id = db.Column(db.Integer, primary_key=True)
    investory_type = db.Column(db.Enum(InvestoryTypeEnum), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False, onupdate=datetime.now(timezone.utc))

class Commitment(db.Model):
    __tablename__ = 'commitments'

    id = db.Column(db.Integer, primary_key=True)
    investor_id = db.Column(db.Integer, db.ForeignKey('investors.id'), nullable=False)
    asset_class = db.Column(db.Enum(AssetClassEnum), nullable=False)
    amount = db.Column(db.Integer, nullable=False) # Assuming amount in GBP
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False, onupdate=datetime.now(timezone.utc))