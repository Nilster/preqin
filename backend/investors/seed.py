# from investors.models import Investor
import click
from flask.cli import with_appcontext
from investors.app import db
import pandas as pd
from pathlib import Path
from investors.models import Investor, InvestoryTypeEnum, AssetClassEnum
from investors.crud import crud_investor, crud_commitment

def seed_data():
    """Load the data from csv file into the database"""
    csv_path = Path(__file__).parent.joinpath("data", "data.csv")
    df = pd.read_csv(csv_path, parse_dates=["Investor Date Added", "Investor Last Updated"])
    #Following are the unique properties of an investor
    group_by_investors = df.groupby(["Investor Name", "Investory Type", "Investor Country", "Investor Date Added", "Investor Last Updated"])
    #Iterate over each sample investor and their commitments
    for investor_info, commitment_info in group_by_investors:
        investor_data = {
            "name": investor_info[0],
            "investory_type": InvestoryTypeEnum(investor_info[1]),
            "address": investor_info[2],
            "created_at": investor_info[3],
            "updated_at": investor_info[4]
        }
        investor_db = crud_investor.create_without_commit(db.session, investor_data)

        for _, commitment in commitment_info.iterrows():
            commitment_data = {
                "investor_id": investor_db.id,
                "asset_class": AssetClassEnum(commitment["Commitment Asset Class"]),
                "amount": commitment["Commitment Amount"]
            }
            commitment_db = crud_commitment.create_without_commit(db.session, commitment_data)

    #Commit the data to the database if everything is successful
    db.session.commit()

@click.command("seed-data")
@with_appcontext
def load_csv():
    """Seed the database from csv file"""
    seed_data()