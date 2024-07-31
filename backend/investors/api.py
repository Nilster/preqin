from flask import Blueprint
from apifairy import other_responses
from investors.crud import crud_investor

homepage_blueprint = Blueprint('homepage', __name__)

@homepage_blueprint.route('/test', methods=['GET'])
@other_responses({200: {"description": "Welcome to the homepage"}})
def homepage():
    return {"home": "Welcome to the homepage"}