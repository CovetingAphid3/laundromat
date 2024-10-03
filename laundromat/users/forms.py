from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from laundromat.models import User


class RegistrationForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	surname = StringField('Surname', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('ConfirmPassword', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')
	def validate_email(self, email):
		user_exists = User.query.filter_by(email=email.data).first()
		if user_exists:
			raise ValidationError('Email address already exists')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')

class AddAddress(FlaskForm):
	street_name  = StringField('Street Address', validators=[DataRequired(), Length(max=250)])
	complex = StringField('Complex | Unit Number', validators=[Length(max=20)])
	suburb = SelectField('Suburb', choices= ['Northern suburbs - JHB Gauteng', 'Western suburbs - JHB Gauteng', 'Southern suburbs - JHB Gauteng', 'Eastern suburbs - JHB Gauteng', 'City & Central suburbs - JHB Gauteng'], validators= [DataRequired()])
	postal_code = IntegerField('Postal code', validators= [DataRequired()])
	submit = SubmitField('Add address')

class UpdateAccountForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired()])
	surname = StringField('Surname', validators=[DataRequired()])
	phone = TelField('Phone number', validators=[DataRequired(), Length(max=10)])
	street_name  = StringField('Street Address', validators= [DataRequired()])
	complex = StringField('Complex | Unit Number', validators=[Length(max=20)])
	suburb = SelectField('Suburb', choices= ['Northern suburbs - JHB Gauteng', 'Western suburbs - JHB Gauteng', 'Southern suburbs - JHB Gauteng', 'Eastern suburbs - JHB Gauteng', 'City & Central suburbs - JHB Gauteng'], validators= [DataRequired()])
	postal_code = IntegerField('Postal code', validators= [DataRequired()])
	submit = SubmitField('Update')
	
class RequestResetForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Request Password Reset')
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('There is no account with that email address. You must register first.')
		
class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('ConfirmPassword', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Reset Pasword')

