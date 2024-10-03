from flask import Blueprint, render_template, redirect, request, flash, url_for
from laundromat import db
from laundromat.models import Newsletter

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/service")
def service():
    return render_template('service.html', title='Service')

@main.route("/pricing")
def pricing():
    return render_template('pricing.html', title='Pricing')

@main.route("/details")
def details():
    return render_template('details.html', title='details')

@main.route("/blog")
def blog():
    return render_template('blog.html', title='blog')


@main.route("/", methods=['GET', 'POST'])
def newsletter_signup():
    name = request.form.get('name')
    email = request.form.get('email')
    newsletter_receipient = Newsletter(name=name, email=email)
    db.session.add(newsletter_receipient)
    db.session.commit()
    flash("You've been successfully signed up to the newsletter", "success")
    return render_template('service.html', title='Service')