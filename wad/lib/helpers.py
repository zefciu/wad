"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
from webhelpers.html.tags import form, text, submit, end_form, checkbox 
from webhelpers.html.tags import javascript_link, stylesheet_link
from routes import url_for
