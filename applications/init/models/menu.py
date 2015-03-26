# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('MiTrend'), _class="brand",_href="http://mitrend.com")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Benjamin Bertka <benjamin.bertka@emc.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    #(T('Home'), False, '/', [])
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # useful links to internal and external resources
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [
      #  (SPAN('Tools', _class='highlighted'), False, '#', [
      #  (T('MiTrend Mobile'), False, "/mitrend"),])
        ]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
