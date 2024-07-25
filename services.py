from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
import models
from datetime import date
from models import EducationSector, HealthSector, SecuritySector, User, db

def create_user(username, email, password, first_name, last_name, dob, phone_number):
    user = models.User(username=username, email=email, first_name=first_name, last_name=last_name, date_of_birth=dob,
                       phone_number=phone_number)
    user.password = password
    return user

def get_user_by_email(email):
    user = models.User.query.filter_by(email=email).first()
    if user:
        return user
    else:
        user = False
        return user

def get_user_by_username(username):
    user = models.User.query.filter_by(username=username).first()
    if user:
        return user
    else:
        user = False
        return user

def authenticate_password(email, password):
    user = get_user_by_email(email)
    if user:
        if user.check_password(password):
            return True
        else:
            return False
    else:
        return False

def get_all_genders():
    genders = models.Gender.query.all()
    genders1 = models.Gender.query.with_entities(models.Gender.description).all()

    return genders

def get_all_nationalities():
    nationalities = models.Nationality.query.all()
    nationalities1 = models.Nationality.query.with_entities(models.Nationality.description).all()
    return nationalities

def get_nationality_id_by_name(name):
    nationalities = get_all_nationalities()
    for i in nationalities:
        if nationalities[i].description == name:
            return nationalities[i].id, True

    return False

def get_gender_id_by_name(name):
    genders = get_all_genders()
    for i in genders:
        if i == name:
            return genders[i].id, True

    return False

def add_health_sector_user_form(health_sector_user):
    if health_sector_user is models.HealthSector:
        health_sector_user.date_of_service = date.today()
        return health_sector_user

def get_gender_id_by_description(description):
    """
    Returns the object ID for the given description from the database.

    :param description: The description for which the object ID is needed
    :return: The object ID corresponding to the given description or None if not found
    """
    # Query the database to find the object with the given description
    obj = models.Gender.query.filter_by(description=description).first()

    if obj:
        return obj.id
    else:
        return None

def get_shateb_user_by_reg_number(number):
    users = models.Shateb.query.filter_by(reg_number=number).all()
    users_list = [{"id": user.id, "first_name": user.first_name, "last_name": user.last_name,
                   "father_name": user.father_name, "reg_number": user.reg_number, } for user in users]
    return users_list

def registration_service(user):
    try: 
        if user is None :
            return False,"Try another Username"
        elif get_user_by_email(user.email):
            return False,"Try another Email",400
        elif get_user_by_username(user.username):
            return False,"Try another Username",400
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        raise e

def login_service(email,password):
    if email is None or password is None : 
        return False
    user = get_user_by_email(email)
    if user is not None:
        if user.check_password(password):
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            return True ,{"access_token" :access_token,"refresh_token": refresh_token}
    return False

def get_all_towns():
    towns = models.Town.query.all()
    return towns


def get_all_marital_status():
    status = models.MartialStatus.query.all()
    return status


def get_all_judiciaries():
    jud = models.Judiciary.query.all()
    return jud


def get_all_governates():
    gov = models.Governate.query.all()
    return gov


def get_all_services():
    services = models.Service.query.all()
    return services


def get_all_institutions():
    inst = models.Institution.query.all()
    return inst

def get_all_users():
    inst = models.User.query.all()
    return inst

def get_nationality_id_by_description(description):
    """
    Returns the object ID for the given description from the database.

    :param description: The description for which the object ID is needed
    :return: The object ID corresponding to the given description or None if not found
    """
    # Query the database to find the object with the given description
    obj = models.Nationality.query.filter_by(description=description).first()

    if obj:
        return obj.id
    else:
        return None

def get_services_id_by_description(description):
    """
    Returns the object ID for the given description from the database.

    :param description: The description for which the object ID is needed
    :return: The object ID corresponding to the given description or None if not found
    """
    # Query the database to find the object with the given description
    obj = models.Service.query.filter_by(description=description).first()

    if obj:
        return obj.id
    else:
        return None


def get_governate_id_by_description(description):
    """
    Returns the object ID for the given description from the database.

    :param description: The description for which the object ID is needed
    :return: The object ID corresponding to the given description or None if not found
    """
    # Query the database to find the object with the given description
    obj = models.Governate.query.filter_by(description=description).first()

    if obj:
        return obj.id
    else:
        return None


def get_town_id_by_description(description):
    """
    Returns the object ID for the given description from the database.

    :param description: The description for which the object ID is needed
    :return: The object ID corresponding to the given description or None if not found
    """
    # Query the database to find the object with the given description
    obj = models.Town.query.filter_by(description=description).first()

    if obj:
        return obj.id
    else:
        return None


def get_judiciary_id_by_description(description):
    """
    Returns the object ID for the given description from the database.

    :param description: The description for which the object ID is needed
    :return: The object ID corresponding to the given description or None if not found
    """
    # Query the database to find the object with the given description
    obj = models.Judiciary.query.filter_by(description=description).first()

    if obj:
        return obj.id
    else:
        return None


def get_inst_id_by_description(description):
    """
    Returns the object ID for the given description from the database.

    :param description: The description for which the object ID is needed
    :return: The object ID corresponding to the given description or None if not found
    """
    # Query the database to find the object with the given description
    obj = models.Institution.query.filter_by(description=description).first()

    if obj:
        return obj.id
    else:
        return None


def get_martial_id_by_description(description):
    """
    Returns the object ID for the given description from the database.

    :param description: The description for which the object ID is needed
    :return: The object ID corresponding to the given description or None if not found
    """
    # Query the database to find the object with the given description
    obj = models.MartialStatus.query.filter_by(description=description).first()

    if obj:
        return obj.id
    else:
        return None

def get_all_education_sectors():
    result =EducationSector.query.all()
    return result

def get_all_health_sectors():
    result = HealthSector.query.all()
    return result

def get_all_security_Sectors():
    result = SecuritySector.quert.all()
    return result 
