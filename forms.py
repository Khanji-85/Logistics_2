from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, Length , Optional, EqualTo,Regexp


class login_form(FlaskForm):
    email = StringField('البريد الإلكتروني', validators=[DataRequired(), Email()])
    password = PasswordField('كلمه المرور', validators=[DataRequired()])
    submit = SubmitField('الدخول')

class registration_form(FlaskForm):
    user_name = StringField('اسم المستخدم', validators=[DataRequired()])
    email = StringField('البريد الإلكتروني', validators=[DataRequired(), Email()])
    first_name = StringField('الاسم الأول', validators=[DataRequired()])
    last_name = StringField('الاسم الأخير', validators=[DataRequired()])
    password = PasswordField('كلمه المرور', validators=[DataRequired(),
                                                    Length(min=8, max=30),
                                                    Regexp('^(?=.*[A-Z])(?=.*[0-9])(?=.*[^a-zA-Z0-9]).{8,30}$',
                                                    message='كلمة السر يجب أن تكون معقدة (بحد أدنى 8 أحرف، حرف كبير واحد، رقم واحد، حرف خاص واحد)')
                                                    ])
    confirm_password = PasswordField('تاكيد كلمه المرور', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    phone_number = StringField('رقم الهاتف', validators=[DataRequired()]) 
    submit = SubmitField("التسجيل")

