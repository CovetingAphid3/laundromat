from flask import Blueprint
from flask import render_template, request, redirect, url_for, session, flash, abort
from flask_login import current_user, login_required

from laundromat import db
from laundromat.models import Orders, Address
from laundromat.orders.forms import CreateOrder
from laundromat.orders.utils import save_picture

orders = Blueprint('orders', __name__)

@orders.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    form = CreateOrder()
    form.phone.data = current_user.phone
    if form.validate_on_submit():
        if form.picture.data:
            picture_file_name = save_picture(form.picture.data)
            order = Orders(phone=form.phone.data, service=form.service.data, date=form.date.data, pick_up_time=form.pick_up_time.data, special_instructions=form.special_instructions.data, user=current_user)
        order = Orders(phone=form.phone.data, service=form.service.data, date=form.date.data, pick_up_time=form.pick_up_time.data, special_instructions=form.special_instructions.data, image=picture_file_name, user=current_user)
        db.session.add(order)
        db.session.commit()
        flash('We are now processing your order.', 'success')
        return redirect(url_for('orders.view_orders'))   
    elif not Address.query.filter_by(user_id=current_user.id).first():
        flash('Please add an address to your account first.', 'success')
        return redirect(url_for('users.addressbook'))

    return render_template('orders/order.html', title='Laundry', form=form)


@orders.route('/orders')
@login_required
def view_orders():
    ref_orders = Orders.query.filter_by(user_id=current_user.id).first()
    if ref_orders is None:
        flash('Seems like you have no orders to view. Please make an order first', 'success')
        return redirect(url_for('orders.order'))
    if ref_orders.user != current_user:
        abort(403)
    page = request.args.get('page', 1, type=int)
    orders = Orders.query.filter_by(user_id=current_user.id).order_by(Orders.date_created.desc()).paginate(page=page, per_page=2)
    return render_template('orders/orders.html', orders=orders)


@orders.route("/orders/<int:order_id>")
@login_required
def order_details(order_id):
    order = Orders.query.get_or_404(order_id)
    if order.user != current_user:
        abort(403)
    return render_template('orders/order_details.html', order=order)

@orders.route("/success")
def blog():
    flash("Thank you! Your payment was success. Your order will be updated shortly", "success")
    return render_template('service.html')