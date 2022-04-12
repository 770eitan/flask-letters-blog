from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from flask_wtf.file import FileField, FileRequired, FileAllowed

from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    value = IntegerField ('Value', validators=[DataRequired()])
    submit = SubmitField('Post')
    
