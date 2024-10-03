from flask import Blueprint
from flask import render_template, abort, redirect, url_for, request, flash
from flask_login import  current_user, login_required
from laundromat import db
from laundromat.admin.forms import AdminUpdateStatusOfOrder, AdminUpdateUser, AdminUpdateAddress
from laundromat.models import Orders, User, Address, Newsletter

administrator = Blueprint('admin', __name__)


@administrator.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    orders = Orders.query.order_by(Orders.id.desc()).all()
    return render_template('admin/orders/admin_dashboard.html', orders=orders)


@administrator.route('/admin/order/<int:order_id>', methods=['GET', 'POST'])
@login_required
def admin_order_details(order_id):
    if not current_user.is_admin:
        abort(403)
    order = Orders.query.get_or_404(order_id)
    form = AdminUpdateStatusOfOrder()
    image_file = order.image
    if request.method == 'POST' and form.validate_on_submit:
        if form.status.data == 'Payment Required':
            if not form.price.data:
                flash('If the status is set to "Payment Required" then a price is is required.', 'success')
                return render_template('admin/orders/admin_order_details.html', order=order, form=form, image_file=image_file)
            order.price = form.price.data
            order.status = form.status.data
        order.status = form.status.data
        db.session.commit()
        return redirect(url_for('admin.admin_dashboard'))
    return render_template('admin/orders/admin_order_details.html', order=order, form=form, image_file=image_file)

@administrator.route('/admin/dashboard/users')
@login_required
def customers():
    if not current_user.is_admin:
        abort(403)
    page = request.args.get('page', 1, type=int)
    users = User.query.order_by(User.id.desc()).paginate(page=page, per_page=20)
    return render_template('admin/customers/list.html', users=users)

@administrator.route('/admin/dashboard/users/<int:user_id>', methods=['GET', 'POST'])
@login_required
def customer(user_id):
    if not current_user.is_admin:
        abort(403)
    user = User.query.get_or_404(user_id)
    page = request.args.get('page', 1, type=int)
    orders =Orders.query.filter_by(user_id=user_id).order_by(Orders.date_created.desc()).paginate(page=page, per_page=2)
    address= Address.query.filter_by(user_id=user_id).first()
    return render_template('admin/customers/detail.html', user=user,orders=orders,address=address)

@administrator.route("/admin/dashboard/users/<int:user_id>/delete", methods=['POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin:
        abort(403)
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User has been deleted!', 'success')
    return redirect(url_for('admin.customers'))
    
@administrator.route("/admin/dashboard/users/<int:user_id>/edit", methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if not current_user.is_admin:
        abort(403)
    user = User.query.get_or_404(user_id)
    address = Address.query.filter_by(user_id=user_id).first()
    userForm = AdminUpdateUser()
    userForm.name.data = user.name
    userForm.surname.data = user.surname
    userForm.email.data = user.email
    userForm.phone.data = user.phone
    addressForm = AdminUpdateAddress()
    addressForm.street_name.data = address.street_name
    addressForm.complex.data = address.complex
    addressForm.suburb.data = address.suburb
    addressForm.postal_code.data = address.postal_code
    if request.method == 'POST' and userForm.validate_on_submit:
        return redirect(url_for('admin.customer', user_id=user_id))
    elif request.method == 'POST' and addressForm.validate_on_submit:
        return redirect(url_for('admin.customer', user_id=user_id))
    return render_template('admin/customers/edit.html', userForm=userForm, addressForm=addressForm)

@administrator.route("/admin/dashboard/newsletter")
@login_required
def newsletter_list():
    if not current_user.is_admin:
        abort(403)
    page = request.args.get('page', 1, type=int)
    newsletter_list = Newsletter.query.order_by(Newsletter.id.desc()).paginate(page=page, per_page=50)
    return render_template('admin/newsletter/list.html', newsletter_list=newsletter_list)

    


    
    

