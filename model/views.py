from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .database import DataBase

view = Blueprint("views", __name__)

@view.route('/')
@view.route('/home')
def home():
     return render_template('login.html')

@view.route('/base')
def base():
     return render_template('base.html')