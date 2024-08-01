from flask import Blueprint
from apifairy import response, other_responses, arguments
from investors.crud import crud_investor
from investors.schemas import investors_schema, investor_id_schema, commitment_summary_schema
from investors.app import db

investors_blueprint = Blueprint('Investors', __name__)

@investors_blueprint.route('/investors', methods=['GET'])
@response(investors_schema, status_code=200, description="Get information about the investors")
@other_responses({500: "Internal Server Error"})
def get_investors():
    """Get information about the investors"""
    investors = crud_investor.get_all(db.session)
    return {"investors": investors}

@investors_blueprint.route('/commitments', methods=['GET'])
@arguments(investor_id_schema)
@response(commitment_summary_schema, status_code=200, description="Get commitment breakdown of an investor")
@other_responses({500: "Internal Server Error"})
def get_commitments(args):
    """Get commitment summary and breakdown of an investor"""
    investor_commitments = crud_investor.get_commitment_summary(db.session, args['investor_id'])
    return investor_commitments