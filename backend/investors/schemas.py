from investors.app import ma
from investors.models import Investor, InvestoryTypeEnum
from investors.models import Commitment, AssetClassEnum
from marshmallow import fields
from marshmallow_sqlalchemy import auto_field

class InvestorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Investor

    id = auto_field(dump_only=True)
    investory_type = fields.Enum(InvestoryTypeEnum, by_value=True)
    total_commitment = fields.Integer(dump_only=True, required=True)

class InvestorsSchema(ma.Schema):
    investors = fields.Nested(InvestorSchema, many=True)

class InvestorIdSchema(ma.Schema):
    investor_id = fields.Integer(required=True)

class CommitmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Commitment
        remove_fields = ["investor_id"]

    id = auto_field(dump_only=True)
    asset_class = fields.Enum(AssetClassEnum, by_value=True)
    amount = fields.Integer(required=True)
    currency = fields.String(required=True, default="GBP")

class AssetClassCommitmentSchema(ma.Schema):
    class_total = fields.Integer(required=True)
    commitments = fields.Nested(CommitmentSchema, many=True)

class CommitmentSummarySchema(ma.Schema):
    investor_id = fields.Integer(required=True)
    total_commitment = fields.Integer(required=True)
    hedge_funds = fields.Nested(AssetClassCommitmentSchema, required=True)
    private_equity = fields.Nested(AssetClassCommitmentSchema, required=True)
    real_estate = fields.Nested(AssetClassCommitmentSchema, required=True)
    infrastructure = fields.Nested(AssetClassCommitmentSchema, required=True)
    natural_resources = fields.Nested(AssetClassCommitmentSchema, required=True)

investors_schema = InvestorsSchema()
investor_id_schema = InvestorIdSchema()
commitment_summary_schema = CommitmentSummarySchema()