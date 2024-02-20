from datetime import datetime
from flask_app import app
from flask import render_template, request, session, redirect, flash
from flask_app.models.recycle import Recycle
import os   
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'flask_app/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/coupons')
def coupons():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('coupons.html')


@app.route('/purchase' , methods=['POST'])   
def purchase():
    if 'user_id' not in session:
        return redirect('/')
    
    return redirect('/')
