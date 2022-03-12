from flask import render_template,redirect,url_for,abort,request
from idna import valid_string_length
from . import main
from ..requests import get_quote
from .forms import CommentForm,UpdateProfile,BlogForm
from ..models import User,Comments,Blogs,Quote
from flask_login import login_required, current_user
from .. import db
import markdown2  

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    quote = get_quote('quote')
    blogs = Blogs.query.all()
    title = 'Home - Welcome to my Personal Blog Website'    
    return render_template('index.html',blogs = blogs, title = title,quote=quote)

@main.route('/blog/',methods = ['GET','POST'])
@login_required
def blog_form():
    blog_form = BlogForm()
    title = ' Blog page '    

    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog_text = blog_form.blog_text.data
        
        new_blogs = Blogs(blog_text=blog_text,user_id=current_user._get_current_object().id,title = title)
        new_blogs.save_b()
        return redirect(url_for('main.index' ))

    return render_template('new_blog.html', blog_form=blog_form, title=title )

@main.route('/comment/<int:blog_id>', methods = ['GET','POST'])
@login_required
def comment(blog_id):
    comment_form = CommentForm()
    title = ' Comments page '    
    blogs = Blogs.query.get(blog_id)
    comments = Comments.get_comment(blog_id)
    user = User.query.filter_by(id=id)
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        
        # Updated commentinstance
        new_comment = Comments(blog_id=blog_id,comment=comment,user_id=current_user.get_id())
        # save comment method
        new_comment.save()
        return redirect(url_for('main.comment',blog_id = blog_id ))

    return render_template('comment.html',comment_form=comment_form,blogs=blogs,comments=comments,user=user,title = title)
    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    blog = Blogs.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,blog=blog)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


