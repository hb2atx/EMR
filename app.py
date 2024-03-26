from flask import Flask
from model import db, connect_db, Patients, Physicians, Visits, Vitals, CovidScreening, AdditionalQuestions, Wounds, Equipment, Treatment, SpecialTreatments

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///emr'

connect_db(app)

# Create the tables
with app.app_context():
    db.create_all()

