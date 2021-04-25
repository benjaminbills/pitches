from flask import render_template, request, redirect, url_for, flash
from . import main
from flask_login import login_required, current_user
from .forms import PitchForm
from ..models import Pitch
from .. import db
@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """

    title = "Welcome to Pitches App"

    return render_template(
        "index.html", title=title
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
        print(description,title, owner_id, category)
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('pitch.html',form=form)