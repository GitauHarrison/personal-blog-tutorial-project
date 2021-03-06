from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import CommentForm
from app.models import User, Comment

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/about-me')
def about_me():
    return render_template('about_me.html', title = 'About Me')


@app.route('/hire-me')
def hire_me():
    return render_template('hire_me.html', title = 'Hire Me')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title = 'Portfolio')

@app.route('/my-interests')
def my_interests():
    return render_template('my_interests.html', title = 'My Interests')

# -------------------Articles Begin Here-----------------------
@app.route('/flask-webforms', methods = ['GET', 'POST'])
def flask_webforms():
    form = CommentForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        post = Comment(body = form.comment.data, author = user)
        db.session.add(user)
        db.session.add(post)
        db.session.commit()
        flash('Your comment is now live!')
        return redirect(url_for('flask_webforms'))
    posts = Comment.query.order_by(Comment.timestamp.desc())
    return render_template('flask_webforms.html', title = 'Flask Webforms', form = form, posts = posts)

# -------------------Articles End Here-----------------------