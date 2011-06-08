#!/usr/bin/env python
#coding=utf-8

"""
file: manage.py
description: This file is used to handle the management of the site from shell, user
             can add shell command here, like 'runserver' etc.
author: Titainium Deng
date: 2011-6-8
"""

from flaskext.script import Server, Manager

from dandelion import create_app

manager = Manager(create_app('config.cfg'))

manager.add_command("runserver", Server('0.0.0.0',port=8080))

if __name__ == "__main__":
    manager.run()
