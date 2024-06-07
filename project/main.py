from flask import Blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template(
        'index.html'
    )

@main.route('/')
@login_required
def profile():
    return render_template(
        'profile.html',
        name=current_user.name
    )

@main.route('/room')
@login_required
def room():
    return render_template(
        'Kaihatu2.html'
        )
