"""
This module provides any dynamically loadable code for the Bit.ly 
Framework Extension such as hook and handler registration.  Additional 
classes and functions exist in cement2.lib.ext_bitly.
    
"""

from cement2.core import hook

def shorten_url(url):
    
@hook.register()
def cement_post_setup_hook(app):
    """
    Sets the default [bitly] config section options.
    
    """
    # Add default config
    defaults = dict()
    defaults['bitly'] = dict()
    defaults['bitly']['enabled'] = True
    defaults['bitly']['user'] = ''
    defaults['bitly']['apikey'] = ''
    defaults['bitly']['baseurl'] = 'http://api.bit.ly/v3/shorten/'
    app.config.merge(defaults, override=False)
    app.shorten_url = shorten_url