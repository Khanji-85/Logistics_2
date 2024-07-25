from flask_login import UserMixin
from sqlalchemy import CheckConstraint
import re
from app import db, bcrypt

class Gender(db.Model):
    __tablename__ = 'lst_gender'
    __table_args__ = {'schema': 'master'}
    id = db.Column('gender_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    educations = db.relationship('EducationSector', backref='author')
    healths = db.relationship('HealthSector', backref='author')
    securities = db.relationship('SecuritySector', backref='author')

    def __repr__(self):
        return f'<Gender {self.description}>'


class Nationality(db.Model):
    __tablename__ = 'lst_nationality'
    __table_args__ = {'schema': 'master'}
    id = db.Column('nationality_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    # educations = db.relationship('EducationSector', backref='author')
    # healths = db.relationship('HealthSector', backref='author')
    # securities = db.relationship('SecuritySector', backref='author')

    def __repr__(self):
        return f'<Nationality {self.description}>'


class Governate(db.Model):
    __tablename__ = 'lst_governate'
    __table_args__ = {'schema': 'master'}
    id = db.Column('governate_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    # judiciaries = db.relationship('Judiciary', backref='author')
    # educations = db.relationship('EducationSector', backref='author')
    # healths = db.relationship('HealthSector', backref='author')
    # securities = db.relationship('SecuritySector', backref='author')

    def __repr__(self):
        return f'<Governate {self.description}>'


class Judiciary(db.Model):
    __tablename__ = 'lst_judiciary'
    __table_args__ = {'schema': 'master'}
    id = db.Column('judiciary_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    governate_id = db.Column(db.Integer, db.ForeignKey(Governate.id))
    # towns = db.relationship('Town', backref='author')
    # educations = db.relationship('EducationSector', backref='author')
    # healths = db.relationship('HealthSector', backref='author')
    # securities = db.relationship('SecuritySector', backref='author')

    def __repr__(self):
        return f'<Judiciary {self.description}>'


class Town(db.Model):
    __tablename__ = 'lst_town'
    __table_args__ = {'schema': 'master'}
    id = db.Column('town_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    judiciary_id = db.Column(db.Integer, db.ForeignKey(Judiciary.id))
    # educations = db.relationship('EducationSector', backref='author')
    # healths = db.relationship('HealthSector', backref='author')
    # securities = db.relationship('SecuritySector', backref='author')

    def __repr__(self):
        return f'<Town {self.description}>'


class Sector(db.Model):
    __tablename__ = 'lst_sector'
    __table_args__ = {'schema': 'master'}
    id = db.Column('sector_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    # services = db.relationship('Service', backref='author')
    # institutions = db.relationship('Institution', backref='author')

    def __repr__(self):
        return f'<Sector {self.description}>'


class Service(db.Model):
    __tablename__ = 'lst_service'
    __table_args__ = {'schema': 'master'}
    id = db.Column('service_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    sector_id = db.Column(db.Integer, db.ForeignKey(Sector.id))
    # references = db.relationship('Reference', backref='author')
    # educations = db.relationship('EducationSector', backref='author')
    # healths = db.relationship('HealthSector', backref='author')
    # securities = db.relationship('SecuritySector', backref='author')

    def __repr__(self):
        return f'<Service {self.description}>'


class Institution(db.Model):
    __tablename__ = 'lst_institution'
    __table_args__ = {'schema': 'master'}
    id = db.Column('institution_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    sector_id = db.Column(db.Integer, db.ForeignKey(Sector.id))
    # educations = db.relationship('EducationSector', backref='author')
    # healths = db.relationship('HealthSector', backref='author')
    # securities = db.relationship('SecuritySector', backref='author')

    def __repr__(self):
        return f'<Institution {self.description}>'


class Reference(db.Model):
    __tablename__ = 'lst_reference'
    __table_args__ = {'schema': 'master'}
    id = db.Column('reference_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    service_type_id = db.Column(db.Integer, db.ForeignKey(Service.id))
    # educations = db.relationship('EducationSector', backref='author')
    # healths = db.relationship('HealthSector', backref='author')
    # securities = db.relationship('SecuritySector', backref='author')

    def __repr__(self):
        return f'<Reference {self.description}>'


class Role(db.Model):
    __tablename__ = 'lst_role'
    __table_args__ = {'schema': 'master'}
    id = db.Column('role_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    # users = db.relationship('User', backref='author')

    def __repr__(self):
        return f'<Role {self.description}>'


class MartialStatus(db.Model):
    __tablename__ = 'martial_status'
    __table_args__ = {'schema': 'master'}
    id = db.Column('martial_status_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    # healths = db.relationship('HealthSector', backref='author')
    # securities = db.relationship('SecuritySector', backref='author')

    def __repr__(self):
        return f'<MartialStatus {self.description}>'


class Status(db.Model):
    __tablename__ = 'status'
    __table_args__ = {'schema': 'master'}
    id = db.Column('status_id', db.Integer, primary_key=True)
    description = db.Column(db.String)
    # users = db.relationship('User', backref='author')
    # registrations = db.relationship('MembershipRegistration', backref='author')

    def __repr__(self):
        return f'<Status {self.description}>'


class User(UserMixin,db.Model):
    __tablename__ = 'lst_user'
    id = db.Column('user_id', db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    date_of_birth = db.Column(db.Date)
    phone_number = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))
    status_id = db.Column(db.Integer, db.ForeignKey(Status.id))
    # educations = db.relationship('EducationSector', backref='author')
    # securities = db.relationship('SecuritySector', backref='author')

    __table_args__ = (
        CheckConstraint('char_length(username) >= 5', name='username_min_length'),
        CheckConstraint('char_length(password_hash) >= 5', name='password_min_length'),
        {'schema': 'master'}
    )

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True 

    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)
    
    @classmethod
    def get(cls, user_id):
        return cls.query.get(user_id)
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # Method to set password (hashes the password)
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # Method to check password (compares with the hashed password)
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    @staticmethod
    def is_valid_email(email):
        return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

    def __repr__(self):
        return f'<User {self.username}>'


class MembershipRegistration(db.Model):
    __tablename__ = 'membership_registration'
    __table_args__ = {'schema': 'master'}
    id = db.Column('registration_id', db.Integer, primary_key=True)
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())
    description = db.Column(db.String)
    status_id = db.Column(db.Integer, db.ForeignKey(Status.id))

    def __repr__(self):
        return f'<Membership {self.description}>'


class Shateb(db.Model):
    __tablename__ = 'tripoli_2024'
    __table_args__ = {'schema': 'shateb_original'}
    id = db.Column('shateb_id', db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    father_name = db.Column(db.String)
    mother_name = db.Column(db.String)
    date_of_birth = db.Column(db.String)
    personal_doctrine = db.Column(db.String)
    gender = db.Column(db.String)
    reg_number = db.Column(db.String)
    doctrine = db.Column(db.String)
    town = db.Column(db.String)
    judiciary = db.Column(db.String)
    governate = db.Column(db.String)
    district = db.Column(db.String)
    # educations = db.relationship('EducationSector', backref='author')
    # healths = db.relationship('HealthSector', backref='author')
    # securities = db.relationship('SecuritySector', backref='author')

    def __repr__(self):
        return f'<Shateb {self.description}>'


class EducationSector(db.Model):
    __tablename__ = 'education_sector'
    __table_args__ = {'schema': 'master'}
    id = db.Column('service_id', db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    father_name = db.Column(db.String)
    mother_name = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    reg_number = db.Column(db.Integer)
    date_of_service = db.Column(db.Date)
    contact_number = db.Column(db.String)
    amount_usd = db.Column(db.Numeric(precision=10, scale=2))
    amount_lira = db.Column(db.Numeric(precision=10, scale=2))
    academic_year = db.Column(db.String)
    description = db.Column(db.String)
    shateb_id = db.Column(db.Integer, db.ForeignKey(Shateb.id))
    gender_id = db.Column(db.Integer, db.ForeignKey(Gender.id))
    nationality_id = db.Column(db.Integer, db.ForeignKey(Nationality.id))
    town_id = db.Column(db.Integer, db.ForeignKey(Town.id))
    judiciary_id = db.Column(db.Integer, db.ForeignKey(Judiciary.id))
    governate_id = db.Column(db.Integer, db.ForeignKey(Governate.id))
    institution_id = db.Column(db.Integer, db.ForeignKey(Institution.id))
    reference_id = db.Column(db.Integer, db.ForeignKey(Reference.id))
    inserted_by_user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    service_type_id = db.Column(db.Integer, db.ForeignKey(Service.id))

    def __repr__(self):
        return f'<Education {self.description}>'


class HealthSector(db.Model):
    __tablename__ = 'health_sector'
    __table_args__ = {'schema': 'master'}
    id = db.Column('service_id', db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    father_name = db.Column(db.String)
    mother_name = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    reg_number = db.Column(db.Integer)
    date_of_service = db.Column(db.Date)
    contact_number = db.Column(db.String)
    amount_usd = db.Column(db.Numeric(precision=10, scale=2))
    amount_lira = db.Column(db.Numeric(precision=10, scale=2))
    description = db.Column(db.String)
    shateb_id = db.Column(db.Integer, db.ForeignKey(Shateb.id))
    gender_id = db.Column(db.Integer, db.ForeignKey(Gender.id))
    nationality_id = db.Column(db.Integer, db.ForeignKey(Nationality.id))
    town_id = db.Column(db.Integer, db.ForeignKey(Town.id))
    judiciary_id = db.Column(db.Integer, db.ForeignKey(Judiciary.id))
    governate_id = db.Column(db.Integer, db.ForeignKey(Governate.id))
    institution_id = db.Column(db.Integer, db.ForeignKey(Institution.id))
    reference_id = db.Column(db.Integer, db.ForeignKey(Reference.id))
    inserted_by_user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    service_type_id = db.Column(db.Integer, db.ForeignKey(Service.id))
    martial_status_id = db.Column(db.Integer, db.ForeignKey(MartialStatus.id))

    def __repr__(self):
        return f'<Health {self.description}>'


class SecuritySector(db.Model):
    __tablename__ = 'security_sector'
    __table_args__ = {'schema': 'master'}
    id = db.Column('service_id', db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    father_name = db.Column(db.String)
    mother_name = db.Column(db.String)
    date_of_birth = db.Column(db.Date)
    reg_number = db.Column(db.Integer)
    date_of_service = db.Column(db.Date)
    contact_number = db.Column(db.String)
    description = db.Column(db.String)
    shateb_id = db.Column(db.Integer, db.ForeignKey(Shateb.id))
    gender_id = db.Column(db.Integer, db.ForeignKey(Gender.id))
    nationality_id = db.Column(db.Integer, db.ForeignKey(Nationality.id))
    town_id = db.Column(db.Integer, db.ForeignKey(Town.id))
    judiciary_id = db.Column(db.Integer, db.ForeignKey(Judiciary.id))
    governate_id = db.Column(db.Integer, db.ForeignKey(Governate.id))
    institution_id = db.Column(db.Integer, db.ForeignKey(Institution.id))
    reference_id = db.Column(db.Integer, db.ForeignKey(Reference.id))
    inserted_by_user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    service_type_id = db.Column(db.Integer, db.ForeignKey(Service.id))
    martial_status_id = db.Column(db.Integer, db.ForeignKey(MartialStatus.id))

    def __repr__(self):
        return f'<Security {self.description}>'