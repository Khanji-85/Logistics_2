from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import models
from app import db


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = models.User
        load_instance = True
        sqla_session = db.session