from flask import render_template, request, redirect, url_for, flash
from . import main
from flask_login import login_required, current_user
from .forms import PitchForm, CommentForm, UpdateProfile
from ..models import Pitch,User,Upvote,Downvote, Comment
from .. import db
@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    pitches = Pitch.query.filter_by()
    print(pitches)
    return render_template(
        "index.html", pitches = pitches
    )
    
@main.route('/pitches/new/', methods = ['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    print(form.errors)
    # my_upvotes = Upvote.query.filter_by(pitch_id = Pitch.id)
    if form.is_submitted():
        print('submitted')
    if form.validate():
        print("valid")
    print(form.errors)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('pitch.html',form=form)

@main.route('/pitches/<category>')
@login_required
def category(category):
    pitches = Pitch.query.filter_by(category=category).all()
    print(pitches)
    return render_template('category.html', pitches = pitches)


@main.route('/upvote/<int:id>',methods = ['POST','GET'])
@login_required
def upvote(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/downvote/<int:id>',methods = ['POST','GET'])
@login_required
def downvote(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in pitch:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))

@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    print(pitch)
    if form.validate_on_submit():
        description = form.description.data
        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.new_comment', pitch_id= pitch_id))
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comments.html', form = form, comment = all_comments, pitch = pitch )

@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()
    user_id = current_user._get_current_object().id
    pitches = Pitch.query.filter_by(owner_id=user_id).all()
    print(pitches)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, pitches=pitches)

@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update-profile.html',form =form)