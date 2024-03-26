from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    with app.app_context():
        db.app = app
        db.init_app(app)
        db.drop_all()
        db.create_all()


class Patients(db.Model):
    __tablename__ = 'patients'

    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address1 = db.Column(db.String(100))
    address2 = db.Column(db.String(100))
    age = db.Column(db.Integer)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10))
    insurance = db.Column(db.String(50))
    previous_patient = db.Column(db.Boolean)
    caregiver_name = db.Column(db.String(100))
    caregiver_phone = db.Column(db.String(20))
    caregiver_relationship = db.Column(db.String(50))
    spouse = db.Column(db.Boolean)
    spouse_phone = db.Column(db.String(20))

class Physicians(db.Model):
    __tablename__ = 'physicians'

    physician_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))

class Visits(db.Model):
    __tablename__ = 'visits'

    visit_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.patient_id'))
    physician_id = db.Column(db.Integer, db.ForeignKey('physicians.physician_id'))
    visit_start_time = db.Column(db.TIMESTAMP)
    visit_end_time = db.Column(db.TIMESTAMP)
    evaluation_date = db.Column(db.Date)

class Vitals(db.Model):
    __tablename__ = 'vitals'

    vital_id = db.Column(db.Integer, primary_key=True)
    visit_id = db.Column(db.Integer, db.ForeignKey('visits.visit_id'))
    temperature = db.Column(db.Float)
    pulse = db.Column(db.Integer)
    oxygen_saturation = db.Column(db.Integer)
    blood_pressure_systolic = db.Column(db.Integer)
    blood_pressure_diastolic = db.Column(db.Integer)
    respiratory_rate = db.Column(db.Integer)
    pain = db.Column(db.Integer)
    capillary_refill = db.Column(db.String(20))
    last_bowel_movement = db.Column(db.Date)
    lung_sounds = db.Column(db.String(100))
    pain_sleep = db.Column(db.Integer)
    pain_transfer_assist = db.Column(db.Integer)
    pain_daily_activities = db.Column(db.Integer)

class CovidScreening(db.Model):
    __tablename__ = 'covid_screening'

    screening_id = db.Column(db.Integer, primary_key=True)
    visit_id = db.Column(db.Integer, db.ForeignKey('visits.visit_id'))
    family_member_temperature = db.Column(db.Float)
    caregiver_temperature = db.Column(db.Float)
    covid_symptoms = db.Column(db.Boolean)
    covid_contact = db.Column(db.Boolean)
    covid_travel = db.Column(db.Boolean)

class AdditionalQuestions(db.Model):
    __tablename__ = 'additional_questions'

    question_id = db.Column(db.Integer, primary_key=True)
    visit_id = db.Column(db.Integer, db.ForeignKey('visits.visit_id'))
    cpap_usage = db.Column(db.Boolean)
    incontinence_level = db.Column(db.Integer)
    catheter_type = db.Column(db.String(20))
    catheter_changed = db.Column(db.Date)
    cognitive_impairment = db.Column(db.Boolean)
    anxiety_level = db.Column(db.Integer)
    phq2_score = db.Column(db.Integer)
    social_isolation = db.Column(db.String(100))
    psychosocial_factors = db.Column(db.String(100))
    cognition_words_correct = db.Column(db.Integer)
    cognition_year = db.Column(db.Integer)
    cognition_month = db.Column(db.Integer)
    cognition_day_of_week = db.Column(db.Integer)
    cognition_sock = db.Column(db.Integer)
    cognition_blue = db.Column(db.Integer)
    cognition_bed = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    living_will = db.Column(db.Boolean)
    medical_power_of_attorney = db.Column(db.Boolean)
    mpoa_name = db.Column(db.String(100))
    mpoa_phone = db.Column(db.String(20))
    dnr = db.Column(db.Boolean)
    agency_received_copy = db.Column(db.Boolean)

class Wounds(db.Model):
    __tablename__ = 'wounds'

    wound_id = db.Column(db.Integer, primary_key=True)
    visit_id = db.Column(db.Integer, db.ForeignKey('visits.visit_id'))
    location = db.Column(db.String(100))
    soiled_percentage = db.Column(db.Integer)
    length = db.Column(db.Integer)
    covering = db.Column(db.String(100))
    adherence = db.Column(db.String(100))
    periwound_skin = db.Column(db.String(100))
    number_of_wounds = db.Column(db.Integer)
    care_provided = db.Column(db.String(100))
    care_tolerance = db.Column(db.String(100))
    care_custom = db.Column(db.String(100))
    description = db.Column(db.String(500))

class Equipment(db.Model):
    __tablename__ = 'equipment'

    equipment_id = db.Column(db.Integer, primary_key=True)
    visit_id = db.Column(db.Integer, db.ForeignKey('visits.visit_id'))
    bed_comm_mode = db.Column(db.Boolean)
    cane = db.Column(db.Boolean)
    toilet_seat_extension = db.Column(db.Boolean)
    grab_bars = db.Column(db.Boolean)
    hospital_bed = db.Column(db.Boolean)
    nebulizer = db.Column(db.Boolean)
    oxygen_supplement = db.Column(db.Boolean)
    tub_bench = db.Column(db.Boolean)
    walker = db.Column(db.Boolean)
    wheelchair = db.Column(db.Boolean)
    bed_rail = db.Column(db.Boolean)
    cervical_brace = db.Column(db.Boolean)
    grabber = db.Column(db.Boolean)
    knee_immobilizer = db.Column(db.Boolean)
    lumbar_brace = db.Column(db.Boolean)
    rollator = db.Column(db.Boolean)
    sock_helper = db.Column(db.Boolean)
    shower_chair = db.Column(db.Boolean)

class Treatment(db.Model):
    __tablename__ = 'treatment'

    treatment_id = db.Column(db.Integer, primary_key=True)
    visit_id = db.Column(db.Integer, db.ForeignKey('visits.visit_id'))
    subjective = db.Column(db.TEXT)
    treatment_given = db.Column(db.TEXT)

class SpecialTreatments(db.Model):
    __tablename__ = 'special_treatments'

    special_treatment_id = db.Column(db.Integer, primary_key=True)
    visit_id = db.Column(db.Integer, db.ForeignKey('visits.visit_id'))
    chemo_iv = db.Column(db.Boolean)
    chemo_oral = db.Column(db.Boolean)
    radiation = db.Column(db.Boolean)
    suctioning = db.Column(db.Boolean)
    tracheostomy_care = db.Column(db.Boolean)
    invasive_mechanical_ventilation = db.Column(db.Boolean)
    non_invasive_mechanical = db.Column(db.Boolean)












   




