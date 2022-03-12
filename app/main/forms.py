from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import DataRequired
from ..models import User,Subscribe
class CommentForm(FlaskForm):
     comment = TextAreaField('Comment',validators = [DataRequired()])
     submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
     title = StringField('Title',validators = [DataRequired()])
     blog_text = TextAreaField('Write your blog...',validators = [DataRequired()])
     submit = SubmitField('Submit')
class SubscribeForm(FlaskForm):
    email = StringField('Enter your  email',validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
        if Subscribe.query.filter_by(email = data_field.data).first():
            raise ValidationError('This information exists.') 