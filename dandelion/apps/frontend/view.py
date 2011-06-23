#!/usr/bin/env python
#coding=utf-8

from flask import Module
from flask import render_template

frontend = Module(__name__, 'frontend')

@frontend.route("/")
def index():

    return render_template("index.html")

