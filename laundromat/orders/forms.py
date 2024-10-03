from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, DateField, TimeField, TelField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length

class CreateOrder(FlaskForm):
	phone = TelField('Phone number', validators=[DataRequired()])
	#province = SelectField('Province', choices=['Kwa-Zulu Natal', 'Gauteng', 'Western Cape', 'Northern Cape', 'Eastern Cape', 'Limpopo', 'Mpumalanga'])
	service = SelectField('Select service', choices=['Wash, Dry & Iron', 'Ironing', 'Dry Cleaning', 'Shoe Cleaning & Repairs'])
	date = DateField('What date should we pick up your laundry?', validators=[DataRequired()], format="%Y-%m-%d")
	pick_up_time = TimeField('What time should we pick up your laundry?', validators=[DataRequired()])
	special_instructions = TextAreaField('Do you have any special instructions?', validators=[Length(max=250)])
	picture = FileField('Show us what you are talking about ?', validators=[FileAllowed(['jpg','jpeg', 'png'])])
	submit = SubmitField('Wash laundry')

class UserUpdateStatusOfOrder(FlaskForm):
	suburb = SelectField('Status', choices= ['Continue', 'Do nothing'])
