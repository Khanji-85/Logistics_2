from datetime import date
from functools import wraps
from flask_jwt_extended import get_jwt_identity, jwt_required
import flask_login
import pandas as pd
from flask import app, redirect, request, jsonify, Blueprint,  session, render_template, url_for
from sqlalchemy import create_engine
import marshmallow_models
import models
import services 
from app import db 

bp = Blueprint('main', __name__)

user_schema = marshmallow_models.UserSchema()
users_schema = marshmallow_models.UserSchema(many=True)


def import_excel(file_path):
    # Read the Excel file into a DataFrame, skipping the first few rows (headers)
    df = pd.read_excel(file_path, skiprows=1)  # Adjust skiprows to ignore the header rows

    # Transform the DataFrame if necessary
    df.columns = ['first_name', 'last_name', 'father_name', 'mother_name', 'date_of_birth', 'personal_doctrine',
                  'gender', 'reg_number', 'doctrine', 'town', 'judiciary', 'governate', 'district']
    # Adjust column names as needed

    # Create a SQLAlchemy engine
    engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/LogisticsDB')

    # Insert the DataFrame into the PostgreSQL table
    # df.to_sql('shateb_original.tripoli_2024', engine, if_exists='append', index=False)
    with engine.connect() as connection:
        df.to_sql('tripoli_2024', connection, schema='shateb_original', if_exists='append', index=False)

    print("File successfully imported and data inserted")

def extract_attribute(objects, attribute):
    """
    Extracts a specific attribute from each object in an array.

    :param objects: List of objects
    :param attribute: The attribute to extract
    :return: List of attribute values
    """
    return [getattr(obj, attribute) for obj in objects]

def extract_attributes(objects, *attributes):
    """
    Extracts specific attributes from each object in an array.

    :param objects: List of objects
    :param attributes: The attributes to extract
    :return: List of tuples containing attribute values
    """

    ss = [
        tuple(getattr(obj, attribute) for attribute in attributes)
        for obj in objects
    ]
    return ss

@bp.route('/', methods=['GET'])
@flask_login.login_required
def home_page():
    # view-table
    headings = ['user_id', 'username', 'email', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'role_id', 'status_id']
    data = [[user.id, user.username, user.email, user.first_name, user.last_name, user.date_of_birth, user.phone_number, user.role_id, user.status_id] for user in services.get_all_users()]
    return render_template('home-page.html', headings=headings, data=data, table_name='User Table')

@bp.route('/add_user')
@flask_login.login_required
def add_user():
    try:
        user_id = get_jwt_identity()
        user = models.User(username='samaasser', email='sam323sss8@gmail.com', first_name='سامر')
        user.password = 'password'
        db.session.add(user)
        db.session.commit()
        return "User added!"
    except Exception as e:
        db.session.rollback()
        return str(e)

@bp.route('/add_user_health', methods=['POST', 'GET'])
@flask_login.login_required
def add_health_sector():
    # data for Table view :
    headings = [field.name for field in models.HealthSector.__table__.columns]
    data = [[
    health_sector.id,
    health_sector.first_name,
    health_sector.last_name,
    health_sector.father_name,
    health_sector.mother_name,
    health_sector.date_of_birth,
    health_sector.reg_number,
    health_sector.date_of_service,
    health_sector.contact_number,
    health_sector.amount_usd,
    health_sector.amount_lira,
    health_sector.description,
    health_sector.shateb_id,
    health_sector.gender_id,
    health_sector.nationality_id,
    health_sector.town_id,
    health_sector.judiciary_id,
    health_sector.governate_id,
    health_sector.institution_id,
    health_sector.reference_id,
    health_sector.inserted_by_user_id,
    health_sector.service_type_id,
    health_sector.martial_status_id
    ] for health_sector in services.get_all_health_sectors()]
    ######
    nationality_list = services.get_all_nationalities()
    gender_list = services.get_all_genders()
    genders = extract_attribute(gender_list, 'description')
    nationalities = extract_attribute(nationality_list, 'description')
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']

        birth_date = request.form['date']
        gender = request.form['gender']

        nationality = request.form['nationality']

        ssn = request.form['ssn']
        status = request.form['status']

        service = request.form['service']
        amount = request.form['amount']

        phone = request.form['phone']

        hospital = request.form['hospital']
        reference = request.form['reference']
        employee = request.form['employee']

        gender_id = services.get_gender_id_by_description(gender)

        form = models.HealthSector(first_name=name, last_name=last_name, mother_name=mother_name,
                                   father_name=father_name, date_of_birth=birth_date, gender_id=gender_id,
                                   amount_usd=amount, contact_number=phone,
                                   reg_number=ssn)

        form1 = services.add_health_sector_user_form(form)
        db.session.add(form)
        db.session.commit()
    return render_template('add_user.html',headings=headings, data=data, table_name='Health Sector Table',nationalities_list=nationalities, genders_list=genders)

