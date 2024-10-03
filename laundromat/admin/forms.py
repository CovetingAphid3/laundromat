from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField, StringField, IntegerField, TelField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from laundromat.models import User


class AdminUpdateStatusOfOrder(FlaskForm):
	price = FloatField()
	status = SelectField('Status', choices= ['Delivered', 'Cancelled', 'Pending', 'Shipped', 'Payment Required'])
	submit = SubmitField('Update')


class AdminUpdateUser(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	surname = StringField('Surname', validators=[DataRequired()])
	phone = TelField('Phone number', validators=[DataRequired(), Length(max=10)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('ConfirmPassword', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Update')
	def validate_email(self, email):
		user_exists = User.query.filter_by(email=email.data).first()
		if user_exists:
			raise ValidationError('Email address already exists')


class AdminUpdateAddress(FlaskForm):
	street_name  = StringField('Street Address', validators=[DataRequired(), Length(max=250)])
	complex = StringField('Complex | Unit Number', validators=[Length(max=20)])
	suburb = SelectField('Suburb', choices= ['Northern suburbs - JHB Gauteng', 'Western suburbs - JHB Gauteng', 'Southern suburbs - JHB Gauteng', 'Eastern suburbs - JHB Gauteng', 'City & Central suburbs - JHB Gauteng'], validators= [DataRequired()])
	postal_code = IntegerField('Postal code', validators= [DataRequired()])
	submit = SubmitField('Update users address')
