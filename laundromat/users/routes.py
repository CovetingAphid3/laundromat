from flask import Blueprint
from flask import render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

from laundromat import db
from laundromat.users.forms import RegistrationForm, LoginForm, AddAddress, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from laundromat.users.utils import send_reset_email 
from laundromat.models import User, Address


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, surname=form.surname.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('users/register.html', title='Register', form =form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        #remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password==form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('users/login.html', title='Login', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.surname = form.surname.data
        current_user.phone = form.phone.data
        user = User(name=form.name.data, surname=form.surname.data, phone=form.phone.data)
        address = Address.query.filter_by(user_id=current_user.id).first()
        if not address:
            address = Address(street_name=form.street_name.date, complex=form.complex.data, suburb=form.suburb.data, postal_code=form.postal_code.data)
            address.street_name = form.street_name.data
            address.complex = form.complex.data
            address.suburb = form.suburb.data
            address.postal_code = form.postal_code.data
            address.user = current_user
            db.session.add(address)
            db.session.commit()
        address.street_name = form.street_name.data
        address.complex = form.complex.data
        address.suburb = form.suburb.data
        address.postal_code = form.postal_code.data
        address.user = current_user
        db.session.commit()
        flash('Account details updated successfully.', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.surname.data = current_user.surname
        form.phone.data = current_user.phone
        address = Address.query.filter_by(user_id=current_user.id).first()
        if address:
            form.street_name.data = address.street_name
            form.complex.data = address.complex
            form.suburb.data = address.suburb
            form.postal_code.data = address.postal_code
        
    return render_template('users/account.html', title='Account', form=form)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('users/reset_request.html', title='Reset Password', form=form)

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.password = form.password.data
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('users/reset_token.html', title='Reset Password', form=form)

@users.route('/addressbook', methods=['GET', 'POST'])
@login_required
def addressbook():
    form = AddAddress()
    if form.validate_on_submit():
        address = Address(street_name=form.street_name.data, complex=form.complex.data, suburb=form.suburb.data, postal_code=form.postal_code.data, user=current_user)
        db.session.add(address)
        db.session.commit()
        flash('Address addded', 'success')
        return redirect(url_for('orders.order'))
    return render_template('users/addressbook.html', title='Address book', form=form)
