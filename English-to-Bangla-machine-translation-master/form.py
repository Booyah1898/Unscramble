from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField
from wtforms.validators import DataRequired


class Enter(FlaskForm):
	sentence = StringField('Name',[DataRequired()])
	submit = SubmitField('Translate')








