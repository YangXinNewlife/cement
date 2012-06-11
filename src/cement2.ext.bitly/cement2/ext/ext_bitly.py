"""
This module provides any dynamically loadable code for the Bit.ly 
Framework Extension such as hook and handler registration.  Additional 
classes and functions exist in cement2.lib.ext_bitly.
    
"""

from cement2.core import hook, backend
from cement2.lib.ext_bitly import Bitly

@hook.register()
def cement_post_setup_hook(app):
    # Add default config
    defaults = backend.defaults('bitly')
    defaults['bitly']['enabled'] = True
    defaults['bitly']['user'] = None
    defaults['bitly']['apikey'] = None
    defaults['bitly']['baseurl'] = 'https://api-ssl.bitly.com/v3/shorten/'
    app.config.merge(defaults, override=False)
    
    bitly = Bitly(
        user=app.config.get('bitly', 'user'),
        apikey=app.config.get('bitly', 'apikey'),
        baseurl=app.config.get('bitly', 'baseurl'),
        enabled=app.config.get('bitly', 'enabled')
        )
    app.extend('bitly', bitly)