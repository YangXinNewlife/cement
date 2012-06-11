"""Tests for cement2.ext.ext_json."""

import unittest
from nose.tools import ok_, eq_, raises
from cement2.core import hook, backend
from cement2 import test_helper as _t

_t.prep()
from cement2.ext import ext_bitly

def import_bitly():
    from cement2.ext import ext_bitly
    hook.register()(ext_bitly.cement_post_setup_hook)
    
class BitlyExtTestCase(unittest.TestCase):
    def setUp(self):
        defaults = backend.defaults('test', 'bitly')
        #defaults['bitly']['user'] = 'derks'
        #defaults['bitly']['apikey'] = 'R_a6ff6b61586df42c0b5460bc79835bbb'
        self.app = _t.prep('tests', 
            extensions=['bitly'], 
            config_defaults=defaults,
            argv='default',
            )
        import_bitly()
    
    def test_json(self):    
        self.app.setup()
        res = self.app.bitly.shorten('http://builtoncement.org')
