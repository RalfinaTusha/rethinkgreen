from datetime import datetime
from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.coupon import Coupon
from flask_app.models.user import User

import os   
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'flask_app/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/coupons')
def coupons():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('coupons.html', coupons = Coupon.get_coupons())


@app.route('/purchase' , methods=['POST'])   
def purchase():
    if 'user_id' not in session:
        return redirect('/')
    
    points = int(request.form['points'])
    user = User.get_by_id({'id': session['user_id']})
    user_points = user.points
    if user_points < points:
        flash("You don't have enough points to purchase this coupon.", "notEnoughPoints")
        return redirect('/coupons')
    user_points -= points
    data = {
        'id': session['user_id'],
        'points': user_points,
        'coupon_id': request.form['coupon_id']
    }
    User.update_points(data)
    Coupon.user_coupons(data)
    return redirect('/')
