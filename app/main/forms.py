from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import Required
from wtforms import ValidationError


class PitchForm(FlaskForm):

 title = StringField('Title', validators = [Required()])

 description = TextAreaField('Type your your pitch',validators=[Required()])

 category = SelectField('category', choices=[('Presentation','Presentation'),('Pickup Lines','Pick Lines'),('Interview','Interview')], validators=[Required()])

class CommentForm(FlaskForm):
  description = TextAreaField('Add comment',validators=[Required()])