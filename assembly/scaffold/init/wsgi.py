# -*- coding: utf-8 -*-
""""
Assembly

https://github.com/mardix/assembly
--------------------------------------------------------------------------------

'asm_wsgi.py' is your application's object. It's required by Assembly.

It sets up and initialize all the views per application

--------------------------------------------------------------------------------

# Environment variables

export ASSEMBLY_ENV=Development
export ASSEMBLY_APP=default

## ASSEMBLY_APP
By default, Assembly will attempt to load the 'default' app. 
To specify a different app, set the environment variable 'ASSEMBLY_APP'
to the name of the app to use
ie: 'export ASSEMBLY_APP=default'

## ASSEMBLY_ENV
By default, Assembly will attempt to load the 'Development' config object from './config.py'
To specify a different environment, set the environment variable 'ASSEMEBLY_ENV'
to the environment class name 
ie: 'export ASSEMBLY_ENV=Production'
"""

"""
Import the base Assembly
"""
from assembly import Assembly

"""
Importing Swagger Supporting Library
"""
from flasgger import Swagger

"""
If you want to use your views CLI, you can import them below
"""
import main.cli

"""
APPS = {}
a dict with list of applications to load by name
You can add as many views as you want per application.
Set the environment variable 'ASSEMBLY_APP' to the name of the app to use
ie: 'export ASSEMBLY_APP=default'
"""

APPS = {
    "default": [
        "main"
    ]
}

"""
Initialize the application
the 'app' variable is required
"""
app = Assembly.init(__name__, APPS)

"""
Initialize the Swagger Docs
"""
app.config["SWAGGER"] = {
    "title": app.config.get("SWAGGER_TITLE"),
    "uiversion": app.config.get("SWAGGER_UI_VERSION"),
}

Swagger(app)
