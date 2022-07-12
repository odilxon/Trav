from flask import render_template, redirect, flash, request, url_for, Blueprint

from app import db
 

from .models import *
from . import main

 

@main.route('/')
def index():
    return render_template('index.html', style='dark-footer skin-dark-footer')


@main.route('/about')
def about():
    return render_template('about.html', style='dark-footer skin-dark-footer')


@main.route('/tours')
def tours():
    r = db.session.query(ToursCat, ToursInfo).join(ToursInfo, ToursCat.id == ToursInfo.cat_id)
    re = db.session.query(PackDay, ToursInfo).join(ToursInfo, PackDay.id == ToursInfo.pack_id)
    return render_template('tour-list.html', style='dark-footer skin-dark-footer')


@main.route('/hotel')
def hotel():
    return render_template('hotel.html', style='dark-footer skin-dark-footer')


@main.route('/article')
def article():
    return render_template('blogs.html', style='dark-footer skin-dark-footer')


@main.route('/faq')
def faq():
    res = db.session.query(Question, Answer).join(Answer, Question.id == Answer.que_id).all()

    return render_template('faq.html', style='dark-footer skin-dark-footer')


@main.route('/contact')
def contact():
    return render_template('contact.html', style='dark-footer skin-dark-footer')