@bp.route('/get-shateb', methods=['GET'])
@flask_login.login_required
def get_shateb_users():
    ss = request.args.get('q')
    print(ss)
    users = services.get_shateb_user_by_reg_number(ss)
    return jsonify(users)

@bp.route('/add_user_education', methods=['POST', 'GET'])
@flask_login.login_required
def add_education_sector():
    # data for Table view :
    headings = [field.name for field in models.EducationSector.__table__.columns]
    data = [[
        education_sector.id,
        education_sector.first_name,
        education_sector.last_name,
        education_sector.father_name,
        education_sector.mother_name,
        education_sector.date_of_birth,
        education_sector.reg_number,
        education_sector.date_of_service,
        education_sector.contact_number,
        education_sector.amount_usd,
        education_sector.amount_lira,
        education_sector.academic_year,
        education_sector.description,
        education_sector.service_type_id 
        ] for education_sector in services.get_all_education_sectors()]
    
    #####
    nationality_list = services.get_all_nationalities()
    gender_list = services.get_all_genders()
    gov_list = services.get_all_governates()
    jud_list = services.get_all_judiciaries()
    town_list = services.get_all_towns()
    service_list = services.get_all_services()
    institution_list = services.get_all_institutions()
    martial_list = services.get_all_marital_status()
    user_list = services.get_all_users()
    genders = extract_attribute(gender_list, 'description')
    nationalities = extract_attribute(nationality_list, 'description')
    governates = extract_attribute(gov_list, 'description')
    judiciaries = extract_attribute(jud_list, 'description')
    towns = extract_attribute(town_list, 'description')
    servicess = extract_attribute(service_list, 'description')
    institutions = extract_attribute(institution_list, 'description')
    martials = extract_attribute(martial_list, 'description')
    user_data = extract_attributes(user_list, 'first_name', 'last_name', 'id')

    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']

        birth_date = request.form['date']
        gender = request.form['gender']

        nationality = request.form['nationality']

        ssn = request.form['ssn']
        status = request.form['martial_status']

        service = request.form['services']
        amount = request.form['amount']
        amount_lira = request.form['amount_lira']

        phone = request.form['phone']

        hospital = request.form['insts']
        reference = request.form['reference']
        employee = request.form['admins']

        town = request.form['towns']
        judiciary = request.form['judiciaries']
        governate = request.form['govs']
        academic_year = request.form['academic_year']

        shateb_id = request.form['shateb']

        gender_id = services.get_gender_id_by_description(gender)
        nationality_id = services.get_nationality_id_by_description(nationality)
        martial_id = services.get_martial_id_by_description(status)
        service_id = services.get_services_id_by_description(service)
        institution_id = services.get_inst_id_by_description(hospital)
        town_id = services.get_town_id_by_description(town)
        judiciary_id = services.get_judiciary_id_by_description(judiciary)
        governate_id = services.get_governate_id_by_description(governate)

        form = models.EducationSector(first_name=name, last_name=last_name, mother_name=mother_name,
                                      father_name=father_name, date_of_birth=birth_date, gender_id=gender_id,
                                      amount_usd=amount, contact_number=phone,
                                      reg_number=ssn, nationality_id=nationality_id, town_id=town_id,
                                      judiciary_id=judiciary_id, governate_id=governate_id,
                                      institution_id=institution_id,
                                      academic_year=academic_year, service_type_id=service_id, shateb_id=shateb_id,
                                      amount_lira=amount_lira)
        form.date_of_service = date.today()

        print(employee)
        db.session.add(form)
        db.session.commit()

    return render_template('add_user_education.html',headings = headings, data=data,table_name="EducationSector table",nationalities_list=nationalities, genders_list=genders,
                           governates_list=governates, judiciaries_list=judiciaries, towns_list=towns,
                           services_list=servicess, institutions_list=institutions, martials_list=martials,
                           admin_first=user_data, admin_last=user_data)

@bp.errorhandler(404)
@flask_login.login_required
def page_not_found(e):
    return render_template('404-page.html',title="page not found"),404

@bp.errorhandler(500)
@flask_login.login_required
def internal_server(e):
    return render_template('500-page.html',title="Internal Server Error"),500

@bp.errorhandler(400)
@flask_login.login_required
def internal_server(e):
    return render_template('400-page.html',title="Internal Server Error"),400
