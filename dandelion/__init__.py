#!/usr/bin/env python
#coding=utf-8

"""
file: __init__.py
description:
author: Titainium Deng
date: 2011-6-9
"""

from flask import Flask

DEFAULT_APP_NAME = 'dandelion'

DEFAULT_MODULES = ()

def create_app(config=None, modules=None):
    """
    Create the root app, register modules
    """

    if modules is None: modules = DEFAULT_MODULES

    app = Flask(DEFAULT_APP_NAME)

    # config
    app.config.from_pyfile(config)

    # register module
    configure_modules(app, modules)

    return app

def configure_modules(app, modules):
    """
    register module function, will be changed later
    """

    for module, url_prefix in modules:
        app.register_module(module, url_prefix=url_prefix)
