#!/usr/bin/env python
# coding=utf-8

from dadelion import db

class event(db.Document):
    description = db.StringField()
    register_time = db.DateTimeField()

