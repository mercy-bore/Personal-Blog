from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
     comment = TextAreaField('Comment',validators = [DataRequired()])
     submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
     title = StringField('Title',validators = [DataRequired()])
     text = TextAreaField('Write your blog...',validators = [DataRequired()])
     submit = SubmitField('Submit')
