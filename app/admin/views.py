from flask import render_template, redirect, flash, request, url_for
from . import admin


@admin.route('/')
def index():
    return render_template('index1.html')
