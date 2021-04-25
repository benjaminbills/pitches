from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from wtforms import ValidationError


class PitchForm(FlaskForm):

 title = StringField('Title', validators = [Required()])

 description = TextAreaField('Type your your pitch',validators=[Required()])

 category = StringField('category', validators=[Required()])

